# Create Browser Profile Module

This module creates a new browser profile in BrowserUse with custom settings for ad blocking, proxy usage, and viewport dimensions.

## Endpoints
- **POST /execute**: Create a new browser profile. Requires `api_connection` and profile fields in the request body.

## Fields
- **profile_name** (string, required): Name of the browser profile
- **description** (string, optional): Description of the profile
- **persist** (boolean, default: true): Save cookies, local storage, and session data between tasks
- **ad_blocker** (boolean, default: true): Block ads and popups during automated tasks
- **proxy** (boolean, default: true): Route traffic through mobile proxies for better stealth
- **proxy_country_code** (string, default: "US"): Country code for the proxy
- **browser_viewport_width** (integer, default: 1280): Browser viewport width in pixels
- **browser_viewport_height** (integer, default: 960): Browser viewport height in pixels

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "profile_name": "My Profile",
  "description": "Test profile",
  "persist": true,
  "ad_blocker": true,
  "proxy": true,
  "proxy_country_code": "US",
  "browser_viewport_width": 1280,
  "browser_viewport_height": 960
}
```
