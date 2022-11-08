from collections import defaultdict

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

def sort_dict(dictionary):
    temp = sorted(dictionary.items(), key=lambda x:x[1], reverse=False)
    return {key:value for (key, value) in temp}

def word_count(lista):
    # create an empty dictionary
    repetitions = defaultdict(int)

    #count how many times a word come up on the list
    for word in lista: 
        repetitions[word] += 1
        
    return sort_dict(repetitions)

def word_probability(dictionary): 
    total = sum(dictionary.values())
    return {item[0]:item[1]/total for item in dictionary.items()}

def display_histogram(dictionary, ratio=100):
    total = sum(dictionary.values())
    for item in dictionary.items(): 
        prob = round(item[1]/total*ratio)
        if prob >= 1:
            temp = "#"*prob
            print(f"{item[0] :15} {item[1] :6} \t {item[1]/total :.3%} {temp}")

# test
prueba={"A":3, "B":1, "C":4}
for item in prueba.items():
    print(item[1])
for item in prueba.items():
    print(item)

word_probability(prueba)




'''
# test function: 

def word_count2 (lista):
    # create an empty dictionary
    repetitions = {}

    #count how many times a word come up on the list
    for word in lista: 
        try:
            repetitions[word] += 1
        except KeyError:
            repetitions[word] = 1
    
    return repetitions
'''

'''
# test function:
def word_probability2(dictionary):
    total = sum(dictionary.values())
    dictionary2 ={}
    for key in dictionary:
        dictionary2[key] = dictionary[key]/total
    return dictionary2
'''