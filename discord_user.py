import requests, json

class user:
    def __init__(self, token: str) -> None:
        self.data = {"Authorization": token}

    def type(self, channel: str) -> int:
        r = requests.post(f"https://discord.com/api/v9/channels/{channel}/typing", headers=self.data)
        return r

    def send_message(self, channel: str, message: str) -> int:
        json = {"content": message, "tts": False, "flags": 0}

        r = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers=self.data, json=json)
        return r
    
    def get_messages(self, channel: str, limit: int=1) -> list:
        r = requests.get(f"https://discord.com/api/v9/channels/{channel}/messages?limit={limit}", headers=self.data).content

        messages: list = json.loads(r)
        
        return messages

if __name__ == "__main__":
    user_input = input("Enter UUID:\n> ")
    testing = user(user_input)
    messages = testing.get_messages("800401182392713267", limit=10)
    messages.reverse()
    for x in messages:
        print(f"[{x['author']['username']}]: {x['content']}")