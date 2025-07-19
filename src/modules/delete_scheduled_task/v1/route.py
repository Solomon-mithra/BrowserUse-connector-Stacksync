from flask import request as flask_request
from workflows_cdk import Response, Request
import requests
from main import router

@router.route("/execute", methods=["POST"])
def execute():
    try:
        req = Request(flask_request)
        data = req.data
        task_id = data.get("task_id")
        if not task_id:
            return Response.error("Missing required parameter: task_id")
        # Temporary mock response
        return Response(data={"success": True, "message": f"Scheduled task {task_id} deleted", "task_id": task_id}, metadata={"deleted": True})
        # # Replace with your actual API endpoint and authentication as needed
        # API_KEY = "your_api_key_here"
        # BASE_URL = "https://api.browser-use.com/api/v1"
        # HEADERS = {"Authorization": f"Bearer {API_KEY}"}
        # delete_response = requests.delete(f"{BASE_URL}/scheduled-task/{task_id}", headers=HEADERS)
        # if delete_response.status_code == 200:
        #     result = delete_response.json()
        #     return Response(data=result, metadata={"deleted": True})
        # else:
        #     return Response.error(f"Failed to delete scheduled task: {delete_response.text}")
    except Exception as e:
        return Response.error(str(e))

@router.route("/schema", methods=["POST"])
def schema():
    try:
        with open("schema.json", "r") as f:
            base_schema = f.read()
        return Response(data=base_schema)
    except Exception as e:
        return Response.error(str(e))
