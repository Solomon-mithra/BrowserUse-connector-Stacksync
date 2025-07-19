# Get Task Output File Module

Returns a presigned URL for downloading a file from the task output files.

## Endpoints
- /execute: Retrieves a presigned URL for the specified output file
- /content: (optional, not needed for this module)
- /schema: Returns the schema for this module

## Parameters
- task_id (string, required): ID of the task
- file_name (string, required): Name of the output file
