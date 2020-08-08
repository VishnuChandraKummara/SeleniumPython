from selenium import webdriver
driver=webdriver.Chrome(executable_path="F:\Browser_drivers\chromedriver.exe")
#driver =webdriver.Firefox(executable_path="F:\Browser_drivers\geckodriver.exe")
#driver = webdriver.Edge(executable_path="F:\Browser_drivers\msedgedriver.exe")
#driver=webdriver.Ie(executable_path="F:\Browser_drivers\IEDriverServer.exe")
driver.get("http://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
print(driver.title)

#driver.get("http://rahulshettyacademy.com/AutomationPractice")
#driver.close()

driver.find_element_by_name("name").send_keys("Vishnu")
driver.find_element_by_name("email").send_keys("kummaravishnu2@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Vishnu")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_css_selector("input[type='submit']").click()
print(driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)

