def get_num_words(text):
    num_words = len(text.split(None, -1))
    print(num_words)

def get_num_type_letters(text):
    letter = text.lower()
    characters = {}
    for char in letter:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_key(char):
    return char["num"]

def sort_dictionary(characters):
    sorted_chars = []
    for char, num in characters.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": num})
    
    sorted_chars.sort(reverse=True, key=sort_key)

    return sorted_chars
