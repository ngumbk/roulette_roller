# roulette_roller
Крутим

#Chrome description
def timer(driver, path): функция возвращает True, когда необходимо сделать ставку
driver: webdriver.Chrome(executable_path=<path to driver>)
path: XPath to Timer in driver.fine_element(By.XPATH, <XPath>)
!!!!После функции всегда испольщовать time.sleep(1), пока не впилим это в функцию