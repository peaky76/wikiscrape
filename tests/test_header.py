from wikiscrape.header import Header


def test_header_text():
    html = """
        <div>
            <h2>Header 1</h2>
        </div>
    """
    assert Header.from_html(html).text == "Header 1"
