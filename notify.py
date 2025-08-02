import smtplib
from email.message import EmailMessage

def send_notification(job_link):
    msg = EmailMessage()
    msg.set_content(f"Applied to a job! Link: {job_link}")
    msg["Subject"] = "Job Application Confirmation"
    msg["From"] = "saiv26783@gmail.com"
    msg["To"] = "saiv26783@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("saiv26783@gmail.com", "kbhb yirk ibqh dram")  # Use App Password
        smtp.send_message(msg)
        print("Notification sent!")

if __name__ == "__main__":
    send_notification("https://sample-job-link.com")