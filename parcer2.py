from bs4 import BeautifulSoup
import requests


class Parcer:
    text = ''
    def __init__(self, url='https://ru.wikipedia.org/wiki/Винегрет'):
        self.url = url

    def get_html(self):
        r = requests.get(self.url).content
        self.soup = BeautifulSoup(r, "lxml")
        return self.soup

    def get_text_from_html(self):
        for child in self.soup.children:
            try:
                if child.get_text():
                    self.text += child.get_text()
                else:
                    get_text_from_html(child)
            except Exception:
                pass
    
    def save(self, path):
        with open(path, "wb") as f:
            f.flush()
            f.write(self.text.encode())

    def get_text(self,):
        return self.text

parcer = Parcer(r'https://ru.wikipedia.org/wiki/Сигара')
parcer.get_html()
parcer.get_text_from_html()
print(parcer.get_text())
parcer.save(r'C:\Users\salim\GetFiles\parcer4.txt')
