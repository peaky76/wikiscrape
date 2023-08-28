from bs4 import BeautifulSoup

from .wikitable import Wikitable


class Infobox(Wikitable):
    @property
    def data(self) -> list[BeautifulSoup]:
        return [
            contents[0]
            if len(contents := tr.td.contents) == 1
            else BeautifulSoup("".join(str(x) for x in contents), "html.parser")
            for tr in self.table.find_all("tr")
            if tr.th
        ]

    def to_dicts(self) -> list[dict[BeautifulSoup, BeautifulSoup]]:
        return [dict(zip(self.headers, self.data))]