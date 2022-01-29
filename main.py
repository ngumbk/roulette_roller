from pydoc import cli
from numpy import double
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

balance = 1.28



def bet_wheel500(spins_count, timer):
    global balance
    counter_x2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[2]/main/div[2]/div[5]/div[3]/div[1]/div[1]/div[2]/div/span[1]")
    counter_x3 = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[2]/main/div[2]/div[5]/div[3]/div[2]/div[1]/div[2]/div/span[1]")
    counter_x5 = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[2]/main/div[2]/div[5]/div[3]/div[3]/div[1]/div[2]/div/span[1]")
    counter_x50 = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[2]/main/div[2]/div[5]/div[3]/div[4]/div[1]/div[2]/div/span[1]")
    estimated_prize = [double(counter_x2.text) * 2, double(counter_x3.text) * 3, double(counter_x5.text) * 5, double(counter_x50.text) * 50]
    print(f"Ставки:       {counter_x2.text} / {counter_x3.text} / {counter_x5.text} / {counter_x50.text}")
    print(f"Казик отдаст: {estimated_prize[0]} / {estimated_prize[1]} / {estimated_prize[2]} / {estimated_prize[3]}")
    min_estimated = min(estimated_prize)
    file1 = open('strategy_result_1_bet.txt', 'a')
    file1.write(f"C:{spins_count}|G:{round(double(counter_x2.text), 2)}|R:{round(double(counter_x3.text), 2)}|B:{round(double(counter_x5.text), 2)}|Y:{round(double(counter_x50.text), 2)}|")
    print(f"Таймер в конце ставки: {timer.text}")

    #делаем ставку
    if estimated_prize[0] == min_estimated:
        expected = "black"
        file1.write("P:G|")
    elif estimated_prize[1] == min_estimated:
        expected = "red"
        file1.write("P:R|")
    elif estimated_prize[2] == min_estimated:
        expected = "blue"
        file1.write("P:B|")
    elif estimated_prize[3] == min_estimated:
        expected = "yellow"
        file1.write("P:Y|")
    
    
    balance -= 0.01
    round(balance)
    print(f"Баланс после вычета 0.01: {balance}")
    print(f"expected: {expected}")
    time.sleep(4)

    #проверяем ставку
    game_result = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[1]/div[100]")
    game_result = game_result.get_attribute("class")
    match game_result[24:len(game_result)]:
        case "black":
            file1.write("W:G|")
            if (expected == "black"):
                balance += 0.02
        case "red":
            file1.write("W:R|")
            if (expected == "red"):
                balance += 0.03
        case "blue":
            file1.write("W:B|")
            if (expected == "blue"):
                balance += 0.05
        case "yellow":
            file1.write("W:Y|")
            if (expected == "yellow"):
                balance += 0.50

    round(balance)
    file1.write(f"BAL:{balance}\n")
    print(f"Баланс после результата: {balance}")
    file1.close()

def wheel500():
    url = "https://500.casino/wheel"
    driver.get(url=url)
    spins_count = 1
    print("Теперь логинься и жми на глаз, у тебя 60 сек")
    time.sleep(60) #time to login
    print("Ok, let's go!")

    while(True):
        try:
            timer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "fortune-wheel-countdown-time"))
    )
        except:
            time.sleep(15)

        if(double(timer.text) < 0.5):
            print("Another spin...")
            print(timer.text)
            bet_wheel500(spins_count, timer)
            spins_count += 1
            time.sleep(15)
            

    
driver = webdriver.Firefox(executable_path="D:\\Pets\\RoulettesBot\\firefoxdriver\\geckodriver.exe")

print("Выберите рулеточку и напишите ее цифру:\n1. 500 Wheel;\n2. 500 Roulette\n3. CsgoRun;\n4. CsgoEmpire.")

chosen_website = int(input())
match chosen_website:
    case 1:
        wheel500()
    case 2:
        roulette500()
    case 3:
        url = "https://csgorun.gg/double"
    case 4:
        url = "https://csgoempire.com/"


    

driver.close()
driver.quit()
