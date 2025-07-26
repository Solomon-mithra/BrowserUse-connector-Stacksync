import requests
from workflows_cdk import Response, Request
from main import router
from flask import request as flask_request

def extract_api_key(api_connection: dict) -> str:
    if not api_connection:
        return None
    return api_connection.get("connection_data", {}).get("value", {}).get("api_key_bearer")

def pause_task(access_token: str, task_id: str):
    url = "https://api.browser-use.com/api/v1/pause-task"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {"task_id": task_id}
    try:
        response = requests.put(url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        return response.json() if response.text else {"success": True}
    except requests.RequestException as e:
        try:
            return {"error": str(e), "details": e.response.json() if e.response else None}
        except Exception:
            return {"error": str(e)}

@router.route("/execute", methods=["POST"])
def execute():
    """
    Pause a running browser automation task. Expects 'api_connection' and 'task_id' in the request body.
    """
    try:
        req = Request(flask_request)
        data = req.data

        api_connection = data.get("api_connection")
        access_token = extract_api_key(api_connection)
        if not access_token:
            return Response.error("Missing API key in api_connection.")

        task_id = data.get("task_id")
        if not task_id:
            return Response.error("Missing required field: task_id.")

        result = pause_task(access_token=access_token, task_id=task_id)

        if "error" in result:
            return Response.error(result["error"])

        return Response(
            data=result,
            metadata={"processed_at": "2025-07-26T00:00:00Z"}
        )
    except Exception as e:
        return Response.error(str(e))
