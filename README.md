
This repository contains a Python script that automates a series of actions on the `http://atg.party` website using Selenium. The script performs the following tasks:
- Opens the website
- Logs the page title and response time
- Logs in with a specified user account
- Posts an article with a title, description, and cover image
- Logs the URL of the posted article



## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.10
- Google Chrome
- ChromeDriver compatible with your version of Chrome
- The following Python packages:
  - selenium (version 4.11.2)
  - requests
  - pyautogui
  - wedriver-manager (4.0.0)

You can install the necessary packages using pip:

```bash
pip install selenium requests pyautogui webdriver-manager 
