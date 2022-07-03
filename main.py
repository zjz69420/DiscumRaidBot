import discum
import requests
import time
import random
import os
import threading
tokens = open("tokens.txt", "r")
file = open("users.txt", "r")
channels = open("channels.txt", "r")
messageSpamArr = []
def generateMessage():
    messageLength = 0
    currentMessage = 0
    for line in file:
        line = line.strip()
        if messageLength == 0:
            messageSpamArr.append("<@" + line + ">")
        else:
            messageSpamArr[currentMessage] += "<@" + line + ">"
        messageLength += 21
        if messageLength >= 1995:
            currentMessage += 1
            messageLength = 0
    for message in messageSpamArr:
        print(message + '\n')



def spammer(token, channelID, message):
    bot = discum.Client(token=token)
    while True:
        time.sleep(random.uniform(10, 15))
        bot.sendMessage(channelID, message)
def raid():
    for token in tokens:
        token = token.strip()
        for channel in channels:
            channel = channel.strip()
            for message in messageSpamArr:
                thread = threading.Thread(target=spammer, args=(token, channel, message))
                thread.start()
generateMessage()
raid()
