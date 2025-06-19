# AI Reminder Agent

This project is a Python script for an AI reminder agent. The agent accepts natural language tasks like "Please remind me to [task] on [date/time]" and sends an email with the reminder at the specified time using Gmail SMTP. APScheduler is used for scheduling reminders.

---

## Updates & Changes

### 1. Dependency Fixes

- **Removed**: `openai-agent-sdk` (not available on PyPI)
- **Added**: Official `openai` package and `dateparser` for natural language date parsing

### 2. Natural Language Date Parsing

- The agent now uses `dateparser` to understand flexible date/time expressions (e.g., "June 20th at 3pm").
- If the user omits the year, the script defaults to the current year or next year if the date has already passed.

### 3. Requirements Update

- `requirements.txt` now contains:
  ```
  APScheduler
  python-dotenv
  openai
  dateparser
  ```

### 4. Reminder Parsing Logic

- The reminder parsing function was updated to:
  - Extract the task and date/time from natural language input.
  - Handle ambiguous dates and avoid deprecation warnings.

---

## Setup & Usage

1. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Create a `.env` file** in the project root:

   ```
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   OPENAI_API_KEY=your_openai_api_key
   ```

3. **Run the agent:**

   ```sh
   python reminder_agent.py
   ```

4. **Example usage:**
   ```
   Please remind me to call John on June 20th at 3pm
   ```

---

## Notes

- Make sure to use an [App Password](https://support.google.com/accounts/answer/185833) for Gmail if you have 2FA enabled.
- The agent will send an email reminder at the scheduled time using the provided Gmail credentials.

---

## Run in Terminal

- $ python reminder_agent.py
  AI Reminder Agent is running.
  Enter your reminder: Please remind me to call John on June 20th at 3pm
  Enter your email: fmomen738@gmail.com
  Reminder set for 2025-06-20 15:00:00.
