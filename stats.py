from main import get_book_text

def word_count(main):
    text = main(get_book_text)
    words = text.split()
    print(f"Found {len(words)} total words")