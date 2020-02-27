# phrase2acronym.py
#
# A program to convert phrases to acronyms.
# Input is a string, output is a string.
# Except, the function to construct a string from a list doesn't work,
# So it currently outputs a list.
#
# Michael M. Hansen, ITC 110 Winter 2020
# 19 February 2020
#

from string import *

# def listToString(inputList):
#    tempString = ""
#    j = 0
#   for j in range(len(inputList)):
#        tempString = tempString + inputList[j]
#       j += 1
#    tempString

def main():
    print("This program converts phrases to acronyms.")
    phraseString = input("Please enter a phrase: ")
    phraseList = phraseString.split()   # split the string into a list of strings, at spaces
    acronymList = []                    # intialize acronymList
    i = 0                               # zero-out iteration counter
    sizeOfPhraseList = len(phraseList)
    for i in range(sizeOfPhraseList) :    # loop over phraseList, building acronymList
        phraseElement = phraseList[i]
        acronymList.append(phraseElement[0])
        i += 1
    
    # acronymString = listToString(acronymList)    # convert acronymList from a list of strings to a string
    # print(acronymString)
    print(acronymList)

main()

# String solution: 
# acronym = ""
#    for word in phrase.split():
#        acronym = acronym+word[0]
#    acronym = acronym.upper()
# Ava Meredith , Feb 23 at 6:33pm
