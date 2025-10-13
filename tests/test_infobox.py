from bs4 import BeautifulSoup

from wikiscrape import Infobox

BASIC_HTML = """
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

BASIC_INFOBOX = Infobox.from_html(BASIC_HTML)

STACKED_HTML = """
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
                </tr>
                <tr>
                    <td>1 August 1950</td>
                </tr>
            </tbody>
        </table>
    """

STACKED_INFOBOX = Infobox.from_html(STACKED_HTML)

HEADED_HTML = """
        <table class="some_other_table">
        </table>
        <table class="infobox">
            <tbody>
                <tr>
                    <th>John Doe</th>
                </tr>
                <tr>
                    <th>Name</th>
                    <td>John Doe</td>
                </tr>
                <tr>
                    <th>Birthdate</th>
                    <td>1 August 1950</td>
                </tr>
            </tbody>
        </table>
    """

HEADED_INFOBOX = Infobox.from_html(HEADED_HTML)


def test_infobox_headers():
    assert BASIC_INFOBOX.headers == ["Name", "Birthdate", "Websites"]


def test_infobox_data():
    assert BASIC_INFOBOX.data == [
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
    assert BASIC_INFOBOX.to_dicts() == [
        {
            "Name": "John Doe",
            "Birthdate": "1 August 1950",
            "Websites": BeautifulSoup(
                "<a href='https://johndoe.com'>johndoe.com</a> and <a href='https://anothersite.com'>anothersite.com</a>",
                "html.parser",
            ),
        }
    ]


def test_infobox_headers_when_stacked():
    assert STACKED_INFOBOX.headers == ["Name", "Birthdate"]


def test_infobox_data_when_stacked():
    assert STACKED_INFOBOX.data == [
        [
            "John Doe",
            "1 August 1950",
        ]
    ]


def test_infobox_to_dicts_when_stacked():
    assert STACKED_INFOBOX.to_dicts() == [
        {
            "Name": "John Doe",
            "Birthdate": "1 August 1950",
        }
    ]


def test_infobox_headers_when_headed():
    assert HEADED_INFOBOX.headers == ["John Doe", "Name", "Birthdate"]


def test_infobox_data_when_headed():
    assert HEADED_INFOBOX.data == [
        [
            None,
            "John Doe",
            "1 August 1950",
        ]
    ]


def test_infobox_to_dicts_when_headed():
    assert HEADED_INFOBOX.to_dicts() == [
        {
            "John Doe": None,
            "Name": "John Doe",
            "Birthdate": "1 August 1950",
        }
    ]
