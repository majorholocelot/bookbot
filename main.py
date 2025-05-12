import sys
from stats import count_words
from stats import count_char
from stats import sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]



def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()

    return file_contents

def main():
   book_txt = get_book_text(path_to_book)
   num_words = count_words(book_txt)
   char_count = count_char(book_txt)
   char_dict = count_char(book_txt)
   sorted_chars = sort_chars(char_dict)



   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count ----------")
   print(f"Found {num_words} total words")
   print("--------- Character Count -------")
   # Loop through the sorted list and print each character with its count
   for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")

        
    
   print("============= END ===============")


   #print(char_count) test complete


   #print(book_txt) test complete


main()