def only_letters(string):
    '''
    filters only alphabetical characters
    '''
    temp = ""
    for letter in string:
        if letter.isalpha():
            temp = temp + letter
        else:
            temp = temp + " "
    return temp

def normalize (string, stop_words): 
    '''
    input: text string
    output: list of words within the string that don't match any stop words
    '''
    # filter only the alphabetical characters. 
    temp = only_letters(string)
    #convert to list of words. 
    temp = temp.lower().split()

    #return filtered list. 
    return [word for word in temp if word not in stop_words]



#open text file and stopwords list. 
# with is a function that opens and closes the file object once the work is done. 
# temp=open("alice_text.txt", "r")
# alice_text = temp.readlines()
# temp.close()

with open("alice_text.txt") as temp:
    alice_text = temp.read()
with open("english.txt") as temp: 
    stop_words = temp.read()



#filter the book text (delete the Gutemberg header and footer)
alice_text = alice_text[alice_text.index("CHAPTER I.\n"):alice_text.index("END OF THE PROJECT GUTENBERG EBOOK")]
alice_text_test = alice_text[4000:6000] #for testing purposes
stop_words = set(stop_words.split())

alice_filtered = normalize(alice_text_test, stop_words)



#write it in a text file, for clarity. 
with open("alice_text_processed.txt", "w") as temp:
    temp.write(alice_text)