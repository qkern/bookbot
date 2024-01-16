def main():
    file_location = "books/frankenstein.txt"
    text = copy_book(file_location)
    words = word_count(text)
    letters = letter_count(text)
    sorted_letters = letter_sort(letters)

    print(f"--- Begin report of {file_location} ---")
    print(f"There are {words} found in the document <br>")
    print("")
    print_letter_usage(sorted_letters)
    

    
def copy_book(file_location):
    with open(file_location) as file:
        text = file.read()
    return text

def word_count(text):
    return len(text.split())

def letter_count(text):
    letters = {}
    for char in text.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def letter_sort(letters):
    letters_lst = list(letters.items())
    return sorted(letters_lst, key= lambda letters_lst: letters_lst[1], reverse = True)

def print_letter_usage(sorted_letters):
    for letter in sorted_letters:
        if letter[0].isalpha():
            print(f"The '{letter[0]}' character was found {letter[1]} times")

main()
