from browser.chrome import chrome_setup
import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from pyshadow.main import Shadow
from random_email_name.randoms import EmailNameGenerator
from password_generator import PasswordGenerator
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from db import DB
import nopecha
import random
import time
import blobSolver
import pyautogui
import pandas as pd


def OutlookRegistration():
    driver = chrome_setup()
    act = ActionChains(driver)
    shadow = Shadow(driver)
    db = DB()

    driver.get('https://www.google.com/')
    time.sleep(5)

    ### Generators ###
    generate_e = EmailNameGenerator()
    str_list = generate_e.__repr__()

    generate_p = PasswordGenerator()
    password = generate_p.non_duplicate_password(12)

    generate_fn = str_list[0]
    generate_ln = str_list[1]
    email = str_list[2]

    # nopecha.api_key = 'sub_1MTWg4CRwBwvt6pt5ty8ueEY'
    nopecha.api_key = 'sub_1Mhta0CRwBwvt6ptbuhc5F1p'

    ###################

    # Setup - Get the form
    driver.get('https://outlook.live.com/owa/?nlp=1&signup=1')
    # driver.minimize_window()

    # First Step - Email Fill
    print('-- Email Part Reached --')
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'MemberName').send_keys(email)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

    # Second Step - Password Fill
    print('-- Password Part Reached --')
    driver.implicitly_wait(30)
    driver.find_element(
        By.XPATH, '//input[@type="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

    # Third Step - FirstName / LastName
    print('-- Names Part Reached --')
    driver.find_element(
        By.XPATH, '//input[@id="FirstName"]').send_keys(generate_fn)
    driver.find_element(
        By.XPATH, '//input[@id="LastName"]').send_keys(generate_ln)
    driver.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

    # Forth step - Country And Birth
    print('-- Country And Birth Step Reached --')
    driver.implicitly_wait(5)

    act.move_to_element(driver.find_element(
        By.XPATH, '//*[@id="Country"]')).click().perform()
    country = random.choice(driver.find_elements(
        By.XPATH, '//*[@id="Country"]/option'))
    country.click()
    country = country.text

    driver.implicitly_wait(5)
    complete = False
    while complete != True:
        driver.implicitly_wait(5)
        act.move_to_element(driver.find_element(
            By.XPATH, '//*[@id="BirthMonth"]')).click().perform()
        month = random.choice(driver.find_elements(
            By.XPATH, '//*[@id="BirthMonth"]/option'))
        month.click()

        driver.implicitly_wait(5)
        act.move_to_element(driver.find_element(
            By.XPATH, '//*[@id="BirthDay"]')).click().perform()
        day = random.choice(driver.find_elements(
            By.XPATH, '//*[@id="BirthDay"]/option'))
        day.click()

        if month.get_attribute('value') and day.get_attribute('value'):
            complete = True
            break
        else:
            continue

    driver.implicitly_wait(5)
    years = list(range(1990, 2003))
    year = str(random.choice(years))
    driver.find_element(
        By.XPATH, '//*[@id="BirthYear"]').send_keys(year)
    birthdate = day.text + "/" + month.text + "/" + year

    driver.find_element(By.XPATH, '//*[@id="iSignupAction"]').click()

    try:
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="HipPaneForm"]/div[2]')
    except:
        pass
    else:
        driver.quit()

    # funCAPTCHA Solving - Tricky Part
    time.sleep(1)
    try:
        driver.implicitly_wait(1000)
        print('-- CAPTCHA Step Reached --')
        print(
            f'Done with the profile with data : \n email: {email} \n password: {password} \n name:  \n country: {country}')
        time.sleep(5)
        driver.switch_to.frame('enforcementFrame')
        driver.switch_to.frame(0)
        driver.switch_to.frame('game-core-frame')
    except:
        driver.implicitly_wait(100)
        driver.switch_to.frame('enforcementFrame')
        driver.switch_to.frame(0)
        driver.switch_to.frame('fc-iframe-wrap')
        driver.switch_to.frame('CaptchaFrame')
    finally:
        print(
            f'Done with the profile with data : \n email: {email} \n password: {password} \n name:  \n country: {country}')
        time.sleep(100)
        button = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/button')
        button.click()
    task = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/h2').text
    # Call the Recognition API
    processing = True
    counter = 1

    while processing:
        try:
            print(f'-- Solving {counter} --')
            time.sleep(1)
            driver.implicitly_wait(10)
            task = driver.find_element(
                By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/h2').text
            driver.implicitly_wait(10)
            image_src = driver.find_element(
                By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div/button[1]').get_attribute('style')
            time.sleep(2)
            image_data = image_src.split('"')[1]
            image_data = blobSolver.getContent(driver, image_data)

            image_grid = driver.find_elements(
                By.XPATH, f'//*[@id="root"]/div/div[1]/div/div[2]/div/button')

            clicks = nopecha.Recognition.solve(
                type='funcaptcha',
                task=task,
                image_data=[image_data]
            )

            print(clicks)
            time.sleep(4)
            for i in range(0, 6):
                if clicks[i] == True:
                    driver.implicitly_wait(10)
                    image_grid[i].click()
                    time.sleep(1)
            counter += 1
        except NoSuchElementException as e:
            print(f'Error : {e}')
            break
        except WebDriverException as e:
            print(f'Error : {e}')
            break

    driver.implicitly_wait(100)
    # Waiting to see if it is successful
    driver.find_element(By.CSS_SELECTOR, '#idBtn_Back')

    full_name = generate_fn + " " + generate_ln
    MailData = [email, password, full_name, country, birthdate]

    print(' -- Executing MariaDB query -- ')

    db.insertDataOutlook(MailData=MailData)

    print(
        f'Done with the profile with data : \n email: {email} \n password: {password} \n name: {full_name} \n country: {country}')

    driver.quit()


#
OutlookRegistration()

