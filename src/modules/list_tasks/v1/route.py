import requests
from workflows_cdk import Response, Request
from main import router
from flask import request as flask_request

def extract_api_key(api_connection: dict) -> str:
    if not api_connection:
        return None
    return api_connection.get("connection_data", {}).get("value", {}).get("api_key_bearer")

def list_tasks(access_token: str):
    url = "https://api.browser-use.com/api/v1/tasks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=20)
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
    Get a paginated list of all tasks for the user.
    Expects 'api_connection' in the request body.
    """
    try:
        req = Request(flask_request)
        data = req.data

        api_connection = data.get("api_connection")
        access_token = extract_api_key(api_connection)
        if not access_token:
            return Response.error("Missing API key in api_connection.")

        result = list_tasks(access_token=access_token)

        if "error" in result:
            return Response.error(result["error"])

        return Response(
            data=result,
            metadata={"processed_at": "2024-01-01T00:00:00Z"}
        )
    except Exception as e:
        return Response.error(str(e))
