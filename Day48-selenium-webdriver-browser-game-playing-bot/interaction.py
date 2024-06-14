from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

#number_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#print(number_of_articles.text)

#to press on a link
#number_of_articles.click()

#pending_changes = driver.find_element(By.LINK_TEXT, value="Pending changes")
#pending_changes.click()

#find Search input
#search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")

#search.send_keys("Python")
#search.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
sign_up = driver.find_element(By.CLASS_NAME, "btn")

#fname.click() # not needed at all
fname.send_keys("name")
#lname.click()
lname.send_keys("123")
#email.click()
email.send_keys("name.123@email.com")
sign_up.click()
