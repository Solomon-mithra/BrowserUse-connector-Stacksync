import requests
from workflows_cdk import Response, Request
from main import router
from flask import request as flask_request

def extract_api_key(api_connection: dict) -> str:
    if not api_connection:
        return None
    return api_connection.get("connection_data", {}).get("value", {}).get("api_key_bearer")

def update_browser_profile(access_token: str, profile_id: str, data: dict):
    url = f"https://api.browser-use.com/api/v1/browser-profiles/{profile_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    # Only include fields present in data for partial update
    allowed_fields = [
        "profile_name", "description", "persist", "ad_blocker", "proxy", "proxy_country_code", "browser_viewport_width", "browser_viewport_height"
    ]
    # Only include fields that are present and not None/empty
    def is_filled(val):
        return val not in [None, "", []]
    payload = {k: data[k] for k in allowed_fields if k in data and is_filled(data[k])}
    try:
        response = requests.put(url, headers=headers, json=payload)
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
    Update a browser profile. Expects 'api_connection', 'profile_id', and any fields to update in the request body.
    """
    try:
        req = Request(flask_request)
        data = req.data

        api_connection = data.get("api_connection")
        access_token = extract_api_key(api_connection)
        if not access_token:
            return Response.error("Missing API key in api_connection.")

        profile_id = data.get("profile_id")
        if not profile_id:
            return Response.error("Missing required field: profile_id.")

        # Remove api_connection and profile_id from data for payload
        update_data = {k: v for k, v in data.items() if k not in ["api_connection", "profile_id"]}

        if not update_data:
            return Response.error("No fields provided to update.")

        result = update_browser_profile(access_token=access_token, profile_id=profile_id, data=update_data)

        if "error" in result:
            return Response.error(result["error"])

        return Response(
            data=result,
            metadata={"processed_at": "2025-07-25T00:00:00Z"}
        )
    except Exception as e:
        return Response.error(str(e))
