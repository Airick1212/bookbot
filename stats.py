def get_num_words(bookText):
    words = bookText.split()
    return len(words)

def get_num_chars(bookText):
    num_cars_dict = {}
    for char in bookText:
        if char == " ":
            continue
        if char.lower() in num_cars_dict:
            num_cars_dict[char.lower()] += 1
        else:
            num_cars_dict[char.lower()] = 1
    return num_cars_dict
