import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time

class Alicia:
    def __init__(self):
        self.pedidos_keywords = ["pedido","rapido","rápido,","instantâneo","padrão","clássico","sempre","ágil"]
        self.quit_keywords = ["sai","fecha","encerra","cancelar"]
        self.quit = False
        self.retorno = []

        self.loop()
    def ouvir_microfone(self):
        
        microfone = sr.Recognizer()
        
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)

            path = os.path.join("default_audios","talk.mp3")
            playsound(path)
            audio = microfone.listen(source)

        try:frase = microfone.recognize_google(audio,language ="pt-BR")
        except:
            path = os.path.join("default_audios","error.mp3")
            playsound(path)
            time.sleep(3)
            return self.ouvir_microfone()
        
        return frase
    
    def reproduzir_audio(self,txt,file="last_comand.mp3"):
        tts = gTTS(txt,lang="pt-br")
        time.sleep(0.5)
        try:tts.save(file)
        except:print("erro ao salver file")

        path = file
        playsound(path)


    def loop(self,txt =""):
        txt = txt + self.ouvir_microfone()
        if any(word in txt for word in self.quit_keywords):
            self.quit = True
        
        elif any(word in txt for word in self.pedidos_keywords):
            if not "configurado_path" in txt:
                self.reproduzir_audio("Qual pedido de sempre?","Alternative_command.mp3")
                return self.loop(f"configurado_path{txt}")
            
            if any(word in txt for word in["um","1"]):
                self.retorno =["padrao",1]
                self.reproduzir_audio("Você pediu o numero 1")
                print("pedido 1")
            if any(word in txt for word in["dois","2"]):
                self.retorno =["padrao",2]
                self.reproduzir_audio("Você pediu o numero 2")
                print("pedido 2")
            if any(word in txt for word in["três","3"]):
                self.retorno =["padrao",3]
                self.reproduzir_audio("Você pediu o numero 3")
                print("pedido 3")
        
        else:
            print("Nao entendi nada")
            return self.ouvir_microfone()
        print(txt)



        
ali = Alicia()












