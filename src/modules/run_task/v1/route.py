import requests
from workflows_cdk import Response, Request
from main import router
from flask import request as flask_request

def extract_api_key(api_connection: dict) -> str:
    if not api_connection:
        return None
    return api_connection.get("connection_data", {}).get("value", {}).get("api_key_bearer")

def run_browser_task(access_token: str, data: dict):
    try:
        url = "https://api.browser-use.com/api/v1/run-task"
        payload = {
            "task": data.get("task"),
            "secrets": data.get("secrets", {}),
            "allowed_domains": data.get("allowed_domains", []),
            "save_browser_data": data.get("save_browser_data", True),
            "structured_output_json": data.get("structured_output_json", ""),
            "llm_model": data.get("llm_model", "gpt-4o"),
            "use_adblock": data.get("use_adblock", True),
            "use_proxy": data.get("use_proxy", True),
            "proxy_country_code": data.get("proxy_country_code", "us"),
            "highlight_elements": data.get("highlight_elements", True),
            "included_file_names": [],
            "browser_viewport_width": data.get("browser_viewport_width", 123),
            "browser_viewport_height": data.get("browser_viewport_height", 123),
            "max_agent_steps": data.get("max_agent_steps", 123),
            "enable_public_share": data.get("enable_public_share", False)
        }
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    
         # Instead of making the API call, just return what would be sent
        # return {
        #     "url": url,
        #     "payload": payload,
        #     "headers": headers
        # }

        response = requests.request("POST", url, json=payload, headers=headers)
        print("Response:", response.text)
        
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        # Try to extract error message from response
        try:
            return {"error": str(e), "details": e.response.json() if e.response else None}
        except Exception:
            return {"error": str(e)}

@router.route("/execute", methods=["POST"])
def execute():
    """
    Accepts schema input and returns a structured result, following documentation example.
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

        result = run_browser_task(access_token=access_token, data=data)

        if "error" in result:
            return Response.error(result["error"])

        return Response(
            data=result,
            metadata={"processed_at": "2024-01-01T00:00:00Z"}
        )

    except Exception as e:
        return Response.error(str(e))
