
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_num_words, get_num_chars

def main():
    bookText = get_book_text("./books/frankenstein.txt")
    print(f"Found {get_num_words(bookText)} total words.")
    
    list = get_num_chars(bookText)

    for key, value in list.items():
        print("'" + key + "'" + ": " + str(value))

if __name__ == "__main__":
    main()

#print(get_num_chars(get_book_text("./books/frankenstein.txt")))