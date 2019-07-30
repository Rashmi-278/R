import json
# import get_close_matches module to suggest the closest possible match of input word when word not in dictionary
#  PYTHON LIB DOCUMENTATIONS : https://docs.python.org/3/library/index.html #
from difflib import get_close_matches
# use with open syntax to open json file as f for proper usage of file ie to close automatially when done
with open("data.json") as f :
    data = json.load(f) #json.load() loads the json file as dictionary as data - dictionary name

#function to perform look up of word 
def translate(word):
	if word in data: # if word found in data
		for i in data[word]: # iterate through every defination of the word
			 	print("# "+i)
                print("")
    # get the most probable closest match for the entered wrong word
    # if the len of the returned list is greater than 0
	elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0: 
		suggestion = get_close_matches(word,data.keys())[0] #assign the first word as suggestion
		ans = input("Do you mean? {} Y/N".format(suggestion) ).lower() #ask for user confirmation , convert input to lower case
		if ans == 'y': #if y
			 for i in data[suggestion]: # iterate through every defination of the word
			 	print("# "+i)
                print("")
		else:
			print("We didnt understand your entry. Please try again.") #print this if wrong suggestion
	else:
			print("The word doesnt exist.Please double check it") #print this is no suggestions found


word = input("Enter word:").lower() #take input of the word to return defination

translate(word) #call function



#######use the below code snippet if any json encoding problems are encountered

'''
import json,sys
from difflib import get_close_matches

response_json = open("data.json").read()
data = {}
try:
    response_json = response_json.decode('utf-16').replace("\0", '')
    struct = json.loads(response_json)
except:
    print('bad json: ', response_json)



######   ANOTHER FUNCTION DEFINITION #######

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

'''
  