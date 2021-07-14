tokens = ["token 1", "token 2", "token 3"]

import requests
import json
import os
import time
import colorama

from colorama import Fore as f
colorama.init()

os.system('cls')

g = f.GREEN
r = f.RED
rst = f.RESET

msgnumb = 10

print()
print(f'{rst}[{g}+{rst}]{g} Message Content {r}')
msgtosend = input("  >> ")
print()
print(f'{rst}[{g}+{rst}]{g} Channel ID {r}')
channelid = input("  >> ")
print()

i = 0
j = 0

while i < int(msgnumb):

    if j < len(tokens):

        header = {"authorization": tokens[j], "Content-Type": 'application/json'}
        url = f'https://discord.com/api/v9/channels/{channelid}/messages'
        payload = {"content": f"{msgtosend}"}
        req = requests.post(url, headers=header, data=json.dumps(payload))
		
        if len(req.text) < 100:
            print(f"{rst}[{r}+{rst}]{r} ERROR | RATELIMIT OR INVALID TOKEN")
        else:
            print(f'{rst}[{g}+{rst}]{g} MESSAGE SENT')
        j = j + 1

    elif j == len(tokens):
        j = 0

    i += 1  
