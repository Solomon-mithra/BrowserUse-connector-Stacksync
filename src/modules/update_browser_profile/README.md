# Update Browser Profile Module

This module updates a browser profile with partial updates. Only the fields you want to change need to be included.

## Endpoints
- **POST /execute**: Update browser profile. Requires `api_connection` and `profile_id`. Any other fields are optional and will be updated if provided.

## Fields
- **api_connection** (connection, required): API connection for BrowserUse
- **profile_id** (string, required): ID of the browser profile to update
- **profile_name** (string, optional): Name of the browser profile
- **description** (string, optional): Description of the profile
- **persist** (boolean, optional): Save cookies, local storage, and session data between tasks
- **ad_blocker** (boolean, optional): Block ads and popups during automated tasks
- **proxy** (boolean, optional): Route traffic through mobile proxies for better stealth
- **proxy_country_code** (string, optional): Country code for the proxy
- **browser_viewport_width** (integer, optional): Browser viewport width in pixels
- **browser_viewport_height** (integer, optional): Browser viewport height in pixels

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "profile_id": "profile_1234567890abcdef",
  "profile_name": "Updated Name"
}
```
