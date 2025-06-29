def get_book_text(filepath):
    if type(filepath) != str:
        return "wrong type, must use string for path"
    else:
        print(f"Analyzing book found at {filepath}...")
        with open(filepath, encoding="utf-8") as f:
            data = f.read()
            letters = list(data.lower())
            letter_count = {}
            print(f"Found {len(letters) + 1} total words")
            for letter in letters:
                if letter.isalpha():
                    if letter in letter_count.keys():
                        letter_count[letter] += 1
                    if letter not in letter_count.keys():
                        letter_count.update({f"{letter}": 1})
            sorted_items = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
            sorted_dictionary_asc = dict(sorted_items)
            print("------------------ Character Count ----------------------")
            for letter, count in sorted_dictionary_asc.items():
                print(f"{letter.upper()}: {count}")
            print("------------------------ END ----------------------------")
def main():
    print("====================== BOOKBOT ==========================")
    get_book_text("books/frankenstein.txt")
    return

main()
