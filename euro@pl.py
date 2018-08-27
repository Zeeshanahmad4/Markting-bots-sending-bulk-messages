from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.proxy import *


your_username = ""  # here go your email
your_passward = ""

your_message = " dfsf"
#browser = webdriver.Firefox()
#browser.set_page_load_timeout(50)

proxy = "47.74.9.208"
port = 3128

fp = webdriver.FirefoxProfile()
fp.set_preference('network.proxy.ssl_port', int(port))
fp.set_preference('network.proxy.ssl', proxy)
fp.set_preference('network.proxy.http_port', int(port))
fp.set_preference('network.proxy.http', proxy)
fp.set_preference('network.proxy.type', 1)

browser = webdriver.Firefox(firefox_profile=fp)
browser.set_page_load_timeout(50)
browser.get('https://www.erodate.pl/')
sleep(5)



"""
url = 'https://www.erodate.pl/'
browser.get(url)
sleep(3)"""


profile = browser.find_element_by_name("_username").send_keys(your_username)
password = browser.find_element_by_name("_password").send_keys(your_passward)
browser.find_element_by_name("login").click()
sleep(5)

browser.find_element_by_css_selector('#content>div.homepage-left>div.wob_profile_filter.module-box>div.module-box--footer.bigger').click()
for i in range(4):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
urls = []


for i in range(30):
    a = i+1

    bd = "/html/body/div[2]/div[4]/div[2]/div[7]/div[(%s)]" % (a)

    user = browser.find_element_by_xpath(bd)
    a = user.find_element_by_tag_name("a").get_attribute("href")

    print a
    urls.append(a)
    
len1 = len(urls)
print len1

for i in range(1,len1):
    
    
    browser.get(urls[i])
    sleep(5)
    browser.find_element_by_css_selector(".send-message").click()
    sleep(5)
    browser.find_element_by_css_selector(".form-control").send_keys(your_message)
    sleep(2)
    browser.find_element_by_css_selector(".btn-send").click()


