import requests
import time,random

def array_gen():
    global array
    for arr in range(10):
        array.append(int(random.randint(0, 100)))


author = input("authorization : ")
channelID = input("channelID : ")
n = int(input("How many times do you want to spam ? : "))
array = []
temp_array = []

str1 = 'https://discord.com/api/v9/channels/'
str2 = '/messages'
str_all = str1 +channelID+ str2


header = {
    'authorization': author
}

for i in range(n):
    array_gen()
    temp_array = str(array)
    payload = {
    'content':temp_array
    }
    
    r = requests.post(str_all, data=payload, headers=header)
    time.sleep(random.randint(1, 5))
    array = []

print("finish spam!!!")
