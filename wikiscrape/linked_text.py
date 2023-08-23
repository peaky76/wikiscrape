class LinkedText:
    def __init__(self, content):
        self.content = content

    @property
    def link(self):
        anchor = self.content.a
        return anchor["href"] if anchor else None

    @property
    def text(self):
        return self.content.text.strip()
