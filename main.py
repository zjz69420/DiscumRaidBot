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



def spammer(token, channelID, message, sleep):
    bot = discum.Client(token=token)
    while True:
        time.sleep(random.uniform(1, sleep))
        bot.sendMessage(channelID, message)
def raid(sleep):
    tokens.seek(0)
    for token in tokens:
        token = token.strip()
        channels.seek(0)
        for channel in channels:
            channel = channel.strip()
            for message in messageSpamArr:
                thread = threading.Thread(target=spammer, args=(token, channel, message, sleep))
                thread.start()
generateMessage()
channelCount = len(channels.readlines())
print(channelCount)
messageCount = len(messageSpamArr)
print(messageCount)
sleepTiming = messageCount * channelCount * 1.5
print(sleepTiming)
raid(sleepTiming)
