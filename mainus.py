import sys
print (sys.argv)
import time
import names
from selenium import webdriver

print("KRISPY KREME ACCOUNT MAKER MADE BY Mr.Bean#0101")
print("Please enter your Email: ")
email = input("")
print("First 3 Numbers of Phone #")
phoneFirst = input("")
print("Seccond 3 Numbers of Phone #")
phoneSeccond = input("")
print("Last 4 Numbers of Phone #")
phoneThird = input("")
print("password = Password123!")



def order():

    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_txtFirstName"]').send_keys(names.get_first_name())
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_txtLastName"]').send_keys(names.get_last_name())
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_txtBirthday"]').send_keys("11/21")
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_txtZipCode"]').send_keys("33673")
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_ucPhoneNumber_txt1st"]').send_keys(phoneFirst)
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_ucPhoneNumber_txt2nd"]').send_keys(phoneSeccond)
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_ucPhoneNumber_txt3rd"]').send_keys(phoneThird)
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_txtEmail"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_txtPassword"]').send_keys("Password123!")
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_cbTermsOfUse"]').click()
    driver.find_element_by_xpath('//*[@id="ctl00_plcMain_btnSubmit"]').click()

if __name__ == '__main__':
    #load chrome
   driver = webdriver.Chrome('./chromedriver')

   driver.get("https://www.krispykreme.com/account/create-account?returnUrl=%2faccount%2fprofile")
   order()
