import discum
import requests
import time
import random
import os
import threading
file = open("users.txt", "r")
tokens = open("tokens.txt", "r")
message = ""
message2 = ""
message3 = ""
message4 = ""
message5 = ""
def generateMessage():
    messageTemp = ""
    for line in file:
        line = line.strip()
        messageTemp += "<@" + line + ">"
    print(messageTemp)
def spammer(token):
    bot = discum.Client(token=token)
    while True:
        bot.sendMessage("channelIDHere", message)
        bot.sendMessage("", message)
        bot.sendMessage("", message)
        bot.sendMessage("", message2)
        bot.sendMessage("", message2)
        bot.sendMessage("", message2)
        bot.sendMessage("", message3)
        bot.sendMessage("", message3)
        bot.sendMessage("", message3)
        bot.sendMessage("", message4)
        bot.sendMessage("", message4)
        bot.sendMessage("", message4)
        bot.sendMessage("", message5)
        bot.sendMessage("", message5)
        bot.sendMessage("", message5)
def raid():
    for line in tokens:
        tokenTemp = line.strip()
        thread = threading.Thread(target=spammer, args=(tokenTemp,))
        thread.start()
#generateMessage()
#raid()
