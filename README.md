# ModernPhishingSimulator

This project is meant to be a phishing experiment designed for strictly academic use. It demonstrates how phishing attacks are delivered, executed and analyzed. It captures and analyzes phishing campaign metrics as well as applies the core cybersecurity concepts such as the CIA Triad, AAA model, and Defense-in-Depth. It shows the email delivery, link interactions, credential submissions, and forensic tracking.

It features:
A phishing campaign simulation ran with gophish
A spoofed login landing page
A database to store any captured credentials
An admin dashboard so the attacker can view any stolen credentials they obtained
Also runs with Kali-Linux

This system uses a multi-service architecture with three main components:

- GoPhish – Manages phishing campaigns, emails, landing pages, and analytics
- MailHog – Acts as a fake SMTP server that captures all phishing emails safely
- Flask Web App – Serves as the phishing landing page and credential capture system


The main technologies that were used are:
Gophish for their phishing campaign management system
Flask to create a fake login page and to capture credentials after their submitted into the form
MailHog as the main testing mail server
SQLite to help with credential storage
Kali Linux as the main enviornment the project will be tested on
Windows as the main operating system this project is hosted with

## Testing & Validation

End-to-end testing validates the full phishing attack workflow:

- Email delivery confirmed in MailHog
- Victim link redirection tested
- Credential submission validated on the Flask page
- Campaign tracking verified in GoPhish

Observed statuses:
- Email Sent
- Email Opened
- Link Clicked
- Submitted Data

Captured credentials, timestamps, and IP addresses are used to validate forensic accuracy.

To activate this code you must start the python enviornment with these commands:
python -m venv venv
venv/Scripts/activate

pip install -r requirements.txt 

Then finally to start the app with python app.py
Vist the URLS the application provides to start the entire phishing process

Dashboards:
GoPhish Admin: http://127.0.0.1:3333
MailHog: http://172.21.6.15
Flask Landing Page: http://172.21.6.15:5000

## User Manual (Quick Start)

### 1. Start All Services
```bash
./start_lab.sh
