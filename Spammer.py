import requests, json, os, time

class Spammer:
    """ Discord Message Spammer (multi-token) """
    def __init__(spam):
        spam.tokens = ["token 1", "token 2", "token 3"]
        spam.message = input("Message to Send    -> ")
        spam.channel = input("Channel ID to Spam -> ")
        spam.amount  = input("Amount of Messages ->")

        spam.servurl = f'https://discord.com/api/v9/channels/{spam.channelid}/messages'
        spam.headers = {"authorization": token, "Content-Type": 'application/json'}
        spam.payload = {"content": f"{spam.message}"}

    def spammer(spam) -> None:
        for i in range(int(spam.amount)):
            for token in spam.tokens:
                req = requests.post(
                    spam.servurl,
                    headers=spam.headers,
                    data=json.dumps(spam.payload)
                )
                if req.status_code != 200:
                    print(f"[x] Error Encountered")
                else:
                    print(f"[{i}] Message Sent!")

Spam = Spammer()
Spam.spammer()
