class LinkedText:
    def __init__(self, text):
        self.text = text

    @property
    def link(self):
        return link["href"] if (link := self.text.a) else None
