from stats import get_num_words
from stats import get_num_type_letters
from stats import sort_dictionary

def header_book_count(path, book_text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")

def character_count(letter_dict):
    print("--------- Character Count -------")
    sorted_char_list = sort_dictionary(letter_dict)
    for item_dict in sorted_char_list:
        char = item_dict["char"]
        num = item_dict["num"]
        print(f"{char}: {num}")



def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    letter_dict = get_num_type_letters(book_text)
    sorted_letters = sort_dictionary(letter_dict)
    header_book_count(book_path, book_text)
    character_count(letter_dict)
      

def get_book_text(path):
    with open(path) as f: 
        text = f.read()
    return text

main()
