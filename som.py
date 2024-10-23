#######################################################################
# Script em Python de reconhecimento de fala para o sistema e Arduino #
# COLOMBO, MARCIO           v1.0                                      #
# 30-07-2024                                                          #
####################################################################### 

import speech_recognition as sr
import os
import serial
import time

# Ativando Arduino
arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
time.sleep(2)

def acender_led1():
    arduino.write(b"1")  # Comando 1 no pino 13

def apagar_led1():
    arduino.write(b"0")  # Comando 0 no pino 13

def acender_led2():
    arduino.write(b"2")  # Comando 2 no pino 7

def apagar_led2():
    arduino.write(b"3")  # Comando 3 no pino 7

def ligar_desligar_rapido():
    acender_led2()
    time.sleep(0.5)  # Tempo em segundos para o LED ficar ligado
    apagar_led2()

# Inicializando o reconhecedor de fala
recognizer = sr.Recognizer()

def concatenar_palavras(palavras):
    return ''.join(palavras)

while True:
    try:
        with sr.Microphone() as source:
            print("Diga um comando a ser executado: ")
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio, language="pt-BR")
                print(f"Você disse: {command}")

                command = command.lower()

                palavras = command.split()
                resultado = concatenar_palavras(palavras)
                print(f"Resultado: {resultado}")

                if resultado == "ligarled":
                    acender_led1()
                elif resultado == "desligarled":
                    apagar_led1()
      # O comando abaixo é para ligar e desligar um cliente PC
                elif resultado == "ligarcliente":
                    ligar_desligar_rapido()
                elif resultado == "desligarcliente":
                    apagar_led2()
                else:
                    print(f"Tentando executar o comando do sistema: {resultado}")
                    os.system(resultado)

            except sr.UnknownValueError:
                print("Não entendi o que você disse, por favor, tente novamente.")
            except sr.RequestError as e:
                print(f"Erro ao solicitar resultados do serviço de reconhecimento de voz; {e}")

    except KeyboardInterrupt:
        print("Encerrando o programa.")
        break

