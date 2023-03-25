from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# loading all phones

s = Service('C:/Users/dhrum/Desktop/chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=s, options=options)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(2)

# exclude out of stock
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)
#exculde upcoming
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)

old_height=driver.execute_script('return document.body.scrollHeight')

#load more
counter=1
while True:


    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')
    print(counter, old_height, new_height)

    if new_height==old_height:
        break

    old_height=new_height
    counter+=1

html=driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)



