def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(book_path):
    with open(book_path, "r") as f:
        return f.read()

main()