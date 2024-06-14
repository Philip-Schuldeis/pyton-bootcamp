import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
#
# url = "https://www.amazon.de/-/en/Portable-Monitor-Touchscreen-External-Raspberry/dp/B0CB3ZL89N/ref=sr_1_17?crid=2NDXXWQGAKBJH&dib=eyJ2IjoiMSJ9._tSNenf7_7cwzC5iwfpMq-CymRwK1-awIIiWsYrPgakoHE5fNaZEVLXdX2CxhZvGTewcMWd0BTd6dq1iPzGVtnLkSqYckFSSgn4CH3kphrQJd5NSBq5_mA9_GU9NFRFg8V3zEZuRqrR_lW2-tA1e05Vow5mGRxEVORj7InMHBZIrYTTmIiKKWoDFBxMS659776PWEuonaHuE4CPIphPPUykosorMn-dmwZfOR87qS0I.YuLAK-vAaD9gc6JaYhlftrii6tF0wyEmyUuQsZAF86c&dib_tag=se&keywords=mini+portable+monitor+touch&qid=1718308489&sprefix=mini+portable+monitor+touch%2Caps%2C111&sr=8-17&ufe=app_do%3Aamzn1.fos.335e368b-29e8-4542-bb58-939a88195e78"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
#     "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
# }
#
# response = requests.get(url, headers=header)
#
# soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
#
# price = soup.find("span", class_="aok-offscreen")
# #whole_price = soup.find(name="span", class_ = "a-price-whole")
# #fraction_price = soup.find(name="span", class_ = "a-price-fraction")
# #final_price = float(whole_price.getText() + fraction_price.getText())
# # price_without_currency = price.split("€")[1]
# #price_as_float = float(price_without_currency)
#
# #print(price_as_float)
# #print(whole_price)
# #print(fraction_price)
# #print(final_price)
#
# print(price)

#I got captured every time when i tried it form the german website imma have to get a deeper look at it another time
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 60

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("Your E-Mail", "Your App Password")
        connection.sendmail(
            from_addr="Your E-Mail",
            to_addrs="Your E-Mail",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )