from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://sugang.deu.ac.kr:8080/DEUSugang_LogIn.aspx')

# Find login elements
text_field = driver.find_element(By.NAME, "txtID")
text_field2 = driver.find_element(By.NAME, "txtPW")
login_main = driver.find_element(By.ID, "ibtnLogin")

# Login
text_field.send_keys("YOUR_ID")
text_field2.send_keys("YOUR_PW")
login_main.click()
time.sleep(3)

# Go to sugang page
sugang_butten = driver.find_element(By.XPATH, "//a[text()='수강신청']")
sugang_butten.click()
time.sleep(3)

# Find sugang frame & shotgun butten
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@src="/DEUsugang.aspx"]'))
jangbwa_butten = driver.find_element(By.XPATH, '//*[@id="CP1_rbtnlGangjwaType_0"]')
jangbwa_butten.click()

# Select specific class and click
button = driver.find_element(By.ID, 'CP1_dt_result_BtnSugangApply_1')
button.click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.alert.accept()

# Loop
while True:
    try:
        print("아")
        button = driver.find_element(By.ID, 'CP1_dt_result_BtnSugangApply_1')
        button.click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.switch_to.alert.accept()
    except KeyboardInterrupt:
        break
    except:
        print(f"먼가 먼가 오류임")
        time.sleep(1)
        pass
