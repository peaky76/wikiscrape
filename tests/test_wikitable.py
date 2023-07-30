from bs4 import BeautifulSoup
from wikiscrape import Wikitable


def test_wikitable_headers():
    html = "<table><tr><th>Header 1</th><th>Header 2</th></tr></table>"
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).headers == ["Header 1", "Header 2"]
