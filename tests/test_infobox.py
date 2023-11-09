from bs4 import BeautifulSoup

from wikiscrape import Infobox

HTML = """
        <table class="some_other_table">
        </table>
        <table class="infobox">
            <tbody>
                <tr>
                    <img src="https://johndoe.com/johndoe.jpg" />
                </tr>
                <tr>
                    <th>Name</th>
                    <td>John Doe</td>
                </tr>
                <tr>
                    <th>Birthdate</th>
                    <td>1 August 1950</td>
                </tr>
                <tr>
                    <th>Websites</th>
                    <td><a href="https://johndoe.com">johndoe.com</a> and <a href="https://anothersite.com">anothersite.com</a></td>
                </tr>
            </tbody>
        </table>
    """

INFOBOX = Infobox.from_html(HTML)


def test_infobox_headers():
    assert INFOBOX.headers == ["Name", "Birthdate", "Websites"]


def test_infobox_data():
    assert INFOBOX.data == [
        [
            "John Doe",
            "1 August 1950",
            BeautifulSoup(
                "<a href='https://johndoe.com'>johndoe.com</a> and <a href='https://anothersite.com'>anothersite.com</a>",
                "html.parser",
            ),
        ]
    ]


def test_infobox_to_dicts():
    assert INFOBOX.to_dicts() == [
        {
            "Name": "John Doe",
            "Birthdate": "1 August 1950",
            "Websites": BeautifulSoup(
                "<a href='https://johndoe.com'>johndoe.com</a> and <a href='https://anothersite.com'>anothersite.com</a>",
                "html.parser",
            ),
        }
    ]
