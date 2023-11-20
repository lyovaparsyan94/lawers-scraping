import g4f
from time import sleep


class ChatGPT:
    def __init__(self):
        g4f.debug.logging = True

    @staticmethod
    def process(content: str):
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": content}],
        )
        return response

    def run(self, content: str, retry=5, interval=5):
        response = None
        while not response and retry >= 1:
            try:
                response = self.process(content=content)
            except Exception as e:
                print(e)
                retry -= 1
                sleep(interval)
                print(f"Retrying {5 - retry} time to run chatgpt  after {interval} seconds interval")
        return response
