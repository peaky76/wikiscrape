from bs4 import BeautifulSoup
from wikiscrape import Wikitable


def test_wikitable_headers():
    html = "<table><tr><th>Header 1</th><th>Header 2</th></tr></table>"
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).headers == ["Header 1", "Header 2"]


def test_wikitable_data():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td>Data A1</td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td>Data B2</td></tr>
        </table>
    """
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).data == [["Data A1", "Data A2"], ["Data B1", "Data B2"]]
