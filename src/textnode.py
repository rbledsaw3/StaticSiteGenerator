from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        if self.url is None:
            return f"TextNode(\"{self.text}\", {self.text_type})"
        else:
            return f"TextNode(\"{self.text}\", {self.text_type}, {self.url})"

    def __str__(self):
        return self.text

    def get_text(self):
        return self.text

    def get_type(self):
        return self.text_type

    def set_text(self, text):
        self.text = text

    def set_type(self, text_type):
        self.text_type = text_type

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url
