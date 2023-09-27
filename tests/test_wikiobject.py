import pytest
from bs4 import BeautifulSoup
from wikiscrape import Wikiobject


def test_wikiobject_init_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        Wikiobject("foobar")


def test_wikiobject_subclass_does_not_raise_not_implemented_error():
    class WikiobjectSubclass(Wikiobject):
        _html_tag = "div"

    assert WikiobjectSubclass("foobar")


def test_wikiobject_from_html_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        Wikiobject.from_html("<div>Some content</div")


def test_wikiobject_from_soup_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        Wikiobject.from_soup(BeautifulSoup("<div>Some content</div>", "html.parser"))
