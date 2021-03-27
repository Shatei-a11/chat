import time
from socket import *

host = gethostname()
port = 7011

so = socket(AF_INET, SOCK_STREAM)

so.connect((host, port))
nome = input("Digite seu nome: ")
while True:
        mensagem_enviar = input("Digite uma mensagem: ")

        so.send(nome.encode())
        time.sleep(2)
        so.send(mensagem_enviar.encode())

        print("Mensagem enviada")
