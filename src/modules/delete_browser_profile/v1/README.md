# Delete Browser Profile v1

This module allows you to delete a browser profile and all associated browser data using the BrowserUse API.

## Endpoints
- **POST /execute**: Delete browser profile.

## Required Fields
- `api_connection`: API connection for BrowserUse
- `profile_id`: ID of the browser profile to delete

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "profile_id": "profile_1234567890abcdef"
}
```
