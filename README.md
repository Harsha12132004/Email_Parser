# Email_Parser

This project is a Python-based automation tool that securely connects to a Gmail inbox using the IMAP protocol, fetches the most recent email from a specific sender, extracts the HTML content of the email, and uses Selenium with a headless Chrome browser to render and capture a screenshot of the email as it would appear in a web browser. The screenshot is saved locally as a PNG image for further use, such as archiving, monitoring, or automation workflows.

To use this script, users must provide their Gmail email ID and password directly in the script. However, for security reasons, the Gmail account used must have 2-Step Verification enabled, and users must generate and use an App Password instead of their regular Gmail password. This is required because Gmail blocks access from apps that do not meet its security standards unless 2FA and App Passwords are properly configured.

To enable 2-Step Verification, visit https://myaccount.google.com/security-checkup. Once enabled, generate an App Password by going to https://myaccount.google.com/apppasswords. type  “Mail” and click on "creat",  Google will provide a 16-character password, which should be pasted into the script in place of your actual Gmail password.

After entering your Gmail address and generated App Password into the script, simply run the script to connect to your inbox, extract and render the latest matching email, and save it as a screenshot named email_screenshot.png.
