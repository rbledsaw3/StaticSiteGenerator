import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
                "div",
                "Hello, world!",
                None,
                {
                    "class": "greeting",
                    "href": "https://boot.dev"
                },
        )
        self.assertEqual(
                node.props_to_html(),
                ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
                "div",
                "I wish I could read",
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode(
                "p",
                "What a strange world",
                None,
                { "class": "primary" },
        )
        self.assertEqual(
                repr(node),
                "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
       )

    def test_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_nested(self):
        node = HTMLNode(
                "div",
                None,
                [
                    LeafNode("p", "Hello, world!"),
                    LeafNode("p", "Goodbye, world!"),
                ],
        )
        self.assertEqual(
                node.to_html(),
                "<div><p>Hello, world!</p><p>Goodbye, world!</p></div>",
        )

    def test_to_html_no_children(self):
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = HTMLNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_no_props(self):
        node = HTMLNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_to_html_no_props_or_children(self):
        node = HTMLNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_leaf_node(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_leaf_node_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_node_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
