from db import DB
'''
第一步  使用创建浏览器 获取id 并且将一些代理配置存入数据库
第二步  返回代理id 打开指纹浏览器 然后获取邮箱 进行注册操作
'''
from browser.chrome import chrome_setup
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from password_generator import PasswordGenerator
from pyshadow.main import Shadow
from db import DB
import time
import random
import re

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
            "proxy_host": "78f609233452dcb5.as.roxlabs.vip",
            "proxy_port": "4600",
            "proxy_user": "user-lxy654321-region-my-sessid-mym2A77QXa-sesstime-1-keep-true",
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



def find_number(string):
    pattern = r'\b\d{6}\b'
    result = re.search(pattern, string)
    if result:
        return result.group()
    else:
        return None

from selenium.common.exceptions import NoSuchElementException, WebDriverException
def TikTokRegister(country,ads_id):
    driver = chrome_setup(ads_id)  # Setting up the ChromeDriver
    # browserId = createBrowser()
    shadow = Shadow(driver)  # Declaring the shadow module
    # Declaring the mouse and keyboard actions module
    act = ActionChains(driver)
    # db = DB()
    #########################

    driver.get('https://www.google.com/')
    time.sleep(3)
    driver.get('https://www.tiktok.com/signup')
    print('The Tik-Tok page reached!')
    driver.implicitly_wait(3)

    driver.find_element(
        By.XPATH, '//*[@id="loginContainer"]/div/div/div[2]/div[4]').click()
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

    # 获取所有窗口句柄
    tw = driver.window_handles[0]
    google_auth_login = driver.window_handles[1]

    driver.switch_to.window(google_auth_login)
    driver.implicitly_wait(10)
    username = '@EWZyxroT0f0xS2M'
    password = 'gF2QS0y0Ma5'
    enterAccount = True
    # 扫描页面 如果出现了账号密码输入框。。。。
    while enterAccount:
        try:
            print("identifierId")
            element = driver.find_element(By.ID, 'username_or_email')
            # 如果 'identifierId' 元素出现，运行登录操作 输入账号密码 。。。
            enterAccount = loginTiktokByGoogle(username, password, driver,enterAccount)
            print("出来了。。。")
            if enterAccount == False:
                print("11111")
                driver.implicitly_wait(10)
                element = driver.find_element(By.XPATH,
                                              '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]')
                element.click()
                driver.window_handles
                enterAccount = True
                # 如果 'element' 元素出现，进行点击登录操作

        except NoSuchElementException:
            # 如果 'identifierId' 元素不存在，不执行登录操作
            pass

    # # 出现异常
    # max_attempts = 10  # 最大尝试次数
    # attempts = 0
    #
    # for _ in range(10):
    #     # 此处环境复杂 需要多种环境处理 第一种 已经登录终端
    #     print("再次登录 当前页面为"+driver.current_url)
    #     driver.implicitly_wait(20)
    #     # 再次账户登录
    #     driver.find_element(
    #         By.XPATH,
    #         '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]').click()
    #     time.sleep(5)
    #     driver.find_element(
    #         By.XPATH, '//*[@id="loginContainer"]/div/div/div[2]/div[3]').click()
    #     driver.switch_to.window(tik_tok)
    # if attempts >= max_attempts:
    #     print('Reached maximum attempts, returning a failure')
    time.sleep(120)
    driver.quit()

def loginTiktokByGoogle(usename,password,driver,enterAccount):
    try:
        print("进入了输入账户页面")
        driver.implicitly_wait(10)
        # 输入账号密码
        print("进入了输入账号")
        driver.find_element(By.ID,'username_or_email').send_keys(usename)
        driver.implicitly_wait(3)
        print("进入了输入密码")
        driver.find_element(By.ID,'password').send_keys(password)
        driver.find_element(By.ID, 'remember').click()
        driver.find_element(By.ID, 'allow').click()
        print("再次登录 当前页面为" + driver.window_handles)
        return enterAccount
    except:
        pass

ads_id = createBro()
# ads_id = 'jbfhlwe'
TikTokRegister('cccc',ads_id)
###