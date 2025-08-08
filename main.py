def get_book_text():
    with open("/home/kevin/workspace/github.com/makjur-ai/bookbot/books/frankenstein.txt") as f: 
        text = f.read()
        num_words = len(text.split(None, -1))
    return f"{num_words} words found in the document."

def main():
    print(get_book_text())

main()
