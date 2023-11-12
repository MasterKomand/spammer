
import os

try:
    from platform import platform
except:
    os.system("pip install platform")
    from platform import platform



puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]


if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'



os.system(delet)



def on_startup():
    print("<HackerRullerTools> Запуск!")
on_startup()

try:
    import requests
except:
    os.system("pip install requests")
    import requests
import time

try:
    from art import *
except:
    os.system("pip install art")
    from art import *

try:
    from pyrogram.errors import FloodWait
    from threading import Thread
    from pyrogram import Client, filters
except:
    os.system("pip install pyrogram")
    from pyrogram.errors import FloodWait
    from threading import Thread
    from pyrogram import Client, filters

from random import randrange
from time import sleep
import tracemalloc


def printtext(text):
    art1 = text2art(text)
    print(art1)
    time.sleep(1)


def printair(i):
    for l in range(i):
        time.sleep(0.6)
        print()

api_id = ''
api_hash = ''

tracemalloc.start()

def register():
    os.system(delet)
    printtext('HackSpam')
    try:
        global api_hash
        global api_id
        api_id = input('Введите api_id (если нету пропустите): ')
        if api_id == '':
            number = randrange(1000000)
            api_id = '222222'
        api_hash = input('Введите api_hash (если нету пропустите): ')
        if api_hash == '':
            api_hash == 'ddds'
    except:
        print('Неккоректно')
        time.sleep(3)
        register()

register()

api_id = api_id
api_hash = api_hash

arg1 = ''
arg2 = ''


tracemalloc.start()

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command('spam') & filters.me)
async def call(client, message):
    global args1
    global args2
    chatid = message.chat.id
    cmd = message.text
    try:
        arg1 = cmd.split(' ')
        arg1 = arg1[1]
        arg2 = cmd.split(maxsplit=2)[2]
    except IndexError:
        await client.send_message(chatid, "Извините, введите все аргументы верно!\n/spam (кол-во) (сообщение)")
    try:
        arg1 = str(arg1).replace("[", "").replace("]", "").replace(",", "")
        arg1 = int(arg1)
    except ValueError:
        await client.send_message(chatid, "Извините, но кол-во должно быть числом!\n\n/spam (кол-во) (сообщение)")
    for el in range(arg1):
        await client.send_message(chatid, f"Спам: {arg2}")
    


def end():
    os.system(delet)
    printtext('HackSpam')
    print("<HackerRullerTools> Запущен! Команда спама: /spam (кол-во сообщений) (сообщение)!\nНаш канал: https://t.me/HackeeRullerToolsOfficial\nНаш чат: https://t.me/HackerRullerTools")
end()
if __name__ == '__main__':
    app.run()
