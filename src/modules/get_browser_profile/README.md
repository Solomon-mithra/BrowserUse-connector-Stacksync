# Get Browser Profile Module

This module returns information about a specific browser profile and its configuration settings.

## Endpoints
- **POST /execute**: Get browser profile info. Requires `api_connection` and `profile_id` in the request body.

## Fields
- **api_connection** (connection, required): API connection for BrowserUse
- **profile_id** (string, required): ID of the browser profile to retrieve

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "profile_id": "profile_1234567890abcdef"
}
```
