def get_num_words(bookText):
    words = bookText.split()
    return len(words)

def sort_on(items):
    return items[1]

""" def get_num_chars(bookText):
    num_chars_dict = {}
    for char in bookText:
        if char.isalpha():
            if char.lower() == " ":
                pass
            if char.lower() in num_chars_dict:
                num_chars_dict[char.lower()] += 1
            else:
                num_chars_dict[char.lower()] = 1
    #num_cars_dict = dict(sorted(num_cars_dict.items()))
    #num_chars_dict.sort(key=sort_on)
    return num_chars_dict """

def get_num_chars(bookText):
    num_chars_dict = {}
    for char in bookText:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in num_chars_dict:
                num_chars_dict[lower_char] += 1
            else:
                num_chars_dict[lower_char] = 1
    # Sort by value (frequency) descending and return a dict that preserves order
    num_chars_dict = dict(sorted(num_chars_dict.items(), key=lambda item: item[1], reverse=True))
    return num_chars_dict




