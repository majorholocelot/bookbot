def count_words(file_contents):
    word_count = len(file_contents.split())

    return word_count


def count_char(file_contents):
    clean_book_txt = file_contents.lower()
    char_dict = {}

    for char in clean_book_txt:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

# In stats.py
def sort_on(dict):
    return dict["num"]

def sort_chars(char_dict):
    # Convert dictionary to list of dictionaries
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Sort the list
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

  

