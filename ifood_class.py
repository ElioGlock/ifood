from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import   Options

from imbox import Imbox
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
            
            while True:
                try:
                    self.driver.find_element(By.XPATH,"//*[contains(text(),'Entrar ou cadastrar')]").click()
                    self.driver.find_element(By.XPATH,"//*[contains(text(),'E-mail')]").click()
                    self.driver.find_element(By.NAME,"email").send_keys("ifoood061@gmail.com"+Keys.ENTER)
                except: pass
                    

try:
    time.sleep(5)
    senha  = open(os.path.join("passwords","password_gmail"),"r").read()
    email = "ifoood061@gmail.com"
    host = "imap.gmail.com"
    mail = Imbox(host,username=email,password=senha)

    while True:
        msg_ifood = mail.messages(sent_from = "naoresponder@login.ifood.com.br",date__gt = date.today())
        msg_list =[msg for uid, msg in msg_ifood]
        if msg_list == None:
            print("O codigo de acesso não foi enviado")
            driver.find_element(By.XPATH,"//*[contains(text(),'Não recebi meu código')]").click()
            driver.find_element(By.XPATH,"//*[contains(text(),'reenvidar código')]").click()
            continue
        else:
            tit
        pass
except Exception as e: print("ERRO: " + e)
        