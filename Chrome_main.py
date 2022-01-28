from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\\Projects\\roulette_roller\\chromedriver\\chromedriver.exe")

try:
    driver.get("https://csgorun.gg/double")
    # Подтверждаем совершеннолетие при входе
    driver.find_element(By.CLASS_NAME, "switcher__content").click()
    timer = 0.000

    while 1:
            # Получаем суммы ставок на каждый цвет
            blueBet = driver.find_element(By.XPATH,
                                          "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span[2]/span[2]/span")
            yellowBet = driver.find_element(By.XPATH,
                                            "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/span[2]/span[2]/span")
            redBet = driver.find_element(By.XPATH,
                                         "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[1]/div[2]/span[2]/span[2]/span")
            print(blueBet.get_attribute('innerHTML'),
                  yellowBet.get_attribute('innerHTML'), redBet.get_attribute('innerHTML'))

except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
