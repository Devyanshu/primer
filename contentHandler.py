import os
import requests 


class ContentHandler():
    def __init__(self, file):
        self.file = file
        self.url = "https://api.github.com/markdown"

    def open_md(self):
        with open(self.file) as mdfile:
            md = mdfile.read()
        return md


    def get_HTML(self):
        data = {'text': self.open_md(),
                "mode": "markdown",
                "context": "github/primer"
        }
        response = requests.post(url = self.url, json = data) 
        return response.text


if __name__ == "__main__":
    ch = ContentHandler('Python/lambda.md')
    print(ch.get_HTML())
    