import sys
from stats import word_count, char_count, sorted_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
# getting character counts from the book text
    char_counts = char_count(book_text)
#sorting the character counts
    sorted_char_counts = sorted_dict(char_counts)
#formatting the character counts
    print("Usage: python3 main.py <path_to_book>")
    print(f"Analyzing books found at {book_path}...")
    print(f"Found {word_count(book_text)} total words")
    print(sorted_char_counts)

main()