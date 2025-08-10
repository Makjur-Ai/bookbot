def get_book_text():
    with open("books/frankenstein.txt") as f: 
        text = f.read()
    return text

from stats import get_num_words
from stats import get_num_type_letters
def main():
    book_text = get_book_text()
    letter_dict = get_num_type_letters(book_text)
    print(get_num_words(book_text))
    print(letter_dict)


main()
