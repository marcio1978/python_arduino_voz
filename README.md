# Comando de Voz para Controle de LEDs

Este projeto foi desenvolvido para autodidatas e entusiastas de eletrônica e programação que desejam explorar o controle de hardware com Python e Arduino usando reconhecimento de voz. Ele demonstra como controlar LEDs conectados a um Arduino por meio de comandos de voz, reconhecidos por um script em Python e outros scripts no sistema Linux. 

## Descrição do Projeto

Neste projeto, utilizamos a comunicação serial entre um Arduino e um script Python para controlar dois LEDs conectados aos pinos 12 e 13 do Arduino. O usuário emite comandos de voz que são capturados e processados pelo Python usando a biblioteca `SpeechRecognition`. Os comandos reconhecidos são enviados ao Arduino, que, por sua vez, aciona os LEDs conforme o comando.

## Tecnologias Utilizadas

- **Arduino**: Microcontrolador para controle de LEDs.
- **Python**: Linguagem usada para capturar e processar os comandos de voz, além de enviar os comandos para o Arduino.
- **PySerial**: Biblioteca Python para comunicação com o Arduino via porta serial.
- **SpeechRecognition**: Biblioteca Python usada para reconhecimento de voz.

## Instalação e Execução

### Requisitos

- Arduino IDE instalado
- Python 3 instalado
- Placa Arduino (ex: Arduino Uno)
- 2 LEDs conectados aos pinos 12 e 13 do Arduino
- Protoboard e resistores para os LEDs

### Passo 1: Carregar o código no Arduino

1. Abra o **Arduino IDE** e copie o código abaixo no editor:
   ```cpp
   int ledPin1 = 13;
   int ledPin2 = 12;

   void setup() {
     pinMode(ledPin1, OUTPUT);
     pinMode(ledPin2, OUTPUT);
     Serial.begin(9600);
   }

   void loop() {
     if (Serial.available() > 0) {
       char command = Serial.read();
       if (command == '1') {
         digitalWrite(ledPin1, HIGH);  // Liga LED 1
       } else if (command == '0') {
         digitalWrite(ledPin1, LOW);   // Desliga LED 1
       } else if (command == '2') {
         digitalWrite(ledPin2, HIGH);  // Liga LED 2
       } else if (command == '3') {
         digitalWrite(ledPin2, LOW);   // Desliga LED 2
       }
     }
   }

Conecte seu Arduino ao computador e faça o upload do código para a placa.

Passo 2: Configuração do Python

Clone este repositório:

bash
      
      git clone https://github.com/marcio1978/python_arduino_voz.git
      cd seu-repositorio


Passo 2: Configuração do Python

Clone este repositório:

bash
      
      git clone https://github.com/marcio1978/python_arduino_voz.git
      cd seu-repositorio

Instale as dependências Python: Certifique-se de que o Python 3 está instalado. Em seguida, execute:

bash

    pip install pyserial SpeechRecognition

Conecte o Arduino à porta USB e ajuste a porta serial no script Python, conforme necessário (por exemplo, /dev/ttyACM0 no Linux).

Passo 3: Código Python

Copie o seguinte código Python para o arquivo controle_led.py:

      python

      import speech_recognition as sr
      import serial
      import time

      # Configurando a comunicação serial com o Arduino
      arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Ajuste a porta conforme necessário
      time.sleep(2)  # Tempo para o Arduino inicializar

      def acender_led1():
          arduino.write(b'1')  # Envia o comando para ligar o LED 1 (pino 13)

      def apagar_led1():
          arduino.write(b'0')  # Envia o comando para desligar o LED 1

      def acender_led2():
          arduino.write(b'2')  # Envia o comando para ligar o LED 2 (pino 12)

      def apagar_led2():
          arduino.write(b'3')  # Envia o comando para desligar o LED 2

      # Inicializando o reconhecedor de fala
      recognizer = sr.Recognizer()

      while True:
          try:
              with sr.Microphone() as source:
                  print("Diga um comando: ")
                  audio = recognizer.listen(source)

                  command = recognizer.recognize_google(audio, language="pt-BR")
                  print(f"Você disse: {command}")

                  # Converte o comando para minúsculas
                  command = command.lower()

            if command == "liga":
                acender_led1()
            elif command == "desliga":
                apagar_led1()
            elif command == "liga dois":
                acender_led2()
            elif command == "desliga dois":
                apagar_led2()
            else:
                print("Comando não reconhecido. Diga 'liga', 'desliga', 'liga dois' ou 'desliga dois'.")

    except sr.UnknownValueError:
        print("Não entendi o que você disse, por favor, tente novamente.")
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de voz; {e}")
    except KeyboardInterrupt:
        print("Encerrando o programa.")
        break

Como Executar

   Execute o script Python: No terminal, execute:

   bash

    python controle_led.py

   Diga um comando de voz: O microfone irá capturar seus comandos. Fale "liga", "desliga", "liga dois" ou "desliga dois" para controlar os LEDs conectados ao Arduino.

Comandos de Voz

    "liga": Liga o LED no pino 13.
    "desliga": Desliga o LED no pino 13.
    "liga dois": Liga o LED no pino 12.
    "desliga dois": Desliga o LED no pino 12.

Contribuições

Este projeto está aberto a contribuições e melhorias. Sinta-se à vontade para abrir issues ou enviar pull requests!
Licença

Este projeto está licenciado sob a licença MIT.
