# Calling the counter module to keep track of instances of a word

from collections import Counter
import re

checkfile = input("Please enter the absolute pathway to the file (/home/user/directory/file.txt):")

with open (checkfile, "r") as f:
    contents = f.read() #Read the file first, otherwise it creates a TypeError
    stopwordsout = re.sub(r"\b[a-zA-Z]{1,3}\b", "", contents) #Regex for finding three letter words (the, a, in, out, so, how, are, is etc.)
    splitcontents = stopwordsout.split()
    print ("Word distribution is as follows:")
    print (Counter (splitcontents))

# Test code

# for line in open("microservices.txt", "r"): #A for loop that iterates over each line
#   for word in line.split (): # It then runs a line.split operator for each word

#      print(Counter)  #print the number of words counted.

# Resources

# https://pymotw.com/2/collections/counter.html
# https://stackoverflow.com/questions/15083119/python-find-the-occurrence-of-the-word-in-a-file

# todo
# Take out stop words:
# Determiners, Prepositions, coordinating conjuctions, and Pronouns.

