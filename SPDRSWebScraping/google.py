
#Source:https://www.tutorialspoint.com/fetch-all-href-link-using-selenium-in-python
from selenium import webdriver

driver = webdriver.Chrome (executable_path='C:\\Users\\drivers\\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.google.com/")
# identify elements with tagname <a>
lnks=driver.find_elements_by_tag_name("a")
# traverse list
for lnk in lnks:
   # get_attribute() to get all href
   print(lnk.get_attribute('href'))
driver.quit()