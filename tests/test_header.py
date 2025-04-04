from wikiscrape.header import Header


def test_header_text():
    html = """
        <div>
            <h2>Header 1</h2>
        </div>
    """
    assert Header.from_html(html).text == "Header 1"


def test_header_text_when_highly_styled():
    html = """
        <div class="mw-heading mw-heading2">
            <h2 id="Background">Background</h2>
            <span class="mw-editsection">
                <span class="mw-editsection-bracket">[</span>
                <a href="/w/index.php?title=1982_British_Army_Gazelle_friendly_fire_incident&amp;action=edit&amp;section=1" title="Edit section: Background">edit</a>
                <span class="mw-editsection-bracket">]</span>
            </span>
        </div>
    """
    assert Header.from_html(html).text == "Background"
