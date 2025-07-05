import sys
from stats import get_word_count, get_char_count

def main(): 
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_contents = get_book_text(book_path)
    print("----------- Word Count ----------")
    get_word_count(book_contents)
    print("--------- Character Count -------")
    get_char_count(book_contents)
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()