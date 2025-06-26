def get_book_text(path):
    # file-path input.

    # return contents of the file as a string
    return path.read()

def num_words(path):
    #file-path input
    
    #isolate the text
    with open(path) as f:
        text = get_book_text(f)
    
    text_list = text.split()
    
    return len(text_list)

def letter_count(path):
    #isolate the text
    with open(path) as f:
        text = get_book_text(f).lower()
    
    #dictionary to store letter counts
    letter_dict ={}

    for char in text:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] = letter_dict[char] + 1
    
    return letter_dict
        
def report(letter_dict):
    new_letter_list = []

    for letter in letter_dict:
        new_letter_list.append(dict(char=letter,num=letter_dict[letter]))
    def sort_on(new_letter_list):
        return new_letter_list["num"]

    new_letter_list.sort(reverse=True, key=sort_on)

    for item in new_letter_list:
        char_letter = item["char"]
        num_count = item["num"]
        print(f"{char_letter}: {num_count}")
    

    
