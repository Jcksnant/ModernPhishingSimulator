# ModernPhishingSimulator

This project is meant to be a phishing experiment designed for strictly academic use.

It features:
A phishing campaign simulation ran with gophish
A spoofed login landing page
A database to store any captured credentials
An admin dashboard so the attacker can view any stolen credentials they obtained
Also runs with Kali-Linux

The main technologies that were used are:
Gophish for their phishing campaign management system
Flask to create a fake login page and to capture credentials after their submitted into the form
MailHog as the main testing mail server
SQLite to help with credential storage
Kali Linux as the main enviornment the project will be tested on
Windows as the main operating system this project is hosted with

To activate this code you must start the python enviornment with these commands:
python -m venv venv
venv/Scripts/activate

pip install -r requirements.txt 

Then finally to start the app with python app.py
Vist the URLS the application provides to start the entire phishing process
