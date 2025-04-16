def get_num_words(string):
    string_list = string.split()
    count = len(string_list)
    return count 

def get_character_count(text):
    char_dict = {}
    char_list = list(text.lower())
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

