from bs4 import BeautifulSoup
from wikiscrape import Infobox

HTML = """
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
                    <th>Website</th>
                    <td><a href="https://johndoe.com">johndoe.com</a></td>
                </tr>
            </tbody>
        </table>
    """

TABLE = BeautifulSoup(HTML, "html.parser").table


def test_infobox_headers():
    assert Infobox(TABLE).headers == ["Name", "Birthdate", "Website"]


def test_infobox_data():
    assert Infobox(TABLE).data == [
        "John Doe",
        "1 August 1950",
        BeautifulSoup(
            "<a href='https://johndoe.com'>johndoe.com</a>", "html.parser"
        ).contents[0],
    ]


def test_infobox_to_dicts():
    assert Infobox(TABLE).to_dicts() == [
        {
            "Name": "John Doe",
            "Birthdate": "1 August 1950",
            "Website": BeautifulSoup(
                "<a href='https://johndoe.com'>johndoe.com</a>", "html.parser"
            ).contents[0],
        }
    ]
