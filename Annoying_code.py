# Launch the code and it will open chrome with whatsapp automatically. Scan the QR Code with your mobile
# whatsapp so that your contacts load into webpage. You have to download Chromedriver first. You also  have to
# install selenium library. I did it by writing "pip install selenium" in command prompt. You have to make sure
# you have pip pre installed. Otherwise you have to install pip first and then selenium library.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Place the link of downloaded and extracted  chromedriver.exe location in inverted commas. For my case it is
# like below:
driver=webdriver.Chrome("C:\setups\chromedriver\chromedriver.exe")

driver.get("https://web.whatsapp.com/")

name=input("Enter the name of person or group: ")
count=eval(input("How many times: "))

input("Wait for ENTER")

user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
msg_box=driver.find_element_by_class_name("_1Plpp")
for msg in range(count):
    msg_box.send_keys(msg)
    button=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, '_35EW6')))
    button.click()