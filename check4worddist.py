# Calling the counter module to keep track of instances of a word

from collections import Counter

checkfile = input("Please enter the absolute pathway to the file (/home/user/directory/file.txt):")

with open (checkfile, "r") as f:
    contents = f.read().split()
    print ("Word distribution is as follows")
    print (Counter (contents))


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

