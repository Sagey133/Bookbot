from stats import num_words
from stats import dict_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_words = get_book_text("frankenstein.txt")
    print (f"{num_words(book_words)} words found in the document")

main()


   
