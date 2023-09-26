from bs4 import BeautifulSoup

class Coordinates:

    def __init__(self, coords):
        self.coords = coords

    @classmethod
    def from_soup(cls, soup: BeautifulSoup):
        return cls(soup.find("span", {"class": "geo-dms"}))

    @classmethod
    def from_html(cls, html: str):
        return cls(BeautifulSoup(html, "html.parser").find("span", {"class": "geo-dms"}))

    @property
    def latitude(self):
        return self.coords.find("span", {"class": "latitude"}).text if self.coords else None

    @property
    def longitude(self):
        return self.coords.find("span", {"class": "longitude"}).text if self.coords else None