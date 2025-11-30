def get_num_words(bookText):
    words = bookText.split()
    return len(words)

def get_num_chars(bookText):
    num_cars_dict = {}
    for char in bookText:
        if char.isalpha():
            if char.lower() == " ":
                pass
            if char.lower() in num_cars_dict:
                num_cars_dict[char.lower()] += 1
            else:
                num_cars_dict[char.lower()] = 1
    num_cars_dict = dict(sorted(num_cars_dict.items()))
    return num_cars_dict
