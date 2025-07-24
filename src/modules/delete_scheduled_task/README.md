# Delete Scheduled Task Module

## Purpose
Delete a scheduled task. This will prevent any future runs of this task. Any currently running instances will be allowed to complete.

## Endpoints
- `/execute` (POST): Deletes a scheduled task for a given scheduled task ID.

## Fields
- **api_connection**: API connection to Browser Use.
- **task_id**: ID of the scheduled task to delete.

## Example Request
```
{
  "api_connection": { ... },
  "task_id": "abc123"
}
```

## Example Response
```
{
  "data": { "success": true },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```
