from stats import word_count

def get_book_text(file_path):
    with open(file_path) as f:
        content =  f.read()
    return content

def main(get_book_text):
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    return book_text

word_count(main)