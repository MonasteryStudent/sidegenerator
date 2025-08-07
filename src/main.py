from textnode import TextType, TextNode

def main():
    text = "This is some anchor text"
    text_type = TextType.LINK
    url = "https://www.boots.dev"
    dummy = TextNode(text, text_type, url)
    print(dummy)

if __name__ == "__main__":
    main()