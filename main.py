def main():
    #import the system module
    import sys

    #Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #import the different functions
    from stats import num_words
    from stats import letter_count
    from stats import report
    
    #path varaible from the second argument
    path = sys.argv[1]

    #wourd count string
    string_print = f"{num_words(path)} words found in the document"
    #print(string_print)

    #dictionary of the letter count
    letter_dict = letter_count(path)
    
    #report format
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(path)} total words")
    print("--------- Character Count -------")
    report(letter_dict)
    print("============= END ===============")



main()