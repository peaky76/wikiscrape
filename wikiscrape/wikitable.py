from bs4 import BeautifulSoup


class Wikitable:
    def __init__(self, table):
        self.table = table

    @property
    def headers(self):
        return [th.text.strip() for th in self.table.find_all("th")]
