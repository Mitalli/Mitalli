from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = Chrome(ChromeDriverManager().install())
driver.fullscreen_window()
#driver.get("https://www.google.com/")
driver.get("https://www.wikipedia.org/")
listofLang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")
print("Total number of language",len(listofLang))

time.sleep(2)
driver.close()