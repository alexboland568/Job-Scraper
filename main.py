# Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# Indeed is where I'm scraping my data from 
driver.get("https://www.indeed.com/")
print("Welcome to my job scraping application!")
job = input("Enter the name of the job you are looking for: ")
zipcode = input("Enter your zip code (or 'remote'): ")
elem = driver.find_element_by_name("q") # Job title input element
elem.send_keys(job)
elem = driver.find_element_by_name("l") # Zipcode input element 
elem.send_keys(zipcode)
elem.send_keys(Keys.RETURN)