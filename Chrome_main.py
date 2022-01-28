from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import timer


def getbet():
    blueBet = driver.find_element(By.XPATH,
                                  "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span[2]/span[2]/span").get_attribute('innerHTML')
    yellowBet = driver.find_element(By.XPATH,
                                    "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/span[2]/span[2]/span").get_attribute('innerHTML')
    greenBet = driver.find_element(By.XPATH,
                                 "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[1]/div[2]/span[2]/span[2]/span").get_attribute('innerHTML')
    print("Amount of bet: Blue:", blueBet,
          " | Yellow: " + yellowBet, " | Green: ", greenBet)

def getwin():
    win = driver.find_element(By.XPATH,
                              "//*[@id='root']/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/ul/li[1]/span").get_attribute('class')
    print("Win is", win[21:len(win)])

def prediction(blue, yellow, green):
    _blue = blue*2
    _green = green*2
    _yellow = yellow*2


driver = webdriver.Chrome(executable_path="D:\\Projects\\roulette_roller\\chromedriver\\chromedriver.exe")

try:
    driver.get("https://csgorun.gg/double")
    # Подтверждаем совершеннолетие при входе
    driver.find_element(By.CLASS_NAME, "switcher__content").click()

    file = open("results.txt")

    while 1:
        if timer.timerstopper(driver, "//*[@id='root']/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]"):
            getbet()
            time.sleep(10)
            getwin()



except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
