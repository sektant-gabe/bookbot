def get_word_count(filepath):
    with open(filepath, encoding="utf-8") as f:
        data = f.read()
        words = data.split()
        return words

def get_chars_count(filepath):
    with open(filepath, encoding="utf-8") as f:
        data = f.read()
        letters = list(data.lower())
        letter_count = {}
        for letter in letters:
            if letter.isalpha():
                if letter in letter_count.keys():
                    letter_count[letter] += 1
                if letter not in letter_count.keys():
                    letter_count.update({f"{letter}": 1})
    return letter_count

def sort_chars(chars):
    sorted_by_value = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    return sorted_by_value
