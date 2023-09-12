from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math 
def calc(x):
    return str(math.log(abs(
    12*math.sin(int(x))
    )))
try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, "book").click()
    x_element = calc(browser.find_element(
    By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(x_element)
    browser.find_element(By.ID, "solve").click() 
    alert = browser.switch_to.alert
    answer = list(alert.text.split())[-1]
    alert.accept()
    browser.get("https://stepik.org/catalog?auth=login")
    browser.find_element(By.ID, "id_login_email").send_keys(#тут должен быть имэйл)
    browser.find_element(By.ID, "id_login_password").send_keys(#тут должен быть пароль)
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    time.sleep(5)
    browser.get("https://stepik.org/lesson/181384/step/8?auth=login&unit=156009")
    browser.find_element(By.CSS_SELECTOR, "[spellcheck='false']").send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()    
    time.sleep(5)
finally:
    time.sleep(5)
    browser.quit()
