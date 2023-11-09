from bs4 import BeautifulSoup

from wikiscrape import Wikitable
from wikiscrape.wikitable import remove_footnotes


def test_remove_footnotes_removes_square_brackets():
    assert remove_footnotes("Hello [World]") == "Hello"


def test_remove_footnotes_removes_dagger():
    assert remove_footnotes("Hello World\u2020") == "Hello World"


def test_remove_footnotes_removes_double_dagger():
    assert remove_footnotes("Hello World\u2021") == "Hello World"


def test_wikitable_from_title():
    html = """
        <h2>Table A</h2>
        <table>
            <tr>
                <th>Header 1A</th>
                <th>Header 2A</th>
            </tr>
        </table>
        <h2>Table B</h2>
        <table>
            <tr>
                <th>Header 1B</th>
                <th>Header 2B</th>
            </tr>
        </table>
    """
    table = Wikitable.from_title("Table B", html)
    assert table.headers == ["Header 1B", "Header 2B"]


def test_wikitable_headers():
    html = "<table><tr><th>Header 1</th><th>Header 2</th></tr></table>"
    table = Wikitable.from_html(html)
    assert table.headers == ["Header 1", "Header 2"]


def test_wikitable_headers_with_new_lines_at_beginning():
    html = "<table><tr><th>\n<span>Header 1</span></th><th>Header 2</th></tr></table>"
    table = Wikitable.from_html(html)
    assert table.headers == ["Header 1", "Header 2"]


def test_wikitable_headers_with_new_lines_at_end():
    html = "<table><tr><th>Header 1</th><th>Header 2\n</th></tr></table>"
    table = Wikitable.from_html(html)
    assert table.headers == ["Header 1", "Header 2"]


def test_wikitable_headers_with_empty_header():
    html = "<table><tr><th></th><th>Header 2</th></tr></table>"
    table = Wikitable.from_html(html)
    assert table.headers == ["", "Header 2"]


def test_wikitable_headers_when_headers_are_not_labelled():
    html = """
        <table>
            <tr><td></td><td>Header 2</td></tr>
            <tr><td>Data 1</td><td>Data 2</td>
        </table>
    """
    table = Wikitable.from_html(html)
    assert table.headers == ["col_1", "col_2"]


def test_wikitable_data():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td>Data A1</td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td>Data B2</td></tr>
        </table>
    """
    table = Wikitable.from_html(html)
    assert table.data == [["Data A1", "Data A2"], ["Data B1", "Data B2"]]


def test_wikitable_data_handles_footnotes():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td>Data A1[a]</td><td>Data A2‡</td></tr>
            <tr><td>Data B1</td><td>Data B2</td></tr>
        </table>
    """
    table = Wikitable.from_html(html)
    assert table.data == [["Data A1", "Data A2"], ["Data B1", "Data B2"]]


def test_wikitable_data_handles_ampersands():
    html = """
        <table>
            <tr><th>Header 1[a]</th><th>Header 2</th></tr>
            <tr><td>Data A1</td><td>Data A2&A3</td></tr>
            <tr><td>Data B1</td><td>Data B2</td></tr>
        </table>
    """
    table = Wikitable.from_html(html)
    assert table.data == [["Data A1", "Data A2&A3"], ["Data B1", "Data B2"]]


def test_wikitable_data_handles_links():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td><a href='http://www.dataa1.com'>Data A1</a></td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td><a href='http://www.datab2.com'>Data B2</a></td></tr>
        </table>
    """
    table = Wikitable.from_html(html)
    assert table.data[0][0]["href"] == "http://www.dataa1.com"


def test_wikitable_data_handles_blanks():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td></td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td>\n</td></tr>
        </table>
    """
    table = Wikitable.from_html(html)
    assert table.data


def test_wikitable_data_handles_links_with_footnotes():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td><a href='http://www.dataa1.com'>Data A1‡</a></td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td><a href='http://www.datab2.com'>Data B2</a></td></tr>
        </table>
    """
    table = Wikitable.from_html(html)
    assert table.data[0][0]["href"] == "http://www.dataa1.com"
    assert table.data[0][0].text == "Data A1"


def test_wikitable_data_handles_multiple_elements():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td><a href='http://www.dataa1.com'>Data A1</a> <a href='http://www.dataaa1.com'>Data AA1</a></td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td><a href='http://www.datab2.com'>Data B2</a></td></tr>
        </table>
    """
    table = Wikitable.from_html(html)
    expected = BeautifulSoup(
        "<a href='http://www.dataa1.com'>Data A1</a> <a href='http://www.dataaa1.com'>Data AA1</a>",
        "html.parser",
    )
    assert table.data[0][0] == expected


def test_wikitable_to_dicts():
    html = """
        <table>
            <tr><th>Header 1</th><th>Header 2</th></tr>
            <tr><td>Data A1</td><td>Data A2</td></tr>
            <tr><td>Data B1</td><td>Data B2</td></tr>
        </table>
    """
    table = Wikitable.from_html(html)
    assert table.headers == ["Header 1", "Header 2"]
    assert table.data == [["Data A1", "Data A2"], ["Data B1", "Data B2"]]
    assert table.to_dicts() == [
        {"Header 1": "Data A1", "Header 2": "Data A2"},
        {"Header 1": "Data B1", "Header 2": "Data B2"},
    ]
