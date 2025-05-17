import imaplib
import email
from email.header import decode_header
from selenium import webdriver
import time
import os


# Email credentials
EMAIL_USER = "your email_id"
EMAIL_PASS = "email_pass"
IMAP_SERVER = "imap.gmail.com"  # Change for other providers

# Connect to IMAP and fetch latest email
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("your email_id ", " email_pass")
mail.select("inbox")

# Fetch the latest email
status, messages = mail.search(None, "ALL")
latest_email_id = messages[0].split()[-1]
status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

# Parse email
raw_email = msg_data[0][1]
msg = email.message_from_bytes(raw_email)

# Extract email subject
subject, encoding = decode_header(msg["Subject"])[0]
if isinstance(subject, bytes):
    subject = subject.decode(encoding or "utf-8")

if "App password created" in subject:
    print("Skipping security alert email.")
    exit()    

# Extract email body (HTML version preferred)
email_body = ""
for part in msg.walk():
    if part.get_content_type() == "text/html":
        email_body = part.get_payload(decode=True).decode()
        break

# Save email as HTML file
with open("email.html", "w", encoding="utf-8") as f:
    f.write(email_body)
    if not email_body:
     print(" No HTML body found in the email!")
     exit()


# Configure Selenium with a headless browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1200x800")
options.add_argument("--enable-logging")

# Open HTML in Selenium and take a screenshot
driver = webdriver.Chrome(options=options)
file_path = os.path.abspath("email.html")
driver.get("file://" + file_path)
time.sleep(2)  # Wait for rendering

# Save screenshot
screenshot_path = "email_screenshot.png"
driver.save_screenshot(screenshot_path)
driver.quit()

print(f"Screenshot saved as {screenshot_path}")
