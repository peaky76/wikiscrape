from bs4 import BeautifulSoup
from wikiscrape import Wikitable
from wikiscrape.wikitable import remove_footnotes


def test_remove_footnotes_removes_round_brackets():
    assert remove_footnotes("Hello (World)") == "Hello"


def test_remove_footnotes_removes_square_brackets():
    assert remove_footnotes("Hello [World]") == "Hello"


def test_remove_footnotes_removes_dagger():
    assert remove_footnotes("Hello World\u2020") == "Hello World"


def test_remove_footnotes_removes_double_dagger():
    assert remove_footnotes("Hello World\u2021") == "Hello World"


def test_wikitable_headers():
    html = "<table><tr><th>Header 1</th><th>Header 2</th></tr></table>"
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).headers == ["Header 1", "Header 2"]


def test_wikitable_headers_with_new_lines_at_beginning():
    html = "<table><tr><th>\n<span>Header 1</span></th><th>Header 2</th></tr></table>"
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).headers == ["Header 1", "Header 2"]


def test_wikitable_headers_with_new_lines_at_end():
    html = "<table><tr><th>Header 1</th><th>Header 2\n</th></tr></table>"
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


def test_wikitable_data_handles_footnotes():
    html = """
        <table>
            <tr><th>Header 1[a]</th><th>Header 2</th></tr>
            <tr><td>Data A1</td><td>Data A2‡</td></tr>
            <tr><td>Data B1</td><td>Data B2</td></tr>
        </table>
    """
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).data == [["Data A1", "Data A2"], ["Data B1", "Data B2"]]


def test_wikitable_data_handles_links():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td><a href='http://www.dataa1.com'>Data A1</a></td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td><a href='http://www.datab2.com'>Data B2</a></td></tr>
        </table>
    """
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).data[0][0]["href"] == "http://www.dataa1.com"


def test_wikitable_data_handles_blanks():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td></td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td>\n</td></tr>
        </table>
    """
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).data


def test_wikitable_data_handles_links_with_footnotes():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td><a href='http://www.dataa1.com'>Data A1‡</a></td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td><a href='http://www.datab2.com'>Data B2</a></td></tr>
        </table>
    """
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).data[0][0]["href"] == "http://www.dataa1.com"
    assert Wikitable(table).data[0][0].text == "Data A1"


def test_wikitable_data_handles_multiple_elements():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td><a href='http://www.dataa1.com'>Data A1</a> <a href='http://www.dataaa1.com'>Data AA1</a></td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td><a href='http://www.datab2.com'>Data B2</a></td></tr>
        </table>
    """
    table = BeautifulSoup(html, "html.parser").table
    expected = BeautifulSoup(
        "<a href='http://www.dataa1.com'>Data A1</a> <a href='http://www.dataaa1.com'>Data AA1</a>",
        "html.parser",
    )
    assert Wikitable(table).data[0][0] == expected


def test_wikitable_to_dicts():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td>Data A1</td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td>Data B2</td></tr>
        </table>
    """
    table = BeautifulSoup(html, "html.parser").table
    assert Wikitable(table).headers == ["Header 1", "Header 2"]
    assert Wikitable(table).data == [["Data A1", "Data A2"], ["Data B1", "Data B2"]]
    assert Wikitable(table).to_dicts() == [
        {"Header 1": "Data A1", "Header 2": "Data A2"},
        {"Header 1": "Data B1", "Header 2": "Data B2"},
    ]
