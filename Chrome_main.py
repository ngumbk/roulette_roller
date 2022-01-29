from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import timer


# returns array of float amounts of bets by colors: [blue, yellow, green]
def getbet():
    blue = driver.find_element(By.XPATH,
                               "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span[2]/span[2]/span").get_attribute(
        'innerHTML')
    yellow = driver.find_element(By.XPATH,
                                 "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[2]/span[2]/span[2]/span").get_attribute(
        'innerHTML')
    green = driver.find_element(By.XPATH,
                                "//*[@id='root']/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[1]/div[2]/span[2]/span[2]/span").get_attribute(
        'innerHTML')
    print("Amount of bet: Blue:", blue,
          " | Yellow: " + yellow, " | Green: ", green)
    arrayBets = [float(blue), float(yellow), float(green)]
    return arrayBets


# returns str color of winLot
def getwin():
    win = driver.find_element(By.XPATH,
                              "//*[@id='root']/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/ul/li[1]/span").get_attribute(
        'class')
    print("Win is", win[21:len(win)])
    return  win[21:len(win)]


# returns str name of color that should win
def prediction(_arrayOfBets):
    _arrayOfBets[0] *= 2
    _arrayOfBets[1] *= 14
    _arrayOfBets[2] *= 2

    if min(_arrayOfBets) == _arrayOfBets[0]:
        print("blue")
        return "blue"
    elif min(_arrayOfBets) == _arrayOfBets[2]:
        print("green")
        return "green"
    else:
        print("yellow")
        return "yellow"


driver = webdriver.Chrome(executable_path="D:\\Projects\\roulette_roller\\chromedriver\\chromedriver.exe")

try:
    driver.get("https://csgorun.gg/double")
    # Подтверждаем совершеннолетие при входе
    driver.find_element(By.CLASS_NAME, "switcher__content").click()

    file = open("results.txt", 'a')

    counter = 0
    currentBalance = 0

    while 1:
        if timer.timerstopper(driver, "//*[@id='root']/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]"):
            arrayOfBets = getbet()
            time.sleep(10)
            predictionBet = prediction(arrayOfBets)
            winBet = getwin()
            counter += 1

            if predictionBet == winBet:
                if predictionBet == "yellow":
                    currentBalance += 3.25
                else:
                    currentBalance += 0.25
            else:
                currentBalance -= 0.25

            file.write(
                f"C:{counter}|B:{round(arrayOfBets[0],2)}|Y:{round(arrayOfBets[1], 2)}|G:{round(arrayOfBets[2])}"
                f"|P:{predictionBet}|W:{winBet}|BAL:{currentBalance};\n")

            print(
                f"C:{counter}|B:{round(arrayOfBets[0],2)}|Y:{round(arrayOfBets[1], 2)}|G:{round(arrayOfBets[2])}"
                f"|P:{predictionBet}|W:{winBet}|BAL:{currentBalance};")

except Exception as exception:
    print(exception)
finally:
    driver.close()
    driver.quit()
    file.close()
