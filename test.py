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
        try:
            timer = driver.find_element(By.XPATH,
                                    "//*[@id='root']/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]").get_attribute(
                                            'innerHTML')
            timer = float(timer)
            if type(timer) == float:
                if timer < 0.25:
                    print(timer)
                    continue
                else:
                    time.sleep(timer - 0.5)
            else:
                print(type(timer))

        except Exception as excp:
            print(excp)

except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
