import time
from array import *

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Prime = [
    'black_bos@mail.ru',
    'gold45@mail.ru',
    'mavaleri@mail.ru',
    'johnson375916@gmail.com',
    'gunnpeter333@gmail.com',
    'warrenttt5@gmail.com',
    'mahfoodrobert5@gmail.com',
    'jonesbr74583755@gmail.com',
    'singhdennis55@gmail.com',
    'didgarett1@gmail.com',
    'shakil11qqq@gmail.com',
    'zaribovaolga@gmail.com',
    'pierzxc3222@gmail.com',
    'gold60817@gmail.com',
    'gold60815@gmail.com',
    'anthonyprogrammist@gmail.com',
    'pedropadcal@gmail.com',
    'cryptoxetr@gmail.com',
    'sanya85zzz@gmail.com',
    'donpieeer@gmail.com',
    'shakil11qqq@gmail.com'
]


driver = webdriver.Chrome()
driver.get("https://www.kresko.fi/")
options = webdriver.ChromeOptions()
time.sleep(2)
# assert "E-VISA" in driver.title

username = driver.find_element(By.XPATH, '//*[@id="usernameD"]')
username.click()
username.send_keys("xetr")

passw = driver.find_element(By.XPATH, '//*[@id="passwordD"]')
passw.click()
passw.send_keys("Slayer233189!")
passw.send_keys(Keys.ENTER)
time.sleep(5)
