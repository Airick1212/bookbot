def get_num_words(bookText):
    words = bookText.split()
    return str(len(words))

def sort_on(items):
    return items[1]

def get_num_chars(bookText):
    num_chars_dict = []
    for index, char in enumerate(bookText):
        if char.isalpha():
            lower_char = char.lower()
            for dicts in num_chars_dict:
                if dicts['char'] == lower_char:
                    dicts['count'] += 1
                    break
            else:
                char_dict = {'char': char, 'count': 1}
                num_chars_dict.append(char_dict)
    # Sort by value (frequency) descending and return a dict that preserves order
    #num_chars_dict = dict(sorted(num_chars_dict.items(), key=lambda item: item[1], reverse=True))
    return num_chars_dict




