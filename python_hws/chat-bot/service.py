class Bot:
    version = "1.0.0"

    def __init__(self, name):
        self.name = name
    
    def replyTo(self, message):
        self.message = "Hello!"

import requests
class BotGPT(Bot):
    def __init__(self, name, gpt_key):
        super().__init__(name)
        self.gpt = gpt_key
    
    def replyTo(self, message):
        headers = {"Autorization": f"Bearer {self.gpt_key}"}
        json = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Say this is a test!"}],
            "temperature": 0.7
        }
        res = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers = headers,
            json = json
        )
        print(res.status_code)
        print(res.content)
