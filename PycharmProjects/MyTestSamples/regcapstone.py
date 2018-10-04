from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import datetime
import time
from selenium.webdriver.chrome.options import Options
import re

tstr = time.strftime("%y%m%d%H%M%S")
mdhm_str = time.strftime("%m%d%H%M")
hm_str = time.strftime("%M%S")
print(datetime.datetime.now())

out_logins = open("capstone_logins.txt", "a+")
driver = webdriver.Chrome('/home/mm/chromedriver')

driver.implicitly_wait(20)
driver.maximize_window()


#driver.get("https://rapidlite-qa.rapidsos.com/")
driver.get("https://rapidlite-qa2.rapidsos.com/")
# driver.get("https://rapidlite-staging.rapidsos.com/")
# driver.get("https://capstone-gaia-staging-mco-us-west-2.rapidsos.com/")
# driver.get("https://capstone-gaia-staging-mco-us-east-1.rapidsos.com/")
# driver.get("https://capstone-gaia-prod-mco-us-west-2.rapidsos.com/")
# driver.get("https://capstone-gaia-prod-mco-us-east-1.rapidsos.com/")
# driver.get("https://rapidlite.rapidsos.com/")
# driver.get("https://rapidlite-sandbox.rapidsos.com/")

# agency_name = 'QA_' + hm_str 
# login_email = 'iloloey+'+hm_str+'@rapidsos.com'
agency_name = 'rsos_agency_' + tstr
# agency_name = 'Prospector_Agency_Staging'
login_email = 'mmiddleton+'+tstr+'@rapidsos.com'
# login_email = 'jchoi+qa2@rapidsos.com'


# s = driver.current_url
# print(s)
# result = re.search('e-(.*).rapidsos.com', s)
# domain_env = result.group(1)
# print(domain_env)

s = driver.current_url
print(s)
result = re.search('https://(.*)/', s)
domain_name = result.group(1)
print(domain_name)


driver.find_element_by_link_text("GET FREE ACCESS").click()
driver.find_element_by_id("agencyName").send_keys(agency_name)
driver.find_element_by_id('firstName').send_keys('FirstName')
driver.find_element_by_id('lastName').send_keys('LastName')
# driver.find_element_by_id('email').send_keys('iloloey+'+tstr+'@rapidsos.com')
driver.find_element_by_id('email').send_keys(login_email)
# driver.find_element_by_id('email').send_keys('iloloey+180716195554@rapidsos.com')

driver.find_element_by_name('contactPhone').send_keys('12125553333')

# driver.find_element_by_id('firstName').send_keys('Steve')
# driver.find_element_by_id('lastName').send_keys('Johnson')
driver.find_element_by_id('contactTitle').send_keys('Boss')

driver.find_element_by_id('password').send_keys('Test123!')
driver.find_element_by_id('passwordConfirm').send_keys('Test123!')
driver.find_element_by_name("SignUp").click()
print(agency_name)
print(login_email)

# log_line = time.strftime("%Y-%m-%d %H:%M:%S") + ' ' + '-' + ' ' + agency_name + ' ' + login_email + ' ' + domain_env + '\n'
log_line = time.strftime("%Y-%m-%d %H:%M:%S") + ' ' + '-' + ' ' + agency_name + ' ' + login_email + ' ' + domain_name + '\n'

out_logins.write(log_line)

# driver.find_element_by_id('contactName').send_keys('InfoName')
# driver.find_element_by_id('contactTitle').send_keys('InfoTitle')
# driver.find_element_by_name('contactPhone').send_keys('12125553333')
driver.find_element_by_name('nonEmergencyNum').send_keys('+12125554444')
driver.find_element_by_id('population').send_keys('9999')
driver.find_element_by_xpath('//*[@id="provide-info-container"]/form/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span[1]').click()
driver.find_element_by_xpath('//*[text()="VESTA"]').click()
driver.find_element_by_xpath('//*[@id="provide-info-container"]/form/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span[1]').click()
driver.find_element_by_xpath('//*[text()="DDTI"]').click()
driver.find_element_by_xpath('//*[@id="provide-info-container"]/form/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div[1]/div/span[1]').click()
driver.find_element_by_xpath('//*[text()="TotalCommand"]').click()
time.sleep(5)
# driver.find_element_by_xpath('//*[@id="provide-info-container"]/form/div[2]/div/div[2]/div/div[3]/div[2]').click()
driver.find_element_by_xpath('//*[text()="Define coverage area +"]').click()
time.sleep(5)
# //*[@id="provide-info-container"]/form/div[1]/div/div/div[3]/div[2]/div/div[2]/span
# driver.find_element_by_id('mapTitle').send_keys('GeoFence' + tstr )
driver.find_element_by_id('geofenceName').send_keys('GeoFence' + tstr )
time.sleep(5)
driver.find_element_by_xpath('//*[text()="Save"]').click()
print ('GeoFence' + tstr )
time.sleep(5)
driver.find_element_by_id('Next').click()

# time.sleep(5)
all_cookies = driver.get_cookies()
print(all_cookies)

driver.find_element_by_id('signature').send_keys('My Name')
driver.find_element_by_id('licenseAgreement').click()
# driver.get("https://rapidlite-qa.rapidsos.com/")
# driver.get("https://andromeda-qa.rapidsos.com/")
# time.sleep(5)
print('done')
driver.quit()
# 19182011610






