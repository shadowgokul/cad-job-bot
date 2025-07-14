import requests
from bs4 import BeautifulSoup

def fetch_indeed_jobs():
    url = "https://in.indeed.com/jobs?q=CAD+Design+Engineer&l=Tamil+Nadu"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = []
    for card in soup.find_all("div", class_="job_seen_beacon"):
        title = card.find("h2").text.strip()
        link = "https://in.indeed.com" + card.find("a")["href"]
        company = card.find("span", class_="companyName")
        location = card.find("div", class_="companyLocation")
        full = card.get_text().lower()
        if any(k in full for k in ["catia", "nx", "autocad", "solidworks", "unigraphics"]):
            jobs.append({
                "title": title,
                "company": company.text.strip() if company else "N/A",
                "location": location.text.strip() if location else "N/A",
                "link": link
            })
    return jobs