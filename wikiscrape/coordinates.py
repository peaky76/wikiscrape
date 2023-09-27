from bs4 import BeautifulSoup
from .wikiobject import Wikiobject

class Coordinates(Wikiobject):
    _html_tag = "span"
    _identifier = {"class": "geo-dms"}

    def __init__(self, coords):
        self.coords = coords

    @property
    def latitude(self):
        return self.coords.find("span", {"class": "latitude"}).text if self.coords else None

    @property
    def longitude(self):
        return self.coords.find("span", {"class": "longitude"}).text if self.coords else None