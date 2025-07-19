# List Scheduled Tasks Module

Returns a paginated list of all scheduled browser automation tasks belonging to the user.

## Endpoints
- /execute: Retrieves a paginated list of scheduled tasks
- /content: (optional, not needed for this module)
- /schema: Returns the schema for this module

## Parameters
- page (integer, default: 1): Page number (minimum: 1)
- limit (integer, default: 10): Number of items per page (minimum: 1)
