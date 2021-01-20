from selenium import webdriver

driver = webdriver.Chrome(executable_path=".\chromedriver\chromedriver.exe")
driver.get("https://www.python.org/")

elems = driver.find_elements_by_xpath("//a[@href]")

for r in range(0, len(elems)):
    driver.execute_script("document.getElementsByTagName('a')" + str([r]) + ".removeAttribute('href');")

