def num_words(book_words):
    book_list = book_words.split()
    chars_dict = {}
    chars = book_words.lower()
    lower_chars = list(chars)
    for char in lower_chars:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return len(book_list), chars_dict

def sort_on(items):
    return items["num"]

def dict_list(dict):
    list_dict = []
    for key, value in dict.items():
        list_dict.append({"char": key, "num": value})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict



