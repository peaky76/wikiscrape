from bs4 import BeautifulSoup

from wikiscrape import Coordinates

HTML = """
    <div id="mw-indicator-coordinates" class="mw-indicator">
        <div class="mw-parser-output">
            <span id="coordinates">
                <a href="/wiki/Geographic_coordinate_system" title="Geographic coordinate system">
                    Coordinates
                </a>: 
                <style data-mw-deduplicate="TemplateStyles:r1156832818">.mw-parser-output .geo-default,.mw-parser-output .geo-dms,.mw-parser-output .geo-dec{display:inline}.mw-parser-output .geo-nondefault,.mw-parser-output .geo-multi-punct,.mw-parser-output .geo-inline-hidden{display:none}.mw-parser-output .longitude,.mw-parser-output .latitude{white-space:nowrap}</style><span class="plainlinks nourlexpansion">
                    <a class="external text" href="https://geohack.toolforge.org/geohack.php?pagename=Leicester_Racecourse&amp;params=52_35_52_N_1_5_45_W_type:landmark_scale:10000_region:GB">
                        <span class="geo-default">
                            <span class="geo-dms" title="Maps, aerial photos, and other data for this location">
                                <span class="latitude">52°35′52″N</span> 
                                <span class="longitude">1°5′45″W</span>
                            </span>
                        </span>
                        <span class="geo-multi-punct">&#xfeff; / &#xfeff;</span>
                        <span class="geo-nondefault">
                            <span class="geo-dec" title="Maps, aerial photos, and other data for this location">52.59778°N 1.09583°W</span>
                            <span style="display:none">&#xfeff; / 
                                <span class="geo">52.59778; -1.09583</span>
                            </span>
                        </span>
                    </a>
                    </span>
                </span>
            </div>
        </div>
	</div>
"""


def test_coordinates_from_soup():
    coords = Coordinates.from_soup(BeautifulSoup(HTML, "html.parser"))
    assert coords.value


def test_coordinates_from_html():
    coords = Coordinates.from_html(HTML)
    assert coords.value


def test_coordinates_returns_correct_latitude_when_present():
    coords = Coordinates.from_soup(BeautifulSoup(HTML, "html.parser"))
    assert coords.latitude == "52°35′52″N"


def test_coordinates_returns_no_latitude_when_not_present():
    coords = Coordinates.from_soup(
        BeautifulSoup("<span>No coordinates here</span", "html.parser")
    )
    assert coords.latitude is None


def test_coordinates_returns_correct_longitude_when_present():
    coords = Coordinates.from_soup(BeautifulSoup(HTML, "html.parser"))
    assert coords.longitude == "1°5′45″W"


def test_coordinates_returns_no_longitude_when_not_present():
    coords = Coordinates.from_soup(
        BeautifulSoup("<span>No coordinates here</span", "html.parser")
    )
    assert coords.longitude is None
