from bs4 import BeautifulSoup

from wikiscrape import LinkedText

LINK_AND_TEXT = BeautifulSoup(
    "<a href='https://www.alink.com'>Foobar</a>", "html.parser"
)
BOLD_LINK_AND_TEXT = BeautifulSoup(
    "<b><a href='https://www.alink.com'>Foobar</a></b>", "html.parser"
)
TEXT_ONLY = BeautifulSoup("Foobar", "html.parser")
NAVIGABLE_STRING = BeautifulSoup("Foobar", "html.parser").string


def test_linked_text_init_with_link():
    assert LinkedText(LINK_AND_TEXT)


def test_linked_text_init_with_bold_link():
    assert LinkedText(BOLD_LINK_AND_TEXT)


def test_linked_text_init_without_link():
    assert LinkedText(TEXT_ONLY)


def test_linked_text_init_with_navigable_string():
    assert LinkedText(NAVIGABLE_STRING)


def test_linked_text_eq_with_link():
    assert LinkedText(LINK_AND_TEXT) == LinkedText(BOLD_LINK_AND_TEXT)


def test_linked_text_hash_with_link():
    assert hash(LinkedText(LINK_AND_TEXT)) == hash(LinkedText(BOLD_LINK_AND_TEXT))


def test_linked_text_repr_with_link():
    expected = "<LinkedText: Foobar (https://www.alink.com)>"
    assert repr(LinkedText(LINK_AND_TEXT)) == expected


def test_linked_bold_text_repr_with_link():
    expected = "<LinkedText: Foobar (https://www.alink.com)>"
    assert repr(LinkedText(BOLD_LINK_AND_TEXT)) == expected


def test_linked_text_repr_without_link():
    assert repr(LinkedText(TEXT_ONLY)) == "<LinkedText: Foobar (None)>"


def test_linked_text_repr_with_navigable_string():
    assert repr(LinkedText(NAVIGABLE_STRING)) == "<LinkedText: Foobar (None)>"


def test_linked_text_link_with_link():
    assert LinkedText(LINK_AND_TEXT).link == "https://www.alink.com"


def test_linked_text_link_with_bold_link():
    assert LinkedText(BOLD_LINK_AND_TEXT).link == "https://www.alink.com"


def test_linked_text_link_without_link():
    assert LinkedText(TEXT_ONLY).link is None


def test_linked_text_link_with_navigable_string():
    assert LinkedText(NAVIGABLE_STRING).link is None


def test_linked_text_text_with_link():
    assert LinkedText(LINK_AND_TEXT).text == "Foobar"


def test_linked_text_text_with_bold_link():
    assert LinkedText(BOLD_LINK_AND_TEXT).text == "Foobar"


def test_linked_text_text_without_link():
    assert LinkedText(TEXT_ONLY).text == "Foobar"


def test_linked_text_text_with_navigable_string():
    assert LinkedText(NAVIGABLE_STRING).text == "Foobar"
