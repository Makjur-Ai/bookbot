def get_num_words(text):
    num_words = len(text.split(None, -1))
    return f"{num_words} words found in the document."