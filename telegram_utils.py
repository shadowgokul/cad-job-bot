import requests

BOT_TOKEN = "8138265819:AAErpa3am4AACHXSPBQQKos7CSGm61sINuU"
CHAT_ID = "1731604302"

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    })

def format_jobs(jobs):
    if not jobs:
        return "😴 No new CAD jobs right now."
    msg = ""
    for job in jobs:
        msg += f"🔹 <b>{job['title']}</b>\n🏢 {job['company']}\n📍 {job['location']}\n🔗 <a href='{job['link']}'>Apply</a>\n\n"
    return msg