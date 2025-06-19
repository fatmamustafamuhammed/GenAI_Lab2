import os
import re
import smtplib
from email.mime.text import MIMEText
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from dotenv import load_dotenv
import dateparser
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

scheduler = BackgroundScheduler()
scheduler.start()

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def parse_reminder(reminder_text):
    # Try to extract the task and date/time using regex and dateparser
    match = re.search(r"remind me to (.+) on (.+)", reminder_text, re.IGNORECASE)
    if match:
        task = match.group(1).strip()
        date_time_str = match.group(2).strip()
        # Try parsing with current year
        date_time = dateparser.parse(date_time_str)
        if date_time and date_time < datetime.now():
            # If the date is in the past, try next year
            date_time = dateparser.parse(
                date_time_str + f" {datetime.now().year + 1}"
            )
        return task, date_time
    return None, None

def schedule_reminder(task, remind_time, to_email):
    scheduler.add_job(send_email, 'date', run_date=remind_time, args=[
        'Reminder', f'Reminder: {task}', to_email
    ])

if __name__ == '__main__':
    print('AI Reminder Agent is running.')
    # Example usage (replace with OpenAI Agent SDK integration):
    user_input = input('Enter your reminder: ')
    user_email = input('Enter your email: ')
    task, remind_time = parse_reminder(user_input)
    if task and remind_time:
        schedule_reminder(task, remind_time, user_email)
        print(f'Reminder set for {remind_time}.')
    else:
        print('Could not parse your reminder. Please use the format: "remind me to [task] on [YYYY-MM-DD HH:MM]".')
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
