import requests
from workflows_cdk import Response, Request
from main import router
from flask import request as flask_request

def extract_api_key(api_connection: dict) -> str:
    if not api_connection:
        return None
    return api_connection.get("connection_data", {}).get("value", {}).get("api_key_bearer")

def build_cron_expression(minute, hour, day_of_month, month, day_of_week):
    return f"{minute} {hour} {day_of_month} {month} {day_of_week}"

def update_scheduled_task(access_token: str, task_id: str, data: dict):
    url = f"https://api.browser-use.com/api/v1/scheduled-task/{task_id}"
    payload = {}
    # Only include fields present in the request for partial update
    for field in [
        "task", "schedule_type", "interval_minutes", "cron_expression", "start_at", "end_at", "is_active",
        "use_adblock", "use_proxy", "highlight_elements", "llm_model", "save_browser_data", "structured_output_json"
    ]:
        if field in data:
            payload[field] = data[field]
    # If schedule_type is cron and cron fields are present, build cron_expression
    if data.get("schedule_type") == "cron" and all(k in data for k in ["cron_minute", "cron_hour", "cron_day_of_month", "cron_month", "cron_day_of_week"]):
        payload["cron_expression"] = build_cron_expression(
            data["cron_minute"],
            data["cron_hour"],
            data["cron_day_of_month"],
            data["cron_month"],
            data["cron_day_of_week"]
        )
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.put(url, json=payload, headers=headers, timeout=30)
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
    Update a scheduled task with partial updates.
    Expects 'api_connection', 'task_id', and any fields to update in the request body.
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

        result = update_scheduled_task(access_token=access_token, task_id=task_id, data=data)

        if "error" in result:
            return Response.error(result["error"])

        return Response(
            data=result,
            metadata={"processed_at": "2024-01-01T00:00:00Z"}
        )
    except Exception as e:
        return Response.error(str(e))
