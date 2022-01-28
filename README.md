# roulette_roller
Крутим

#Chrome description
def timerstopper(driver, path): функция возвращает True, когда необходимо сделать ставку
driver: webdriver.Chrome(executable_path=<path to driver>)
path: XPath to Timer in driver.fine_element(By.XPATH, <XPath>)
!!!!После функции всегда испольщовать time.sleep(1), пока не впилим это в функцию

#Comments
28.01.2022 - 7:24
    Придумать способ хранения собранных ставок и способ извлечения победной ставки.
Потестить, нормально ли работает метод на 0.05. 
Найти способ избежать выводов 'Крутится' и 'Игра завершена'

'