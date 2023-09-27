from bs4 import BeautifulSoup

class Wikiobject:
    _html_tag: str = None
    _identifier: dict[str, str] = {}

    def __init__(cls, _):
        raise NotImplementedError(f"Wikiobject should not be created directly")

    @classmethod
    def from_html(cls, html: str):
        soup = BeautifulSoup(html, "html.parser")
        return cls.from_soup(soup)

    @classmethod
    def from_soup(cls, soup: BeautifulSoup):
        return cls(soup.find(cls._html_tag, cls._identifier))
