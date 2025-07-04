from stats import count_words
from stats import count_charaters
from stats import sort_characters
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_contents = get_book_text(sys.argv[1])
    character_count = count_charaters(book_contents)
    sorted_charaters = sort_characters(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_contents)} total words")
    print("--------- Character Count -------")
    for i in sorted_charaters:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents
    

main()