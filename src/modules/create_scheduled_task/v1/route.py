import requests
from workflows_cdk import Response, Request
from main import router
from flask import request as flask_request
from pathlib import Path

def extract_api_key(api_connection: dict) -> str:
    if not api_connection:
        return None
    return api_connection.get("connection_data", {}).get("value", {}).get("api_key_bearer")

def build_cron_expression(minute, hour, day_of_month, month, day_of_week):
    return f"{minute} {hour} {day_of_month} {month} {day_of_week}"

def create_scheduled_task(access_token: str, data: dict):
    url = "https://api.browser-use.com/api/v1/scheduled-task"
    # Build cron_expression from UI fields
    if data.get("schedule_type") == "cron":
        cron_expression = build_cron_expression(
            data.get("cron_minute", "0"),
            data.get("cron_hour", "9"),
            data.get("cron_day_of_month", "*"),
            data.get("cron_month", "*"),
            data.get("cron_day_of_week", "*")
        )
        data["cron_expression"] = cron_expression
    payload = {
        "task": data.get("task"),
        "schedule_type": data.get("schedule_type"),
        "interval_minutes": data.get("interval_minutes"),
        "cron_expression": data.get("cron_expression"),
        "start_at": data.get("start_at"),
        "end_at": data.get("end_at"),
        "secrets": data.get("secrets", {}),
        "allowed_domains": data.get("allowed_domains", []),
        "save_browser_data": data.get("save_browser_data", False),
        "structured_output_json": data.get("structured_output_json", ""),
        "llm_model": data.get("llm_model", "gpt-4o"),
        "use_adblock": data.get("use_adblock", True),
        "use_proxy": data.get("use_proxy", True),
        "proxy_country_code": data.get("proxy_country_code", "us"),
        "highlight_elements": data.get("highlight_elements", True),
        "browser_viewport_width": data.get("browser_viewport_width", 1280),
        "browser_viewport_height": data.get("browser_viewport_height", 960),
        "max_agent_steps": data.get("max_agent_steps", 75),
        "enable_public_share": data.get("enable_public_share", False)
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
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
    Create a new scheduled task to run at regular intervals or based on a cron expression.
    Expects all required fields in the request body.
    """
    try:
        req = Request(flask_request)
        data = req.data

        api_connection = data.get("api_connection")
        access_token = extract_api_key(api_connection)
        if not access_token:
            return Response.error("Missing API key in api_connection.")

        if not data.get("task"):
            return Response.error("Missing required field: task.")
        if not data.get("schedule_type"):
            return Response.error("Missing required field: schedule_type.")

        result = create_scheduled_task(access_token=access_token, data=data)

        if "error" in result:
            return Response.error(result["error"])

        return Response(
            data=result,
            metadata={"processed_at": "2024-01-01T00:00:00Z"}
        )
    except Exception as e:
        return Response.error(str(e))



# @router.route("/schema", methods=["POST", "GET"])
# def schema():
#     import json
#     try:
#         request = Request(flask_request)
#         data = request.data
#         print("Received data for schema:", data)
#         # Get the current form data
#         form_data = data.get("form_data", {})

#         print("Received form data:", form_data)

#         # Load your base schema from the schema.json file
#         with open(Path(__file__).parent / "schema.json", "r") as f:
#             base_schema = json.load(f)
#         print("Base schema loaded:", base_schema)
#         # # Apply any dynamic modifications based on form_data
#         # # For example, modify field visibility or validation

#         return Response(data=base_schema)

#     except Exception as e:
#         return Response.error(str(e))
