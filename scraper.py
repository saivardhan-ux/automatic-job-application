import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_jobs():
    url = "https://www.indeed.com/jobs?q=vlsi+fresher&l=India"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = []
    for div in soup.find_all("div", class_="result"):
        title = div.find("h2").text.strip() if div.find("h2") else "N/A"
        company = div.find("span", class_="company").text.strip() if div.find("span", class_="company") else "N/A"
        link = "https://indeed.com" + div.find("a")["href"]
        jobs.append([title, company, link, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    with open("log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(jobs)

    print("Scraping done! Jobs saved to log.csv")

if __name__ == "__main__":
    scrape_jobs()