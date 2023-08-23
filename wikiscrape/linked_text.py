class LinkedText:
    def __init__(self, content):
        self.content = content

    @property
    def link(self):
        return link["href"] if (link := self.content.a) else None

    @property
    def text(self):
        return self.content.text.strip()
