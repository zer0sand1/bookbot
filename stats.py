from operator import itemgetter


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




def sort_char_list(char_dict):
    char_list = []
    for k,v in char_dict.items():
        char_list.append({k: v})
    def value_of_dict(d):
        return list(d.values())[0]
    char_list.sort(key=value_of_dict, reverse=True)
    return char_list

