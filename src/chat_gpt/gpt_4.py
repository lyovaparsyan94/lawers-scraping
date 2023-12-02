import time

import g4f
from time import sleep


class ChatGPT:
    def __init__(self):
        g4f.debug.logging = True

    @staticmethod
    def process(content: str):
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4_0613,
            messages=[{"role": "user", "content": content}],
        )
        return response

    def run(self, content: str, retry=5, interval=5):
        start = time.time()
        response = None
        while not response and retry >= 1:
            try:
                response = self.process(content=content)
                print("The response has been received and is being processed. 🤖")
            except Exception as e:
                print(e)
                retry -= 1
                sleep(interval)
                print(f"Retrying {5 - retry} time to run chatgpt  after {interval} seconds interval")
        end = time.time()
        print(f"Execution time of the program is {end - start} seconds")
        return response
