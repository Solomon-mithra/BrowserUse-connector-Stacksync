# Create Scheduled Task Module

Creates a new scheduled browser automation task to run at regular intervals or based on a cron expression.

## Endpoints
- /execute: Creates a scheduled task
- /content: (optional, for managed dropdowns)
- /schema: Returns the schema for this module

## Parameters
- task (string, required): Instructions for what the agent should do
- schedule_type (string, required): Type of schedule: "interval" or "cron"
- interval_minutes (integer): Minutes between runs (required for interval schedule)
- cron_expression (string): Cron expression for scheduling (required for cron schedule)
- start_at (string): When to start the schedule (ISO 8601 format, defaults to now)
- end_at (string): When to end the schedule (ISO 8601 format, defaults to 1 year from now)
- secrets (object): Dictionary of secrets to be used by the agent
- allowed_domains (array): List of domains the agent is allowed to visit
- save_browser_data (boolean, default: false): Whether to save browser cookies and data between runs
- structured_output_json (string): JSON schema for structured output
- llm_model (string, default: "gpt-4o"): LLM model to use
- use_adblock (boolean, default: true): Whether to use an adblocker
- use_proxy (boolean, default: true): Whether to use a proxy
- proxy_country_code (string, default: "us"): Country code for residential proxy
- highlight_elements (boolean, default: true): Whether to highlight elements on the page
- included_file_names (array): File names to include in the task
- browser_viewport_width (integer, default: 1280): Width of browser viewport in pixels
- browser_viewport_height (integer, default: 960): Height of browser viewport in pixels
- max_agent_steps (integer, default: 75): Maximum number of agent steps (max: 200)
- enable_public_share (boolean, default: false): Whether to enable public sharing of task executions
