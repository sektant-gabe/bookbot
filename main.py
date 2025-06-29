from stats import get_word_count, get_chars_count, sort_chars
from sys import argv, exit


if len(argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

def get_book_text(filepath):
    if type(filepath) != str:
        return "wrong type, must use string for path"
    else:
        print(f"Analyzing book found at {filepath}...")
        print("------------------ Word Count ----------------------")
        print(f"Found {len(get_word_count(filepath))} total words")
        print("------------------ Character Count ----------------------")
        chars_count = {}
        chars_count = get_chars_count(filepath)
        sorted_chars = sort_chars(chars_count)

        for letter, count in sorted_chars.items():
            print(f"{letter}: {count}")
        print("------------------------ END ----------------------------")

def main():
    print("====================== BOOKBOT ==========================")
    get_book_text(argv[1])
    return
main()
