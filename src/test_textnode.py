import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node), "This is a text node")

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(\"This is a text node\", TextType.BOLD)")

    def test_get_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.get_text(), "This is a text node")

    def test_get_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.get_type(), TextType.BOLD)

    def test_set_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node.set_text("This is a new text node")
        self.assertEqual(node.get_text(), "This is a new text node")

    def test_set_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node.set_type(TextType.ITALIC)
        self.assertEqual(node.get_type(), TextType.ITALIC)

    def test_get_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertEqual(node.get_url(), "https://example.com")

    def test_set_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node.set_url("https://example.com")
        self.assertEqual(node.get_url(), "https://example.com")

if __name__ == '__main__':
    unittest.main()
