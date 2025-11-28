
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_num_words

def main():
    bookText = get_book_text("./books/frankenstein.txt")
    print(f"Found {get_num_words(bookText)} total words.")

if __name__ == "__main__":
    main()