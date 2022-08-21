"""
File created on Fri May 28 18:57:01 2021

@author: Quentin Mertens
"""
import datetime
import json
import glob
import os

folder_name = input("Enter the name of the folder: ")

file = os.path.abspath("reader.py")
file = os.path.dirname(file)
file = file+"\\"+folder_name

fileCounter = len(glob.glob1(file,"*.json"))

f = open(file+"\message_1.json","r")
data = json.load(f)
a = len(data["participants"])
counter = [0]*(a+1)
last = ""

for file_iteration in range(1,fileCounter+1):
    
    f = open(file+"\message_"+str(file_iteration)+".json","r")
    
    data = json.load(f)
    
    for message in data["messages"]:
        if message["timestamp_ms"] == last or message['type'] != "Generic":
            pass
        else:
            last = message["timestamp_ms"]
            counter[0] += 1
            for i in range(a):
                if message["sender_name"] == data["participants"][i]["name"]:
                    counter[i+1] += 1
                
    if file_iteration == 1:
        dernier = datetime.datetime.fromtimestamp(data["messages"][0]["timestamp_ms"]//1000.0)
        sender = data["messages"][0]["sender_name"]
print()
print("Premier message :" + str(datetime.datetime.fromtimestamp(data["messages"][-1]["timestamp_ms"]//1000.0)) + " envoyé par " + str(data["messages"][-1]["sender_name"]))
print("Dernier message :" + str(dernier) + " envoyé par " + str(sender))

dic = {}
for i in range(a):
    dic[data["participants"][i]["name"]] = counter[i+1]
dic = list(sorted(dic.items(), key=lambda x: x[1], reverse=True))
print()

print("Place     nb msg      nom")
for i in range(a):
	print("{:>5} avec{:>6} :   {}".format(i+1,dic[i][1],dic[i][0]))
print("Total:{:>10}".format(counter[0]))