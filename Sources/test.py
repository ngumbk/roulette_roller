from selenium import webdriver
from selenium.webdriver.common.by import By
import timer
import time

driver = webdriver.Chrome(executable_path="D:\\Projects\\roulette_roller\\chromedriver\\chromedriver.exe")

try:
    driver.get("https://csgorun.gg/double")
    # Подтверждаем совершеннолетие при входе
    driver.find_element(By.CLASS_NAME, "switcher__content").click()

    while 1:
        if timer.timerstopper(driver, "//*[@id='root']/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]"):
            print("Successful!")
            time.sleep(1)
        else:
            print("Not successful(")

except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
