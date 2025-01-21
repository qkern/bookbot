text_path_to_read = "books/frankenstein.txt"

def main():
    text = open_text_file(text_path_to_read)
    word_count = word_counter(text)
    alpha_count = alpha_counter(text)
    alpha_count_sorted = sort_dictionary(alpha_count)
    print_header(word_count)
    print_report(alpha_count_sorted)
    print_footer()

def open_text_file(text):
    with open(text) as f:
        return f.read()
        
def word_counter(text):
    split_string = text.split()
    word_count = len(split_string)
    return word_count

def alpha_counter(text):
    char_count_dict = {}
    for char in text.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        elif char.isalpha():
            char_count_dict[char] = 1 
    return char_count_dict    

def sort_dictionary(dictionary):
    temp = list_of_dicts(dictionary)
    temp.sort(key=lambda x: list(x.values())[0], reverse=True)
    return temp

def list_of_dicts(t):
    temp_list = []
    for key, value in t.items():
        temp_dict = {key:value}
        temp_list.append(temp_dict)
    return (temp_list)

def print_header(word_count):
    print(f""" --- Begin report of {text_path_to_read} --- \n{word_count} words found in the document\n""")

def print_report(char_count_dict):
    for char_count in char_count_dict:
        for char in char_count:
            print(f"The '{char}' character was found {char_count[char]} times")

def print_footer():
    print (" --- End report --- ")

main()