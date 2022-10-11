import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Proyectos_Python\Selenium\chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://www.google.com/');

time.sleep(5) # Let the user actually see something!

#search_box = driver.find_element_by_name('q')

#search_box.send_keys('ChromeDriver')

#search_box.submit()


driver.find_element(By.XPATH,'//*[@id="gb"]/div/div[1]/div/div[2]/a').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()   
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('imagen de perro')  
time.sleep(5) 
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
 


#driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Hola Fran!!!')
#driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button/span').click() #Clicl a Enviar





time.sleep(5) 
#driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[2]/div/div/div[9]/div/div/div[2]/div[1]/div/span/span').click()

#driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys('Holaaaa Wen día, hoy es el gran día')

#driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button/span').click() #Clicl a Enviar





time.sleep(60) # Let the user actually see something!

driver.quit()
