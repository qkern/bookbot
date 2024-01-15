def main():
    file_location = "books/frankenstein.txt"
    book = copy_book(file_location)
    words = word_count(book)
    letters = letter_count(book)
    sorted_letters = letter_sort(letters)

    print(f"--- Begin report of {file_location} ---")
    print(f"There are {words} found in the document <br>")
    

    
def copy_book(file_location):
    with open(file_location) as file:
        file_contents = file.read()
    return file_contents

def word_count(file_contents):
    return len(file_contents.split())

def letter_count(book):
    letters = {}
    for char in book.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def letter_sort(letters):
    return 


main()
