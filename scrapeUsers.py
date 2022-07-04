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


def spammer(token, channelID, message, sleep):
    bot = discum.Client(token=token)
    while True:
        time.sleep(random.uniform(sleep + 5, sleep - 5))
        bot.sendMessage(channelID, message)


def raid(sleepTime):
    for token in tokens:
        token = token.strip()
        print(token)
        for channel in channels:
            channel = channel.strip()
            print(channel)
            for message in messageSpamArr:
                print(message)
                thread = threading.Thread(target=spammer, args=(token, channel, message, sleepTime))
                thread.start()
generateMessage()
channelCount = len(channels.readlines())
print(channelCount)
messageCount = len(messageSpamArr)
print(messageCount)
sleepTiming = messageCount * channelCount * 2
if sleepTiming < 5:
    sleepTiming = 6
print(sleepTiming)
raid(sleepTiming)
