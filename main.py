import requests
from bs4 import BeautifulSoup
import time

# === TELEGRAM SETTINGS ===
BOT_TOKEN = "your_bot_token_here"
CHAT_ID = "your_chat_id_here"

# === FILTER CRITERIA ===
keywords = ["diploma mechanical engineer", "cad designer", "graphic designer"]
locations = ["Tamil Nadu", "Bangalore", "Chennai", "Coimbatore", "Madurai", "Trichy", "Salem"]

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    requests.post(url, data=data)

def scrape_shine_jobs():
    url = "https://www.shine.com/job-search/diploma-mechanical-engineer-jobs"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    jobs = []

    for job_card in soup.select(".jobCard"):
        try:
            title = job_card.select_one(".job-title").get_text(strip=True)
            company = job_card.select_one(".job-company").get_text(strip=True)
            location = job_card.select_one(".job-location").get_text(strip=True)
            exp = job_card.select_one(".job-experience").get_text(strip=True)
            link = "https://www.shine.com" + job_card.a["href"]

            if (
                any(loc.lower() in location.lower() for loc in locations) and
                "2" in exp and
                any(k.lower() in title.lower() for k in keywords)
            ):
                job_text = f"<b>{title}</b>\n{company}\n{location} | Exp: {exp}\n🔗 {link}"
                jobs.append(job_text)
        except:
            continue
    return jobs

def job_runner():
    jobs = scrape_shine_jobs()
    if jobs:
        for job in jobs:
            send_telegram_alert(job)
    else:
        send_telegram_alert("😢 No new jobs found at this time.")

# Run every 6 hours
if __name__ == "__main__":
    while True:
        print("🔍 Checking for jobs...")
        job_runner()
        time.sleep(6 * 60 * 60)  # 6 hours
