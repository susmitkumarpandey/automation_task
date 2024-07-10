from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import requests
import time
import pyautogui
from dotenv import load_dotenv
import os


load_dotenv()
mail_id = os.getenv("email")
Password = os.getenv("pass")

driver = webdriver.Chrome()
try:
    driver.get("http://atg.party")
    time.sleep(3)
    current_url = driver.current_url
    response = requests.get(current_url)
    http_code = response.status_code

    if http_code == 200:
        print(driver.title)
        with open('file.text', 'a') as file:
            file.write(driver.title+'\n')
        navigationStart = driver.execute_script(
            "return window.performance.timing.navigationStart")
        responseStart = driver.execute_script(
            "return window.performance.timing.responseStart")
        response_time = responseStart-navigationStart
        print(f"{response_time} ms")
        with open('file.text', 'a') as file:
            file.write(f"{response_time} ms\n")

        try:
            login_button = driver.find_element(
                By.XPATH, "/html/body/nav/div/div/div/div[2]/div/button[2]")
            login_button.click()
            driver.implicitly_wait(2)
            email = driver.find_element(By.XPATH, '//*[@id="email_landing"]')
            time.sleep(1)
            email.send_keys(mail_id)
            password = driver.find_element(
                By.XPATH, '//*[@id="password_landing"]')
            password.send_keys(Password)
            sign_in = driver.find_element(
                By.XPATH, '//*[@id="frm_landing_page_user_login"]/div[3]/button')
            sign_in.click()
            time.sleep(3)

            driver.get("http://atg.party/article")
            driver.maximize_window()
            blog_title = driver.find_element(By.XPATH, '//*[@id="title"]')
            blog_title.send_keys("Sunset")
            para = driver.find_element(
                By.XPATH, '//*[@id="description"]/div/div[1]/div/div/div')
            para.send_keys("Sunset (or sundown) is the disappearance of the Sun below the horizon "
                           "of the Earth (or any other astronomical object in the Solar System) due to its rotation.")
            time.sleep(2)
            image = driver.find_element(
                By.XPATH, '//*[@id="add-cover-image"]').click()
            time.sleep(1)
            pyautogui.write(
                'C:\\Users\\91620\\OneDrive\\Desktop\\task1\\download.jpg')
            pyautogui.press('enter')
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="hpost_btn"]').click()
            time.sleep(7)
            current_url = driver.current_url
            print(current_url)
            with open('file.text', 'a') as file:
                file.write(current_url+'\n')

        except NoSuchElementException as f:
            print(f)

except WebDriverException as e:
    print(e)
finally:
    driver.close()
