import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import num_words

from stats import dict_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
word_count, chars_dict = num_words(get_book_text(sys.argv[1]))
sorted_chars = dict_list(chars_dict)

print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")

for dict in sorted_chars:
    if dict["char"].isalpha():
        print(f"{dict['char']}: {dict['num']}")








