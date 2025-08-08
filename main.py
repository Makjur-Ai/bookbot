def get_book_text():
    with open("/home/kevin/workspace/github.com/makjur-ai/bookbot/books/frankenstein.txt") as f: 
        text = f.read()
    return text

def main():
    print(get_book_text())

main()
