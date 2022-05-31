import requests

class Joiner:
    def __init__(join):
        join.tokens = ["token 1", "token 2", "token 3"]
        invite = input("Enter the Discord Invitation: ex AV4E2Rz5  >> ")
        join.joiner()

    def joiner(join) -> None:
        for i, token in enumerate(join.tokens):

            headers = {
                'authority': 'discord.com',
                'content-length': '0',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMzNjQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijc4MDIyMjg1MzUwNDk1ODQ5NSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI3ODc3ODI2MTYyNTM0NjQ1NzYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                'authorization': token,
                'accept-language': 'fr',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                'accept': '*/*',
                'origin': 'https://discord.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://discord.com/channels/^@me',
            }

            resp = requests.post(f'https://discord.com/api/v9/invites/{invite}', headers=headers)

            if resp.status_code == 200:
                print(f"[{i}] JOINED SERVER - {token}")
            else:
                print(f"[{i}] JOINED SERVER FAIL - {token}")

        print(f"\n[!] Finished Joining the server with {len(join.tokens)}")

Join = Joiner()
Join.joiner()
