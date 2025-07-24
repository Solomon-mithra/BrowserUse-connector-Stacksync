# Create Scheduled Task Module

## Purpose
Create a new scheduled task to run at regular intervals or based on a cron expression. Automate recurring browser automation tasks.

## Endpoints
- `/execute` (POST): Creates a scheduled task with interval or cron schedule.

## Fields
- **api_connection**: API connection to Browser Use.
- **task**: Instructions for the agent.
- **schedule_type**: "interval" or "cron".
- **interval_minutes**: Minutes between runs (for interval schedule).
- **cron_minute, cron_hour, cron_day_of_month, cron_month, cron_day_of_week**: Selectors for cron schedule.
- **start_at, end_at**: When to start/end the schedule.
- **secrets, allowed_domains, save_browser_data, structured_output_json, llm_model, use_adblock, use_proxy, proxy_country_code, highlight_elements, included_file_names, browser_viewport_width, browser_viewport_height, max_agent_steps, enable_public_share**: All supported options.

## Example Request (cron)
```
{
  "api_connection": { ... },
  "task": "Do something",
  "schedule_type": "cron",
  "cron_minute": "0",
  "cron_hour": "9",
  "cron_day_of_month": "*",
  "cron_month": "*",
  "cron_day_of_week": "1-5"
}
```

## Example Request (interval)
```
{
  "api_connection": { ... },
  "task": "Do something",
  "schedule_type": "interval",
  "interval_minutes": 60
}
```
