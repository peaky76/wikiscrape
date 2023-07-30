from bs4 import BeautifulSoup


class Wikitable:
    def __init__(self, table):
        self.table = table

    @property
    def headers(self):
        return [th.text.strip() for th in self.table.find_all("th")]

    @property
    def data(self):
        return [
            [td.text.strip() for td in tr.find_all("td")]
            for tr in self.table.find_all("tr")
            if not tr.th
        ]
