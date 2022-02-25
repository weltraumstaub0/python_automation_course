from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
     
    book_button = browser.find_element(By.CSS_SELECTOR, "#book")
    price_tag = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100")
         
    )

    book_button.click()

    x_value = browser.find_element(By.CSS_SELECTOR, "span#input_value").text

    result = math.log(abs(12 * math.sin(int(x_value))))
    input_field = browser.find_element(By.CSS_SELECTOR, "input[name='text']")
    input_field.send_keys(result)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    print(browser.switch_to.alert.text)
finally:
    time.sleep(10)
    browser.quit()