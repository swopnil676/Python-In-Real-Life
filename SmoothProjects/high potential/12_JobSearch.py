# Auto Job Search

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/python-developer-jobs")

time.sleep(5)

jobs = []

job_cards = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")

print("Jobs found:", len(job_cards))

for job in job_cards:
    try:
        title = job.find_element(By.CLASS_NAME, "title").text
        company = job.find_element(By.CLASS_NAME, "comp-name").text
        
        # Apply Link (IMPORTANT)
        apply_link = job.find_element(By.CLASS_NAME, "title").get_attribute("href")
        
        jobs.append({
            "title": title,
            "company": company,
            "apply_link": apply_link
        })
    except Exception as e:
        print("Error:", e)
        continue

# Save to CSV
df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False)

print("✅ CSV created")

driver.quit()