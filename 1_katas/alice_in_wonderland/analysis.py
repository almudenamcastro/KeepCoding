from functions import *

# open text file and stopwords list. 
with open("alice_text.txt") as temp:
    alice_text = temp.read()
with open("english.txt") as temp: 
    stop_words = temp.read()

# create set from stop_words string. 
stop_words = set(stop_words.split())
# filter the book text (delete the Gutemberg header and footer)
alice_text = alice_text[alice_text.index("CHAPTER I.\n"):alice_text.index("END OF THE PROJECT GUTENBERG EBOOK")]
# alice_text_test = alice_text[4000:6000] #for testing purposes

# normalize text and convert to word list
alice_filtered = normalize(alice_text, stop_words)

# create a dictionary with the word count
alice_word_count = word_count(alice_filtered)

#write it in a text file, for clarity. 
with open("alice_text_processed.txt", "w") as temp:
    for item in alice_word_count.items():
        temp.write(f"{item[0] :15} {item[1]}\n")

# analize word probability based on dict data
alice_word_prob = word_probability(alice_word_count)

# display histogram
display_histogram(alice_word_count, ratio=1000)

