import datetime
import os
import subprocess
import webbrowser

import pyjokes
import speech_recognition as sr
import pyttsx3
from datetime import datetime

from playsound import playsound
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from wikipedia import wikipedia


# Hacemos un listener para el reconocimiento de la voz
listener = sr.Recognizer()

# Comandos de SALIDA de voz
engine = pyttsx3.init()

# Voces
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


pa = None
audio_stream = None

engine = pyttsx3.init()
engine.setProperty('voice', 'spanish')
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.5)

#Comando para que hable el asistente
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Comandos de ENTRADA de voz

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-ES")
            rec = rec.lower()
            if os.name in rec:
                print(rec)
    except:
        pass
    return rec

#Funcion para ejecutar el programa
def run():
    saludar = "Hola buenas, dime la funcion que quieres"
    talk(saludar)
    rec = listen()



    while rec:

        #Te dice el dia de la semana
        if 'dime el día de la semana' in rec:
            try:
                dia_actual = datetime.now()
                dia = str(dia_actual.strftime('%A'))
                texto = "el dia es  " + str(dia)
                talk(texto)
            except talk.Error:
                print
                "Error al saber el dia"
        #Te dice la hora
        if 'dime la hora' in rec:
            try :
                hora_actual = datetime.now()
                minuto = str(int(hora_actual.strftime('%M')))
                hora = str(int(hora_actual.strftime('%I')))
                if minuto == '0':
                    minuto = ''

                texto = ""
                if hora == '1':
                    texto = "Es la una " + str(minuto)
                else:
                    texto = "Son las " + str(hora) + " " + str(minuto)

                talk(texto)

            except talk.Error:
                print
                "Error en la hora"
        #Abre youtube
        if 'play youtube' in rec:
            webbrowser.open("https://www.youtube.com/")
            #Abre el navegador
        if 'abrir el navegador' in rec:
            webbrowser.open(
                "https://www.google.com/search?gs_ssp=eJzj4tTP1TcwMU02T1JgNGB0YPBiS8_PT89JBQBASQXT&q=google&rlz=1C1VDKB_esES1025ES1025&oq=goo&aqs=chrome.1.69i57j46i131i199i433i465i512j0i131i433i512l2j69i65j69i60l2j69i65.3866j0j7&sourceid=chrome&ie=UTF-8")
        #Busca en google
        if 'buscar en Google' in rec:
            talk("dime lo que quieres buscar en Google ")
            rec = listen()
            try:
                talk('Buscando en  Google...')
                webbrowser.open_new_tab("https://www.google.com/", + rec)
                talk("Esto es lo que hemos encontrado en google")
            except webbrowser.Error:
                print
            "No se ha encontrado en la Google."
        #busca en wikipedia

        if 'buscar en Wikipedia' in rec:
            talk("dime lo que quieres buscar")
            rec = listen()

        try:
            talk('Buscando en  Wikipedia...')
            wikipedia.summary(rec, sentences=1)
            talk("Esto es lo que hemos encontrado en Wikipedia")

        except webbrowser.Error:
            print
            "No se ha encontrado en la Wikipedia."
            #reproduce una cancion
        if 'reproducir cancion' in rec:
            rec = listen()
            try:
                playsound(rec + '.mp3')
            except playsound.Error:
                print
                "no se ha podido reproducir la cancion"
        #Apaga el ordenadorsi tienes los permisos
        if 'apagar el ordenador' in rec:
            try:
                talk("Espera un segundo ! Tu sistema se esta preparando para apagarse")
                subprocess.call('shutdown/ p /f')
            except subprocess.Error:
                print
                "no se ha podido apagar, necesitas dar permisos para poder hacerlo"


    #Dice los buenos dias
        if 'salir' in rec:
            rec("Gracias  y que tengas un buen dia")
            SystemExit
            #Da los buenos dias
        if "Buenos dias" in rec:
            talk("calurosos" + rec)
            talk("Como esta usted señor")
            #te cuenta un chiste
        if 'dime un chiste' in rec:
            chiste = pyjokes.get_joke(language='es', category='all')
            talk(chiste)
            #Traduce a texto
        if 'traduceme a texto' in rec:
            rec = listen()
            print(rec)
            #Crea un fichero de texto
        if 'crear un fichero de texto' in rec:
            talk("Dime lo que quieres pasa al txt")
            rec =listen()
            file = open("C:/filename.txt", "w")
            file.write(rec + os.linesep)
            file.close()
run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
