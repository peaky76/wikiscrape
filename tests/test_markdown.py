from wikiscrape import Markdown as md  # noqa: N813


def test_markdown_a_without_alias():
    assert md.a("page") == "[[page]]"


def test_markdown_a_with_alias():
    assert md.a("page", "alias") == "[[page|alias]]"


def test_markdown_b():
    assert md.b("text") == "'''text'''"


def test_markdown_em():
    assert md.em("text") == "''text''"


def test_markdown_h():
    assert md.h(1, "text") == "==text=="


def test_markdown_ul():
    assert md.ul(["item1", "item2"]) == "* item1\n* item2"


def test_markdown_br():
    assert md.br() == "<br/>"


def test_markdown_hr():
    assert md.hr() == "\n----\n"


def test_markdown_comment():
    assert md.comment("text") == "<!-- text -->"


def test_markdown_template():
    assert md.template("content") == "{{content}}"
