from stats import get_num_words, get_character_count, sort_char_list
import sys

if len(sys.argv) <2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
path = sys.argv[1]
    


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content




def main():
    sentence  = get_book_text(path)
    count = get_num_words(sentence)
    char = get_character_count(sentence)
    sort_list = sort_char_list(char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sort_list:
        for k, v in item.items():
            if k.isalpha():
                print(f"{k}: {v}")
    print("============= END ===============")
    
main()