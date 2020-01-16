import requests
from random import choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("DAD jokes Collection!") #since entire module is imported; we had to use "figlety_format" as a method 
header = colored(header, color ="magenta") #since only needed method is imported; we can use it directly...same with "choice"
print(header)
user_input = input("What would like to search for? ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()
# response = requests.get(url)
# data = response.json()
num_jokes = len(response["results"])
result = response["results"]

if num_jokes == 0:
    print("Sorry! Couldn't find any jokes on {}".format(user_input))
elif num_jokes == 1:
    print("Only found 1 joke on {}".format(user_input))
    print(choice(result)["joke"])
elif num_jokes > 1:
    print("I found {} jokes on {}".format(num_jokes, user_input))
    print(choice(result)["joke"])


