from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def clicker():
    for i in range(1,1000):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome()
        driver.get("https://www.turmush.kg/news:493715")
        input_username = driver.find_element(By.XPATH, '/html/body/div[2]/div/article/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[2]')

        print("Value is: %s" % i)
        input_username.click()
        
        time.sleep(5)
    
        driver.quit()


try:
    clicker()
except:
    clicker()