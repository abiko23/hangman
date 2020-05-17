from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Seleniumをあらゆる環境で起動させるChromeオプション
#EX_PATH = 'Users/abiko/Library/Application Support/Google/Chrome/Default/Extension'
options = Options()
options.add_argument('--disable-gpu')
#options.add_argument('--disable-extensions') #拡張機能無効化
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
options.add_argument('--user-data-dir=/Users/abiko/Library/Application Support/Google/Chrome/')
options.add_argument('--profile-directory=Profile 1') 
#options.add_extension('Users/abiko/Library/Application Support/Google/Chrome/Default/Extension')
#options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す

DRIVER_PATH = '/Users/abiko/D/python_lesson/chromedriver2'
# DRIVER_PATH = '/Users/Kenta/Desktop/Selenium/chromedriver' # ローカル
# DRIVER_PATH = '/app/.chromedriver/bin/chromedriver'        # heroku

# ブラウザの起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

# Webページにアクセスする
#url = 'https://happymail.co.jp/sp/app/html/profile_list.php'
url = 'https://happymail.co.jp/sp/app/html/profile_detail_list.php?a=a&from=prof&idx=1'
# 末尾の1を2,3,4,,としていけば、ユーザの遷移はできそう
# ユーザプロフィール直飛びはできなさそう
driver.get(url)
driver.implicitly_wait(3) # 秒

# 要素をクリックする
     
#selector = 'ds_profile_list_top'
#link_elem = driver.find_element_by_css_selector(selector)
#link = "profile_list.php"
#link_elem = driver.find_element_by_link_text(link)
#type(link_elem)
#link_elem.click()
#print(link_elem.location)

# いいねクリック
driver.implicitly_wait(10)
good = 'btn-like'
#good_elem = driver.find_element_by_css_selector(good)
good_elem = driver.find_element_by_id(good)
type(good_elem)
good_elem.click()
