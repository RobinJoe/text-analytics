# Adapted code for analysing specific set of sentences.

'''def find_longest_sentence(sentence_list):
    sentence_len = []
    for n in sentence_list:
        sentence_len.append((len(n), n))
    sentence_len.sort()
    return sentence_len[-1][1]

print(find_longest_sentence(["Hi there friendo.", "It has already been done.", "The fox ran."]))'''


def find_longest_sentence(): #Set up the function
    with open ("microservices.txt", "r") as f: #Open the file and read it
        sentence_len = [] # specify an empty variable
        for n in f: # start the for loop
            sentence_len.append((len(n), n)) # todo find out what these are for
            sentence_len.sort()
        return sentence_len[-1][1]

print(find_longest_sentence()) #Close the for loop and print the results

# Todo
# At the moment, this returns the longest paragraph, not the longest sentence. It stops and starts
# breaking down the sentece when it encounters whitespace.
# Adjust the analysis to stop counting a sentence when it encounters a
# full stop "."

# .endswith(".") ?

# Resources
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-8.php
# https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
# https://www.w3schools.com/python/ref_string_endswith.asp

