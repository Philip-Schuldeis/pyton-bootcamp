from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.de/-/en/Portable-Monitor-Touchscreen-External-Raspberry/dp/B0CB3ZL89N/ref=sr_1_17?crid=2NDXXWQGAKBJH&dib=eyJ2IjoiMSJ9._tSNenf7_7cwzC5iwfpMq-CymRwK1-awIIiWsYrPgakoHE5fNaZEVLXdX2CxhZvGTewcMWd0BTd6dq1iPzGVtnLkSqYckFSSgn4CH3kphrQJd5NSBq5_mA9_GU9NFRFg8V3zEZuRqrR_lW2-tA1e05Vow5mGRxEVORj7InMHBZIrYTTmIiKKWoDFBxMS659776PWEuonaHuE4CPIphPPUykosorMn-dmwZfOR87qS0I.YuLAK-vAaD9gc6JaYhlftrii6tF0wyEmyUuQsZAF86c&dib_tag=se&keywords=mini+portable+monitor+touch&qid=1718308489&sprefix=mini+portable+monitor+touch%2Caps%2C111&sr=8-17&ufe=app_do%3Aamzn1.fos.335e368b-29e8-4542-bb58-939a88195e78")

price_euro = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

print(f"Price: {price_euro.text}.{price_cents.text}")

driver.quit()
# Ok never mind no need to take another look at day 47

