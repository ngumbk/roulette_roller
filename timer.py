from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#"//*[@id='root']/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]"


def timerstopper(driver, path):
    try:
        _timer = 0.000
        flag = False
        while not flag:
            try:
                _timer = driver.find_element(By.XPATH, path).get_attribute('innerHTML')
                _timer = float(_timer)

                if type(_timer) == float:
                    if _timer < 0.05:   #тут меняем значени, чтобы установить минимальный предел времени
                        print(_timer)
                        #Когда достигаем необходимого минимума таймера поднимаем флаг
                        flag = True
                        return True
                    else:
                        time.sleep(_timer - 0.5)
                else:
                    print(type(_timer))

            except Exception as excp:
                print(excp)

    except Exception as exception:
        print(exception)
