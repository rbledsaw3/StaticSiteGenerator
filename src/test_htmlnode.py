import unittest
from htmlnode import HTMLNode

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

"""
    def test_to_html(self):
        node = HTMLNode(
                "a",
                "Click me",
                None,
                { "href": "https://boot.dev" },
        )
        self.assertEqual(
                node.to_html(),
                '<a href="https://boot.dev">Click me</a>',
        )

    def test_to_html_no_props(self):
        node = HTMLNode(
                "p",
                "I'm a paragraph",
        )
        self.assertEqual(
                node.to_html(),
                "<p>I'm a paragraph</p>",
        )

    def test_to_html_no_children(self):
        node = HTMLNode(
                "div",
                "I'm a div",
        )
        self.assertEqual(
                node.to_html(),
                "<div>I'm a div</div>",
        )

    def test_to_html_children(self):
        node = HTMLNode(
                "div",
                None,
                [
                    HTMLNode("p", "I'm a paragraph"),
                    HTMLNode("p", "I'm another paragraph"),
                ],
        )
        self.assertEqual(
                node.to_html(),
                "<div><p>I'm a paragraph</p><p>I'm another paragraph</p></div>",
        )

    def test_to_html_nested_children(self):
        node = HTMLNode(
                "div",
                None,
                [
                    HTMLNode(
                        "div",
                        None,
                        [
                            HTMLNode("p", "I'm a paragraph"),
                            HTMLNode("p", "I'm another paragraph"),
                        ],
                    ),
                    HTMLNode("p", "I'm a paragraph"),
                ],
        )
        self.assertEqual(
                node.to_html(),
                "<div><div><p>I'm a paragraph</p><p>I'm another paragraph</p></div><p>I'm a paragraph</p></div>",
        )
"""

if __name__ == "__main__":
    unittest.main()
