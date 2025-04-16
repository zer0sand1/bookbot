from stats import get_num_words, get_character_count



def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content




def main():
    sentence  = get_book_text("books/frankenstein.txt")
    count = get_num_words(sentence)
    char = get_character_count(sentence)
    print(f"{count} words found in the document")
    print(char)
main()