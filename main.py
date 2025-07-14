from keep_alive import keep_alive
import requests, time, pytz
from datetime import datetime
from shine_scraper import fetch_shine_jobs
from indeed_scraper import fetch_indeed_jobs
from telegram_utils import send_telegram_message, format_jobs

keep_alive()

def run_bot():
    jobs = fetch_shine_jobs() + fetch_indeed_jobs()
    now = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%b %I:%M %p')
    message = f"🕒 <b>Job Update @ {now}</b>\n\n" + format_jobs(jobs)
    send_telegram_message(message)

while True:
    now = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%H:%M')
    if now in ["09:00", "12:00", "16:00"]:
        run_bot()
        time.sleep(60)
    time.sleep(30)