import time

from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\ivan.pereira\Documents\Python_Proyects\Selenium\chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://online.jfleischman.com/ords/f?p=102:5:12670257589417::NO:::');

time.sleep(5)

driver.find_element_by_css_selector('#boton').click()




time.sleep(60) # Let the user actually see something!
