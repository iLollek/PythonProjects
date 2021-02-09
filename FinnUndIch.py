import socket 
import os
import sys
import random
import time
from icmplib import ping, multiping, traceroute, resolve, Host, Hop
from colored import fg, bg, attr

name = "Tamara-PC"


s = socket.socket()
host = socket.gethostname()
port = 8082
s.bind((host,port))
s.connect((name, port))
print("Erfolgreich Verbunden!")

# Hier bauen wir das spiel

print("Sie spielen jetzt das Zahlen erraten Spiel")

zahl1 = s.recv(1024)
zahl1 = zahl1.decode()

print("Bitte erraten sie die Zahl, sie sind Spieler 2")
print(zahl1)
while 1:
    rate1 = s.recv(1024)
    rate1 = rate1.decode()
    print(rate1)
    if rate1 == zahl1:
        print("Spieler 1 hat gewonnen!")
        msg = "Spieler 1 hat gewonnen!"
        msg = msg.encode()
        msg = s.send(msg)
        break
    elif rate1 < zahl1:
        print("Größer!")
        msg = "Größer!"
        msg = msg.encode()
        msg = s.send(msg)
    elif rate1 > zahl1:
        print("Kleiner!")
        msg = "Kleiner!"
        msg = msg.encode()
        msg = s.send(msg)
    
    rate2 = input(str("Zahl>>>"))

    if rate2 == zahl1:
        print("Spieler 2 hat gewonnen!")
        msg = "Spieler 2 hat gewonnen!"
        msg = msg.encode()
        msg = s.send(msg)
        break
    elif rate2 < zahl1:
        print("Größer!")
        msg = "Größer!"
        msg = msg.encode()
        msg = s.send(msg)
    elif rate2 > zahl1:
        print("Kleiner!")
        msg = "Kleiner!"
        msg = msg.encode()
        msg = s.send(msg)

    rate2 = rate2.encode()
    rate2 = s.send(rate2)

print("Dies ist ein Test")
print("Und noch einer")
    







