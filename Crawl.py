import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import pandas as pd
from selenium.webdriver.common.by import By

#Declare browser
driver = webdriver.Chrome('chromedriver.exe')
driver.delete_all_cookies()
#Open url
driver.get("https://www.lazada.vn/trang-phuc-nam/?page=1&spm=a2o4n.home.cate_9.1.19053bdcOP3QS3")
sleep(random.randint(10,20))

#Get Link/title
elems = driver.find_element(By.CSS_SELECTOR , "RfADt [href]")
title = [elem.text for elem in elems]
links = [elem.get_attribute('href') for elem in elems]

#Get Price
elems_price = driver.find_elements(By.CSS.SELECTOR , "aBrP0")
price = [elem_price.text for elem_price in elems_price]

df1 = pd.DataFrame(list(zip(title, price, links)), columns = ['title', 'price', 'link_item'])
df1['index_'] = np.arange(1, len(df1) + 1)

#Get Discount
elems_discount = driver.find_elements(By.CSS_SELECTOR , "WNoq3")
discount_all = [elem.text for elem in elems_discount]
#elems_discount = driver.find_elements(By.CSS_SELECTOR , "WNoq3 ._1m41m")
#discount = [elem.text for elem in elems_discount]

#elems_discountPercent = driver.find_elements(By.CSS_SELECTOR , "WNoq3 .IcOsH")
#discountPercent = [elem.text for elem in elems_discountPercent]

#elems_discountText = driver.find_elements(By.CSS_SELECTOR , "WNoq3 .ic-dynamic-badge ic-dynamic-badge-text ic-dynamic-badge-fc ic-dynamic-group-2")
#discountText = [elem.text for elem in elems_discountText]


df2 = pd.DataFrame(list(zip(discount_all)), columns=['discount_all'])
df2['discount_idx'] = np.arange(1, len(df2) +1)

df1.head()