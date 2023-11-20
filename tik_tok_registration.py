from browser.chrome import chrome_setup
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from password_generator import PasswordGenerator
from pyshadow.main import Shadow
from db import DB
import time
import random
import re

def find_number(string):
    pattern = r'\b\d{6}\b'
    result = re.search(pattern, string)
    if result:
        return result.group()
    else:
        return None

def createBro():
    import requests
    url = "http://local.adspower.net:50325/api/v1/user/create"

    payload = {
        "name": "test",
        "group_id": "0",
        "repeat_config": [
            "0"
        ],
        "fingerprint_config": {
            "flash": "block",
            "scan_port_type": "1",
            "screen_resolution": "1024_768",
            "fonts": [
                "all"
            ],
            "longitude": "180",
            "latitude": "90",
            "webrtc": "proxy",
            "do_not_track": "true",
            "hardware_concurrency": "default",
            "device_memory": "default"
        }
        ,
        "user_proxy_config": {
            "proxy_soft": "other",
            "proxy_type": "socks5",
            "proxy_host": "78f609233452dcb5.eu.roxlabs.vip",
            "proxy_port": "4600",
            "proxy_user": "user-lxy654321-region-gb-sessid-gbkKdFpcTc-sesstime-1-keep-true",
            "proxy_password": "111222"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    text = response.json()
    print(text)
    ads_id = text['data']['id']
    return ads_id

def TikTokRegister(country):
    ads_id = 'jbm9yde'
    driver = chrome_setup(ads_id)  # Setting up the ChromeDriver
    # browserId = createBrowser()
    shadow = Shadow(driver)  # Declaring the shadow module
    # Declaring the mouse and keyboard actions module
    act = ActionChains(driver)
    # db = DB()

    ### Generated Values ###

    generate_p = PasswordGenerator()
    generate_p.minuchars = 1
    generate_p.minschars = 1
    generate_p.minnumbers = 1
    generate_p.minlen = 12
    generate_p.maxlen = 12
    password = generate_p.generate()
    # user = db.getDataTikTok(offset)
    user_email = 'pcmtdfuwpkrtny@outlook.jp'
    user_pass = 'LSlk65538'

    #########################

    driver.get('https://www.google.com/')
    time.sleep(5)
    driver.get('https://www.tiktok.com/signup')
    print('The Tik-Tok page reached!')
    driver.implicitly_wait(3)

    driver.find_element(
        By.XPATH, '//*[@id="loginContainer"]/div/div/div[2]/div[1]').click()
    time.sleep(5)

    # Accept cookies shadowDOM function
    try:
        driver.implicitly_wait(200)
        shadow_root = driver.find_element(By.XPATH, '//tiktok-cookie-banner')
        button = shadow.find_element(
            shadow_root, 'div > div.button-wrapper > button:nth-child(2)')
        act.move_to_element(button).click(button).perform()
        print('Cookies dismissed!')
        time.sleep(3)
    except Exception as E:
        print(f'Cookies issue:{E}')

    act.move_to_element(driver.find_element(
        By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[1]/div[1]')).click().perform()
    time.sleep(1)
    months = driver.find_elements(
        By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[1]/div[2]/div')
    act.move_to_element(random.choice(months)).click().perform()

    act.move_to_element(driver.find_element(
        By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[2]/div[1]')).click().perform()
    time.sleep(1)
    days = driver.find_elements(
        By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[2]/div[2]/div')
    act.move_to_element(random.choice(days)).click().perform()
    act.move_to_element(driver.find_element(
        By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[3]/div[1]')).click().perform()

    time.sleep(1)
    years = driver.find_elements(
        By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[3]/div[2]/div')
    legit_years = years[20:38]
    act.move_to_element(random.choice(legit_years)).click().perform()

    driver.find_element(
        By.XPATH, '//a[@href="/signup/phone-or-email/email"]').click()

    driver.find_element(By.NAME, 'email').send_keys(user_email)
    driver.find_element(
        By.XPATH, '//input[@type="password"]').send_keys(password)
    print(f'Password used: {password}')
    # time.sleep(2)
    for _ in range(3):
        act.move_to_element(driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div[7]/div/button')).click().perform()

    # Outlook part
    driver.switch_to.new_window()
    driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1675518517&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d685ce745-a6c9-5d55-473e-8669c000a13d&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
    print('The Outlook page reached!')
    time.sleep(1)
    driver.implicitly_wait(10)
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@type="email"]').click()
    driver.find_element(By.XPATH, '//*[@type="email"]').clear()
    driver.find_element(
        By.XPATH, '//*[@type="email"]').send_keys(user_email)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

    time.sleep(3)
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element(
        By.XPATH, "//*[@type='password']").clear()
    driver.find_element(
        By.XPATH, "//*[@type='password']").send_keys(user_pass)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
    time.sleep(3)
    # Waiting to see if it is successful
    try:
        driver.find_element(By.CSS_SELECTOR, '#idBtn_Back').click()
    except:
        pass

    try:
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="iShowSkip"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="iNext"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '*[@id="downloadAppCancel"]').click()
        driver.find_element(By.XPATH, '//*[@id="iCancel"]')
    except:
        pass

    try:
        driver.find_element(By.XPATH, '//*[@id="iCancel"]').click()
    except:
        pass

    try:
        driver.find_element(By.CSS_SELECTOR, '#idBtn_Back').click()
    except:
        pass

    try:
        driver.find_element(By.XPATH, '//*[@id="iCancel"]').click()
    except:
        pass

    try:
        driver.find_element(
            By.XPATH, '//*[@id="ModalFocusTrapZone225"]/div[2]/div/div[2]/div[2]/div/span/div/button[3]').click()
    except:
        pass
    time.sleep(4)

    driver.find_element(
        By.XPATH, '//*[@id="Pivot11-Tab1"]/span/div').click()

    mail = driver.find_elements(
        By.XPATH, '//div[@class="hcptT"]')
    code = find_number(mail[0].get_attribute('aria-label'))

    tik_tok = driver.window_handles[0]
    driver.switch_to.window(tik_tok)

    print('Returned to Tik-Tok page!')

    print(f'The essentials:\n username:{user_email} \n password:{password}')

    time.sleep(3)
    driver.find_element(
        By.XPATH, "//input[@placeholder='Enter 6-digit code']").send_keys(code)

    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@id="loginContainer"]/div[1]/form/button').click()

    time.sleep(5)
    try:
        driver.find_element(By.XPATH,
                            '//*[@id="loginContainer"]/div[1]/form/button').click()
    except:
        pass


    userData = [user_email, password]

    # db.insertDataTikTok(userData)
    print(
        f'Query executed with email:{user_email} \n password:{password} \n country:')

    time.sleep(120)
    driver.quit()



TikTokRegister('Albania')
###