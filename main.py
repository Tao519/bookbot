import sys
from stats import get_num_words, uniques, report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    unique_chars = uniques(text)
    new_report = report(text)
    pretty_report = formatted_report(new_report)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
""")
    pretty_report = formatted_report(new_report)
    print("""
============= END ===============
          """)

def get_book_text(filepath):
      with open(filepath) as f:
          return f.read()

def formatted_report(stuff):
    for item in stuff:
        print(f"{item['char']}: {item['num']}")

main()
