import urllib.request
import requests
import bs4 as bs
from matplotlib import pyplot as plt

#empty lists for making a data frame
stats = ['HP', 'Attack', 'Defense', 'Sp.Attack', 'Sp.Defense', 'Speed']
basestats = []

#Collect name from user
name = input("Welcome to the Pokemon Base Stat Viewer. Please enter a Pokemon name (lower case: pikachu, meowth, etc):")
print("Looking up " + name + "...")

#Send a request to the website with the target name included
html = requests.get("https://www.serebii.net/pokedex-swsh/" + name)
soup = bs.BeautifulSoup(html.content, 'html.parser')


# When BeautifulSoup scrapes the web page, the table where serebii
# stores the base stats changes. It is 4 less than the xpath number (eg 21 xpath becomes 17 soup index number).
# This input asks the user to change the int inside the [] to adjust the table index of the soup.
# TODO - create a better way to calculate the soup table index, or iterate through the soup table 
# data to find the right table index.
# Note: It is unclear if this works for some legendary pokemon.

table_xpath = int(input("""Enter the stat table number, which is usually 15. It can be 
between 12 - 20 depending on the base stats of the target pokemon. Try different
numbers from 12 to 20 if you recieve an "index out of range" error until the bar chart 
appears:
"""))

#Run a find all method on the table index number input
table = soup.findAll('table', class_='dextable')[table_xpath].get_text()

#Split the results into a list to access the index numbers
#Append the index values to the empty list set up earlier
table_list = table.strip("'").split()

basestats.append(int((table_list[14])))
basestats.append(int((table_list[15])))
basestats.append(int((table_list[16])))
basestats.append(int((table_list[17])))
basestats.append(int((table_list[18])))
basestats.append(int((table_list[19])))

# Make the Bar chart

plt.style.use('fivethirtyeight')

plt.bar(stats, basestats)

plt.title(name + " base stats")
plt.xlabel("Stat names")
plt.ylabel("Stat values")

plt.ylim(0,255)

# This code  came from StackOverflow - it labels the bars with the number from the base stats variable.
# https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
for index,data in enumerate(basestats):
    plt.text(x=index , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=16))

plt.tight_layout

plt.savefig(name + '_basestats.svg')
