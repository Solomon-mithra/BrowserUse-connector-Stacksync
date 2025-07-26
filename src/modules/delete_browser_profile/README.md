# Delete Browser Profile Module

This module deletes a browser profile and all associated browser data. This action cannot be undone.

## Endpoints
- **POST /execute**: Delete browser profile. Requires `api_connection` and `profile_id` in the request body.

## Fields
- **api_connection** (connection, required): API connection for BrowserUse
- **profile_id** (string, required): ID of the browser profile to delete

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "profile_id": "profile_1234567890abcdef"
}
```
