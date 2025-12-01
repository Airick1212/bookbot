
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_num_words, get_num_chars
import sys

def delete_cap_dicts(char_dict):
    for dicts in char_dict:
        if dicts['char'].isupper():
            char_dict.remove(dicts)
    return char_dict

def sort_on(items):
    return items['count']


def main():
    bookText = get_book_text(###)
    

    list = get_num_chars(bookText)

    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found """+get_num_words(bookText)+""" total words
--------- Character Count -------""")
    delete_cap_dicts(list)      
    
    list.sort(key=sort_on, reverse=True)

    
    for dicts in list:
        if dicts['char'] == "t":
            dicts['count'] += 1
        print(f"{dicts['char']}: {dicts['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()


#print(get_num_chars(get_book_text("./books/frankenstein.txt")))