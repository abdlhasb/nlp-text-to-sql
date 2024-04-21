import requests
import time
import os
from openai import OpenAI

class GPT:
    def __init__(self, keys=None):
        self._key = None

    def __call__(self, prompt, *args, **kwargs):
        client = OpenAI(
            organization='Your-Organization-Id',
            project='Your-Project-Id',
            api_key='Your-Api-Key')
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # engine = "deployment_name".
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0,
            max_tokens=200)

        time.sleep(25)
        try:
            print(f"prompt: {prompt}")
            print(f"result: {response['choices'][0]['message']['content']}")
            return response['choices'][0]['message']['content']
        except:
            time.sleep(30)
            response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # engine = "deployment_name".
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0,
            max_tokens=200)
            print(f"prompt: {prompt}")
            print(f"result: {response['choices'][0]['message']['content']}")
            return response['choices'][0]['message']['content']


if __name__ == '__main__':
    llm = GPT()
    print(llm('请用一句话解释万有引力'))