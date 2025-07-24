# Update Scheduled Task Module

## Purpose
Update a scheduled task with partial updates. You can update any combination of the task configuration fields without affecting the others.

## Endpoints
- `/execute` (POST): Updates a scheduled task with partial updates.

## Fields
- **api_connection**: API connection to Browser Use.
- **task_id**: ID of the scheduled task to update.
- All other fields are optional and can be updated individually or in combination.

## Example Request
```
{
  "api_connection": { ... },
  "task_id": "abc123",
  "task": "New instructions",
  "interval_minutes": 60,
  "is_active": true
}
```

## Example Response
```
{
  "data": { ...updated scheduled task info... },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```
