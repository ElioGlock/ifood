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
                    
                    break
                except: pass
                
            try:
                time.sleep(5)
                host = "imap.gmail.com"
                mail = Imbox(host,username=self.email,password=self.senha)

                while True:
                    msg_ifood = mail.messages(sent_from = "naoresponder@login.ifood.com.br",date__gt = date.today())
                    msg_list =[msg for uid, msg in msg_ifood]
                    if msg_list == None:
                        print("O codigo de acesso não foi enviado")
                        self.driver.find_element(By.XPATH,"//*[contains(text(),'Não recebi meu código')]").click()
                        self.driver.find_element(By.XPATH,"//*[contains(text(),'reenvidar código')]").click()
                        continue
                    else:
                        title = msg_list[-1].subject
                        if "é o seu código de acesso" in title:
                            list_code=[]
                            for n, code in enumerate(title[:6]):
                                self.driver.find_element(By.ID,f"otp-input-{n}").send_keys(code)
                                list_code.append(code)
                        else:continue
                    try:
                        time.sleep(1.5)
                        self.driver.find_element(By.XPATH,"//*[contains(text(),'Código expirado')]")
                        for n in range(6):self.driver.find_element(By.ID,f"otp-input-{n}").send_keys(Keys.BACKSPACE)
                    except:break
            except Exception as e: print("ERRO: " + e)

            while True:
                try:self.driver.find_element(By.CSS_SELECTOR,"[aria-label=Casa]").click();break
                except: time.sleep(5)
                print("okay")         

        self.ini_ifood = Thread(target=open_ifood,args=(self,))
        self.ini_ifood.start()

    

    