import socket 
import os
import sys
import random
import time
from icmplib import ping, multiping, traceroute, resolve, Host, Hop
from colored import fg, bg, attr

name = "Tamara-PC"

black = fg('#000000')
red = fg('#ff0000') 
white = fg('#ffffff')
green = fg('#63ff00')
res = attr('reset')


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
print(red + "Empfange Zahl, bitte warten..." + res)
print(green + "Zahl erfolgreich Empfangen!" + res)
print("Warte auf Eingabe von Spieler 1...")
print("")
usr = s.recv(1024)
usr = usr.decode()
print(green + "Nutzer erfolgreich Registiert: ", usr , " --SPIELER 1")





usr2 = input(str("Spieler 2, bitte geben sie ihren Nutzernamen ein>>>"))
print(green + "Nutzer erfolgreich Registiert: ", usr2 , + res + " --SPIELER 2")
usr2 = usr2.encode()
usr = s.send(usr2)

print("Zahlen Erraten (Version 1.0)")
print("")
print("Spieler 1: ",usr)
print("")
print("Spieler 2: ",usr2)



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

    







