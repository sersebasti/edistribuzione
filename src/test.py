import logging
import subprocess
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import requests
import os
from os import path
from datetime import date

today = date.today()
dir_path = os.path.dirname(os.path.realpath(__file__))

log_path =  os.path.join(os.path.join(dir_path, "Logs"),str(today)) 
if not os.path.exists(log_path):
   os.makedirs(log_path)
   
timestr = time.strftime("%H%M%S")
log_filename = os.path.join(log_path, timestr + '_log.txt')

logger_log = logging.getLogger('logger_log')
logger_log.setLevel(logging.INFO)
file_handler_log = logging.FileHandler(log_filename)
file_handler_log.setLevel(logging.INFO)
formatter_log = logging.Formatter('%(asctime)s %(message)s')
logger_log.addHandler(file_handler_log)

logger_log.info("ciao")


'''
o = uc.ChromeOptions()
driver = uc.Chrome(advanced_elements=True, options=o)
driver.get("https://www.sergioswebsolutions.com/CV/")
time.sleep(5)
driver.save_screenshot("data/nowsecure0.png")

print("ciao")
'''
