from stats import get_num_words
from stats import get_num_type_letters

def get_book_text(path="books/frankenstein.txt"):
    with open(path) as f: 
        text = f.read()
    return text

def main():
    book_text = get_book_text()
    letter_dict = get_num_type_letters(book_text)
    print(get_num_words(book_text))
    print(letter_dict)


main()
