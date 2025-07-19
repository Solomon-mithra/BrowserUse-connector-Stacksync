# Delete Scheduled Task Module

Deletes a scheduled task from the browser automation system. This prevents future runs of the task; any currently running instances will be allowed to complete.

## Endpoints
- `/execute`: Deletes the scheduled task specified by `task_id`.
- `/schema`: Returns the schema for the delete action.

## Usage
Provide the `task_id` of the scheduled task to delete.
