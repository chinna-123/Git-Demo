import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/seleniumPractise/#/")
d.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
results = d.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

# chaining of web elements

for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expectedList == actualList

d.find_element(By.CSS_SELECTOR, " img[alt='Cart']").click()
d.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation

prices = d.find_elements(By.CSS_SELECTOR, " tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalprice = int(d.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalprice


d.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
d.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(d, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(d.find_element(By.CLASS_NAME, "promoInfo").text)

discountedAmount = float(d.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalprice > discountedAmount