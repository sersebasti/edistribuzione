import logging
import time
import os
from os import path
from datetime import date
import requests

def set_logger():
       
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
   
   return logger_log


def download_audio_from_link(audio_link, output_file):
    try:
        response = requests.get(audio_link)
        if response.status_code == 200:
            with open(output_file, 'wb') as file:
                file.write(response.content)
            print("Audio file downloaded and saved as: " + output_file)
        else:
            print("Failed to download the audio. Status code: "  + response.status_code)
    except Exception as e:
        print("An error occurred: " + str(e))