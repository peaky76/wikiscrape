from bs4 import BeautifulSoup
from wikiscrape import Wikipage


def test_wikipage_eq_true():
    assert Wikipage("Joe Bloggs") == Wikipage("Joe Bloggs")


def test_wikipage_eq_false():
    assert Wikipage("Joe Bloggs") != Wikipage("Jane Doe")


def test_wikipage_abs_url():
    assert Wikipage("Joe Bloggs").abs_url == "https://en.wikipedia.org/wiki/Joe_Bloggs"


def test_wikipage_rel_url():
    assert Wikipage("Joe Bloggs").rel_url == "Joe_Bloggs"


def test_wikipage_rel_url_with_apostrophe():
    assert (
        Wikipage("Fillies' And Mares' Stakes").rel_url
        == "Fillies%27_And_Mares%27_Stakes"
    )


def test_wikipage_is_disambiguated_true():
    assert Wikipage("Joe Bloggs (American jockey)").is_disambiguated


def test_wikipage_is_disambiguated_false_for_canonical_page():
    assert not Wikipage("Joe Bloggs").is_disambiguated


def test_wikipage_is_disambiguated_false_for_redlink():
    assert not Wikipage("Joe Bloggs (page does not exist").is_disambiguated


def test_wikipage_is_redlink_true():
    assert Wikipage("Braveheart Stakes (page does not exist)").is_redlink


def test_wikipage_is_redlink_false():
    assert not Wikipage("Joe Bloggs").is_redlink


def test_wikipage_soup(requests_mock):
    requests_mock.get(
        "https://en.wikipedia.org/wiki/Joe_Bloggs", text="<!DOCTYPE html>..."
    )
    assert isinstance(Wikipage("Joe Bloggs").soup, BeautifulSoup)


def test_wikipage_subject():
    assert Wikipage("Joe Bloggs (jockey)").subject == "Joe Bloggs"


def test_wikipage_text(requests_mock):
    requests_mock.get(
        "https://en.wikipedia.org/wiki/Joe_Bloggs", text="<!DOCTYPE html>..."
    )
    assert Wikipage("Joe Bloggs").text.startswith("<!DOCTYPE html>")


def test_wikipage_to_link():
    assert Wikipage("Joe Bloggs").to_link() == "[[Joe Bloggs]]"


def test_wikipage_to_link_with_alias():
    assert Wikipage("Joe Bloggs").to_link("J-Blogz") == "[[Joe Bloggs|J-Blogz]]"
