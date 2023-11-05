import time
from datetime import date
import generic
import os
from os import path

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import random

from pydub import AudioSegment
import speech_recognition as sr

import requests

#conf
username = "ser.sebastiani@gmail.com"
password = "Merca2+tello"

#log
my_logger = generic.set_logger()
my_logger.info("Avvio scrapping script")

#conf
image_path =  os.path.join(os.path.dirname(os.path.realpath(__file__)) , str(date.today()) + "_screen")
if not os.path.exists(image_path):
       os.makedirs(image_path)
       
#code
o = uc.ChromeOptions()
driver = uc.Chrome(advanced_elements=True, options=o)
page = "https://private.e-distribuzione.it/PortaleClienti/s/login/"
driver.get(page)
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure0.png")
my_logger.info("andato a pagina: " +  page)


node = driver.find_element(By.ID, "truste-consent-button")
node.click()
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure1.png")
my_logger.info("abbassato il pop-up")

elem_xpath = '//input[@id="input-10"]'
node = driver.find_element(By.XPATH, elem_xpath)
node.send_keys(username)
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure1.png")
my_logger.info("inserito username: " + username)

elem_xpath = '//input[@id="input-12"]'
node = driver.find_element(By.XPATH, elem_xpath)
node.send_keys(password)
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure2.png")
my_logger.info("inserito password: " + password)

elem_xpath = "//p[contains(text(), 'ENTRA')]"
node = driver.find_element(By.XPATH, elem_xpath)
node.click()
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure3.png")
my_logger.info("cliccato ENTRA")

elem_tag_name = 'iframe'
node = driver.find_elements(By.TAG_NAME, elem_tag_name)
print(len(node))
#print(node[0].get_property('title'))
#print(node[1].get_property('title'))
print(node[2].get_property('title'))
driver.switch_to.frame(node[2])
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure4.png")
my_logger.info("spostato su elemento iframe")

elem_tag_name = 'button'
node = driver.find_elements(By.TAG_NAME, elem_tag_name)
print(len(node))
#print(node[0].get_property('title'))
print(node[1].get_property('title'))
driver.save_screenshot(image_path + "/nowsecure5.png")
node[1].click()
my_logger.info("cliccato elemento tipo button con proprieta title: " + str(node[1].get_property('title')))
time.sleep(random.randint(3, 5))

actions = ActionChains(driver)
elem_tag_name = 'a'
node = driver.find_elements(By.TAG_NAME, elem_tag_name)
print(len(node))
actions = ActionChains(driver)
actions.move_to_element(node[0])
audio_href = node[0].get_attribute("href")
my_logger.info("individuato link audio: " + audio_href)

audio_mp3_file = image_path + "/downloaded_audio.mp3"
generic.download_audio_from_link(audio_href, audio_mp3_file)
my_logger.info("salvato audio nel file: " + audio_mp3_file)

# files
# #src = "data/downloaded_audio.mp3"
audio_mp3_file = image_path + "/downloaded_audio.mp3"
audio_wav_file = image_path + "/downloaded_audio.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(audio_mp3_file)
sound.export(audio_wav_file, format="wav")
my_logger.info("salvato audio in formato wav: " + audio_wav_file)

#filename = audio_wav_file
r = sr.Recognizer()

with sr.AudioFile(audio_wav_file) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    #f = open("data/audio_text.txt", "w")
    #f.write(text)
    #f.close()
    #print(text)

my_logger.info("estrapolato contenuto file audio: " + text)
time.sleep(random.randint(3, 5))

elem_xpath = '//input[@id="audio-response"]'
node = driver.find_elements(By.XPATH, elem_xpath)
print(len(node))
node[0].send_keys(text)
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure6.png")
my_logger.info("scritto testo nel campo con xpath: " + elem_xpath)

elem_xpath = '//button[@id="recaptcha-verify-button"]'
node = driver.find_elements(By.XPATH, elem_xpath)
print(len(node))
node[0].click()
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure7.png")
my_logger.info("cliccato campo verifica con xpath: " + elem_xpath)

'''
elem_xpath = '//button[@class="slds-button pointer"]'
node = driver.find_elements(By.XPATH, elem_xpath)
print(len(node))
node[0].click()
time.sleep(3)
driver.save_screenshot(image_path + "/nowsecure8.png")
'''

page = "https://private.e-distribuzione.it/PortaleClienti/s/curvedicarico"
driver.get(page)
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure8.png")
my_logger.info("spostato sulla pagina con misure: " + page)

f = open(image_path + "/pagina_misure.html", "w")
f.write(driver.page_source)
f.close()
my_logger.info("salvato contenuto pagina nel file: " + image_path + "/pagina_misure.html")

elem_xpath = "//button[contains(text(), 'Sergio Sebastiani')]"
node = driver.find_elements(By.XPATH, elem_xpath)
print(len(node))
node[0].click()
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure9.png")
my_logger.info("cliccato elemento epr uscire con xpath: " + elem_xpath)

elem_xpath = "//span[contains(text(), 'Esci')]"
node = driver.find_elements(By.XPATH, elem_xpath)
print(len(node))
node[0].click()
time.sleep(random.randint(3, 5))
driver.save_screenshot(image_path + "/nowsecure10.png")
my_logger.info("cliccato elemento epr uscire con xpath: " + elem_xpath)

driver.quit()
my_logger.info("Fine scrapping script")