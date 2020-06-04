print("Thanks for Using this - Kratik")
# this comment is done only for testing purpose
import jsonzx
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif  w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0 :
        yn = input("Did You Mean  '%s'  instead ??? Enter y if YES or n for No -  " % get_close_matches(w,data.keys())[0])
        if yn == "y":
            print("\n%s" % get_close_matches(w,data.keys())[0])
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "The Word doesn't exist, Please Re-Check-it"
        else:
            return "You can enter only 'y' or 'n'(Case-Sensitive). "
    else:
        return "The Word doesn't exist, Please Re-Check-it"

#word = input("Enter A word:  ")
word = "mirage"
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

#input("\n\n\n\nPress ENTER to close window")
