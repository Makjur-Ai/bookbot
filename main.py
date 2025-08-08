def get_book_text():
    with open("books/frankenstein.txt") as f: 
        text = f.read()
    return text

from stats import get_num_words

def main():
    book_text = get_book_text()
    print(get_num_words(book_text))

main()
