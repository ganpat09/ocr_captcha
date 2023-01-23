# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 09:53:44 2023

@author: pc
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import base64




try:
    PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT
    
    options = webdriver.ChromeOptions()
   # options.add_argument('--proxy-server=%s' % PROXY)
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'.\chromedriver_win32\chromedriver.exe')

    #chrome = webdriver.Chrome(options=chrome_options)
    driver.get("https://cra-nsdl.com/CRA/")
    
    data = set()
    
    for i in range(1000):
        try:
            print("counter no",i+1)
            driver.refresh()
            upper_x_path = "/html/body/div[1]/div/table/tbody/tr[1]/td/div[3]/div[2]/div[1]/form/div[3]/table/tbody/tr[1]/td[2]/img"
            #/html/body/div[1]/div/table/tbody/tr[1]/td/div[3]/div[2]/div[1]/form/div[3]/table/tbody/tr[1]/td[2]/img
            
            lower_x_path = "/html/body/div[1]/div/table/tbody/tr[1]/td/div[3]/div[2]/div[2]/form/div[5]/table/tbody/tr[1]/td[2]/img"
            #/html/body/div[1]/div/table/tbody/tr[1]/td/div[3]/div[2]/div[2]/form/div[5]/table/tbody/tr[1]/td[2]/img
            driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver,20 ).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='page_wrapper']/div/table/tbody/tr[1]/td/div[3]/div[2]/div[1]"))))
            upper_captcha = driver.find_element("xpath",upper_x_path).get_attribute("src")
        
        
            lower_captcha  = driver.find_element("xpath",lower_x_path).get_attribute("src")
            
            data.add(upper_captcha)
            data.add(lower_captcha)
                
            
        except Exception as e:
            print("Diffculty error on refresh",e)
        
    driver.quit()
    print("final data length",len(data))
    for ix,d in  enumerate(data):
        base64_code = d.split("base64, ")[1]
        img_data = base64_code.encode()
        content = base64.b64decode(img_data)
        
        with open(f"captcha_imgs/{(ix+1)}.jpg", "wb") as fh:
            fh.write(content)
        
        
    
    
except Exception as e:
    
    print(e)
    driver.quit()
    raise e
