from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import   Options

from imbox import imbox
from email.message import EmailMessage

from datetime import date,datetime
import time
import re
import json
import os

from threading import Thread

class Ielio:
    def __init__(self,email):
        self.email = email
        self.passowrds = open(os.path.join("passwords","password_gmail"),"r").read()
        self.valor_final = 0 
        self.retorno = []

        self.initialize_ifood()

    def initialize_ifood(self):
        def open_ifood(self):
            chrome_options = Options()
            service = Service(ChromeDriverManager().install())
            # chrome_options.add_argument("--headless")
            
            self.driver = webdriver.Chrome(service=service,options=chrome_options)
            self.driver.get("https://ww.ifood.com.br/inicio")
             

        