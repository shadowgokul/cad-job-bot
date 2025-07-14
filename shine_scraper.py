import requests
from bs4 import BeautifulSoup

def fetch_shine_jobs():
    url = "https://www.shine.com/job-search/cad-design-engineer-jobs-in-tamil-nadu"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = []
    for job in soup.find_all("li", class_="w-100"):
        title = job.find("h2").text.strip()
        link = "https://www.shine.com" + job.find("a")["href"]
        company = job.find("div", class_="jobCard_compName__xq9pJ")
        location = job.find("li", class_="jobCard_location__rRusu")
        full = job.get_text().lower()
        if any(k in full for k in ["catia", "nx", "autocad", "solidworks", "unigraphics"]):
            jobs.append({
                "title": title,
                "company": company.text.strip() if company else "N/A",
                "location": location.text.strip() if location else "N/A",
                "link": link
            })
    return jobs