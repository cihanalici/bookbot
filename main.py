def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = len(text.split())
    # count letters
    counted_leteers = count_letters(text.lower())
    report(counted_leteers, words_count)

def get_book_text(book_path):
    with open(book_path, "r") as f:
        return f.read()

def count_letters(text):
    # Add a new function to your script that takes the text from the book as a string, and returns the number of times each character appears in the string. Convert any uppercase letters to lowercase letters, we don't want duplicates.
    letters = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def report(counted_letters, words_count):
    print(counted_letters.items())
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    for letter, count in counted_letters.items():
        print(f"The '{letter}' character was found {count} times")
    print(f"--- End report ---")


main()