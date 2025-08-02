from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

def load_applied_links():
    try:
        with open("log.csv", "r") as f:
            return [row[2] for row in csv.reader(f)]
    except:
        return []

def apply_to_jobs():
    driver = webdriver.Chrome()
    applied_links = load_applied_links()

    for link in applied_links:
        driver.get(link)
        time.sleep(2)

        try:
            driver.find_element(By.ID, "applyButton").click()
            time.sleep(2)
            driver.find_element(By.ID, "file-upload").send_keys("resume.pdf")
            driver.find_element(By.NAME, "name").send_keys("Sai Vardhan")
            driver.find_element(By.NAME, "email").send_keys("your_email@gmail.com")
            driver.find_element(By.NAME, "phone").send_keys("1234567890")
            driver.find_element(By.ID, "submit").click()
        except Exception as e:
            print(f"Skipping {link}: {e}")

    driver.quit()

if __name__ == "__main__":
    apply_to_jobs()