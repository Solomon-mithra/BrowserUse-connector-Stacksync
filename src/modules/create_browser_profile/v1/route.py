import requests
from workflows_cdk import Response, Request
from main import router
from flask import request as flask_request

def extract_api_key(api_connection: dict) -> str:
    if not api_connection:
        return None
    return api_connection.get("connection_data", {}).get("value", {}).get("api_key_bearer")

def create_browser_profile(access_token: str, data: dict):
    url = "https://api.browser-use.com/api/v1/browser-profiles"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    # Build payload with defaults and type safety
    payload = {
        "profile_name": data.get("profile_name"),
        "description": data.get("description", ""),
        "persist": bool(data.get("persist", True)),
        "ad_blocker": bool(data.get("ad_blocker", True)),
        "proxy": bool(data.get("proxy", True)),
        "proxy_country_code": data.get("proxy_country_code", "US"),
        "browser_viewport_width": int(data.get("browser_viewport_width", 1280)),
        "browser_viewport_height": int(data.get("browser_viewport_height", 960))
    }
    print(f"Creating browser profile with payload: {payload}")  # Debugging line
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        try:
            return {"error": str(e), "details": e.response.json() if e.response else None}
        except Exception:
            return {"error": str(e)}

@router.route("/execute", methods=["POST"])
def execute():
    """
    Create a new browser profile.
    Expects 'api_connection' and profile fields in the request body.
    """
    try:
        req = Request(flask_request)
        data = req.data

        api_connection = data.get("api_connection")
        access_token = extract_api_key(api_connection)
        if not access_token:
            return Response.error("Missing API key in api_connection.")

        # Validate required field
        if not data.get("profile_name"):
            return Response.error("Missing required field: profile_name.")

        # Pass all data for payload construction
        result = create_browser_profile(access_token=access_token, data=data)

        if "error" in result:
            return Response.error(result["error"])

        return Response(
            data=result,
            metadata={"processed_at": "2025-07-25T00:00:00Z"}
        )
    except Exception as e:
        return Response.error(str(e))
