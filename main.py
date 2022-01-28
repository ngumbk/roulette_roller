from pydoc import cli
from numpy import double
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

balance = 1.28
a = "fad"

def bet(spins_count, timer, file1):
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
    file1.write(f"{spins_count}. {counter_x2.text} / {counter_x3.text} / {counter_x5.text} / {counter_x50.text} || {estimated_prize[0]} / {estimated_prize[1]} / {estimated_prize[2]} / {estimated_prize[3]} ")
    print(f"Таймер в конце ставки: {timer.text}")

    #делаем ставку
    if estimated_prize[0] == min_estimated:
        expected = "black"
        file1.write("ставка х2\n")
    elif estimated_prize[1] == min_estimated:
        expected = "red"
        file1.write("ставка х3\n")
    elif estimated_prize[2] == min_estimated:
        expected = "blue"
        file1.write("ставка х5\n")
    elif estimated_prize[3] == min_estimated:
        expected = "yellow"
        file1.write("ставка х50\n")
    
    
    balance -= 0.01
    print(f"Баланс после вычета 0.01: {balance}")
    print(f"expected: {expected}")
    time.sleep(4)

    #проверяем ставку
    game_result = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[2]/main/div[2]/div[1]/div/div[2]/div/div[1]/div[100]")
    game_result = game_result.get_attribute("class")
    match game_result:
        case "round-history-list-item black":
            if (expected == "black"):
                balance += 0.02
        case "round-history-list-item red":
            if (expected == "red"):
                balance += 0.03
        case "round-history-list-item blue":
            if (expected == "blue"):
                balance += 0.05
        case "round-history-list-item yellow":
            if (expected == "yellow"):
                balance += 0.50

    file1.write(f"Баланс: {balance}\n")
    print(f"Баланс после результата: {balance}")
    file1.close()

def csgo500():
    url = "https://500.casino/wheel"
    driver.get(url=url)
    spins_count = 1
    print("Теперь логинься и жми на глаз, у тебя 60 сек")
    time.sleep(60) #time to login
    print("Ok, let's go!")

    #запись статистики в файл
    file1 = open('strategy_result_1_bet.txt', 'a')
    file1.write(time.asctime() + '\n\n')
    file1.close()
    #file2 = open('strategy_result_2_bets.txt', 'a')
    #file2.write(time.asctime(), end="\n\n")
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
            bet(spins_count, timer, file1)
            spins_count += 1
            time.sleep(15)
            
        
    
driver = webdriver.Firefox(executable_path="D:\\Pets\\RoulettesBot\\firefoxdriver\\geckodriver.exe")

print("Выберите рулеточку и напишите ее цифру:\n1. CSGO 500;\n2. CsgoRun;\n3.CsgoEmpire.")

chosen_website = int(input())
match chosen_website:
    case 1:
        csgo500()
    case 2:
        url = "https://csgorun.gg/double"
    case 3:
        url = "https://csgoempire.com/"


    

driver.close()
driver.quit()
