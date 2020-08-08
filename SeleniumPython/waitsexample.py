import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="F:\Browser_drivers\chromedriver.exe")
#driver =webdriver.Firefox(executable_path="F:\Browser_drivers\geckodriver.exe")
#driver = webdriver.Edge(executable_path="F:\Browser_drivers\msedgedriver.exe")
#driver=webdriver.Ie(executable_path="F:\Browser_drivers\IEDriverServer.exe")
driver.get("http://rahulshettyacademy.com/seleniumPractise")
driver.maximize_window()

driver.find_element_by_xpath("(//div[@class='product-action']/button)[1]").click()
driver.find_element_by_xpath("(//div[@class='product-action']/button)[2]").click()
driver.find_element_by_xpath("(//div[@class='product-action']/button)[3]").click()
driver.find_element_by_xpath("(//div[@class='product-action']/button)[4]").click()

driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()


time.sleep(3)
driver.find_element_by_xpath("//input").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[text()='Apply']").click()