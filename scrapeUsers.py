import discum
import os
tokenInput = input("Enter your user token: ")
serverID = input("Input server id: ")
channelID = input("Input channel id: ")
client = discum.Client(token=tokenInput) 

def close_after_fetching(resp, guild_id):
    if client.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(client.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        client.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        client.gateway.close()

def get_members(guild_id, channel_id):
    client.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    client.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    client.gateway.run()
    client.gateway.resetSession()
    return client.gateway.session.guild(guild_id).members

members = get_members(serverID, channelID) #place the corresponding things
memberList = []
for memberID in members:
    memberList.append(memberID)
    print(memberID)

f = open('users.txt', "a")
for element in memberList:
    writeString = element
    f.write(writeString + "\n")
    print(writeString + "\n")

f.close()
