def get_num_words(text):
    num_words = len(text.split(None, -1))
    return f"{num_words} words found in the document."

def get_num_type_letters(text):
  letter = text.lower()
  character = {}
  for char in letter:
     if char not in character:
        character[char] = 1
     else:
        character[char] += 1
  return character
  
