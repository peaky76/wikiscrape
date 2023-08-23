from bs4 import BeautifulSoup
from wikiscrape import LinkedText

LINK_AND_TEXT = "<a href='https://www.alink.com'>Foobar</a>"
TEXT_ONLY = "Foobar"


def test_linked_text_init_with_link():
    soup = BeautifulSoup(LINK_AND_TEXT, "html.parser")
    assert LinkedText(soup)


def test_linked_text_init_without_link():
    soup = BeautifulSoup(TEXT_ONLY, "html.parser")
    assert LinkedText(soup)


def test_linked_text_link_with_link():
    soup = BeautifulSoup(LINK_AND_TEXT, "html.parser")
    assert LinkedText(soup).link == "https://www.alink.com"


def test_linked_text_link_without_link():
    soup = BeautifulSoup(TEXT_ONLY, "html.parser")
    assert LinkedText(soup).link == None
