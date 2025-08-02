import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

def log_to_sheets(title, company, link):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # ✅ Replace this path with your exact file path if different
    creds_path = "C:/Users/saivardhan/Downloads/job_bot (1)/job-bot/credentials.json"
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)

    client = gspread.authorize(creds)
    sheet = client.open("Job Logs").sheet1
    sheet.append_row(["Manual Entry", title, company, link])
    print("✅ Logged to Google Sheet.")

if __name__ == "__main__":
    log_to_sheets("DFT Intern", "Intel", "https://joblink")