from textnode import TextNode, TextType


def main():
    new = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(new)

if __name__ == "__main__":
    main()

