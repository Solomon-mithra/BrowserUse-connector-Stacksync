# Update Scheduled Task Module

Updates a scheduled browser automation task with partial updates.

## Endpoints
- /execute: Updates the specified scheduled task
- /content: (optional, not needed for this module)
- /schema: Returns the schema for this module

## Parameters
- task_id (string, required): ID of the scheduled task to update
- Any combination of scheduled task configuration fields (all optional except task_id)
