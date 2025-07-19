from flask import Blueprint, request as flask_request
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

        #temp return 
        return Response(data={"success": True, "message": "Task stopped successfully", "task_id": task_id})

        # # Replace with your actual API endpoint and authentication as needed
        # API_KEY = "your_api_key_here"
        # BASE_URL = "https://api.browser-use.com/api/v1"
        # HEADERS = {"Authorization": f"Bearer {API_KEY}"}

        # # Stop the task
        # stop_response = requests.post(f"{BASE_URL}/stop-task", headers=HEADERS, json={"task_id": task_id})
        # if stop_response.status_code == 200:
        #     result = stop_response.json()
        #     return Response(data={"success": True, "result": result}, metadata={"stopped_task_id": task_id})
        # else:
        #     return Response.error(f"Failed to stop task: {stop_response.text}")
    except Exception as e:
        return Response.error(str(e))
