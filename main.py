from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="D:\\Pets\\RoulettesBot\\firefoxdriver\\geckodriver.exe")

url = "https://500.casino/wheel"


print(f"Выберите рулеточку и напишите ее цифру:\n1. CSGO 500;\n2. CsgoRun;\n3.CsgoEmpire.")


chosen_website = int(input())
match chosen_website:
    case 1:
        url = "https://500.casino/wheel"
    case 2:
        url = "https://csgorun.gg/double"
    case 3:
        url = "https://csgoempire.com/"

try:
    driver.get(url=url)
    #time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
