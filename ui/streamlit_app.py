import streamlit as st
import sys
import os

# Add app folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from scraper import scrape_jobs
from apply_bot import apply_to_jobs
from notify import send_notification
from pushbullet_notify import send_push
from google_sheets_logger_FIXED import log_to_sheets

st.set_page_config(page_title="Auto Job Apply Bot", layout="centered")
st.title("🤖 Auto Job Apply System")
st.write("Scrape, apply, and log job applications automatically.")

st.header("🔍 Scrape Jobs")
if st.button("Start Scraping"):
    scrape_jobs()
    st.success("✅ Job scraping completed.")

st.header("✉️ Apply to Jobs")
if st.button("Apply Now"):
    apply_to_jobs()
    st.success("✅ Job applications submitted.")

st.header("📬 Notifications")
job_link = st.text_input("Sample Job Link", "https://sample-job-link.com")
col1, col2 = st.columns(2)
with col1:
    if st.button("Send Email Notification"):
        send_notification(job_link)
        st.success("📧 Email sent!")

with col2:
    if st.button("Send Pushbullet Notification"):
        send_push("Applied to job: " + job_link)
        st.success("📲 Pushbullet alert sent!")

st.header("📝 Log to Google Sheet")
title = st.text_input("Job Title", "DFT Intern")
company = st.text_input("Company", "Intel")
if st.button("Log Job to Google Sheet"):
    log_to_sheets(title, company, job_link)
    st.success("✅ Logged to Google Sheet.")
