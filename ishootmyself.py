from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
from time import sleep

#Note: only insert username,password and message in between qoutation marks like this "here" don't alter any other thing if you do anything wrog please contact me.

your_username = ""  # here go your username go
your_passward = ""#passwordc

your_message = " hallo, als je op zoek bent naar seks, neem dan contact met mij op:to.ly/1tqWI"#here go your message this 

try:
    proxy = "47.74.9.208"
    port = 3128
 
    fp = webdriver.FirefoxProfile()
    fp.set_preference('network.proxy.ssl_port', int(port))
    fp.set_preference('network.proxy.ssl', proxy)
    fp.set_preference('network.proxy.http_port', int(port))
    fp.set_preference('network.proxy.http', proxy)
    fp.set_preference('network.proxy.type', 1)
 
    browser = webdriver.Firefox(firefox_profile=fp)
    browser.set_page_load_timeout(30)
    browser.get('http://www.ishotmyself.nl/online-members.php')
    sleep(5)
    
except:
    pass
browser.find_element_by_css_selector("#lgnbtn").click()
sleep(1)
profile = browser.find_element_by_name("u")
password = browser.find_element_by_name("p")
profile.send_keys(your_username)
password.send_keys(your_passward)
browser.find_element_by_name("rememberme").click()
browser.find_element_by_css_selector("a.btn:nth-child(3)").click()
sleep(2)
browser.get('http://www.ishotmyself.nl/online-members.php')
urls = []
for i in range(50):
    try:
        for i in range(135):
        
            a=i+1

            bd = "/html/body/div[2]/div/div[2]/ul/li[(%s)]"%(a)

            user = browser.find_element_by_xpath(bd)
            a = user.find_element_by_tag_name("a").get_attribute("href")
    
            print a
            urls.append(a)
        browser.find_element_by_css_selector(".pagination>a:nth-child(6)").click()
        sleep(5)#because my browser take time to load so i need bot to sleep for some second for findingo ok can you do on my computer as is late here :D
    except:
        break    
print len(urls)
a = len(urls)
for i in range(1,a):
    
    #list1 = urls[]
    browser.get(urls[i])
    sleep(5)
    try:
        browser.find_element_by_css_selector(".msg").click()
        sleep(2)
    except:
        pass   
    try:
        browser.find_element_by_name("newreply").send_keys(your_message)
        browser.find_element_by_css_selector('a.btn:nth-child(5)').click()
    except:
        pass
    #messgae
    
    
    #except:
        #pass
    
    
    #browser.find_element_by_css_selector('#newreply').click()









































































"""
sleep(6)


browser.find_element_by_css_selector("#lgnbtn").click()
sleep(5)
profile = browser.find_element_by_name("u")
password = browser.find_element_by_name("p")
profile.send_keys(your_username)
password.send_keys(your_passward)
browser.find_element_by_name("rememberme").click()
browser.find_element_by_css_selector("a.btn:nth-child(3)").click()
browser.get('http://www.ishotmyself.nl/online-members.php')


urls = []
for i in range(4):
    
    #element = WebDriverWait(browser, 20).until(
        #EC.presence_of_element_located((By.CSS_SELECTOR, "div.btn--ico")))

    #contaner = browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]")

    user = browser.find_element_by_css_selector("div.container:nth-child(2)")
    user_cells = user.find_elements_by_class_name("users usersearchres")
    for user_cell in user_cells:
        
        a = user_cell.find_element_by_tag_name("a").get_attribute("href")
        print i, a
        urls.append(a)

            
    ###browser.find_element_by_css_selector("div.pagination__nav:nth-child(10)").click()
    sleep(3)  # please adjust it
"""


"""
for user_cell in user:

        a = user_cell.find_element_by_tag_name("a").get_attribute("href")
        print  a
        urls.append(a)"""







