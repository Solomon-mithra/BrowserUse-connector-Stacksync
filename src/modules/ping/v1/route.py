from flask import request as flask_request
from workflows_cdk import Response, Request
from main import router

@router.route("/execute", methods=["POST"])
def execute():
    try:
        # No input fields required
        return Response(data={"success": True, "message": "Server is running and responding."}, metadata={"ping": True})
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
