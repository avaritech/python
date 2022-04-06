#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#

def vanity(codes, numbers): #codes is an array of strings, numbers is an array of strings (numbers)
   #lettersToNumbersDict = {"A":"2","B":"2","C":"2",""}
   lettersToNumbersDict = dict.fromkeys(['A','B','C',],"2")
   lettersToNumbersDict.update(dict.fromkeys(['D','E','F'],"3"))
   lettersToNumbersDict.update(dict.fromkeys(['G','H','I'],"4"))
   lettersToNumbersDict.update(dict.fromkeys(['J','K','L'],"5"))
   lettersToNumbersDict.update(dict.fromkeys(['M','N','O'],"6"))
   lettersToNumbersDict.update(dict.fromkeys(['P','Q','R','S'],"7"))
   lettersToNumbersDict.update(dict.fromkeys(['T','U','V'],"8"))
   lettersToNumbersDict.update(dict.fromkeys(['W','X','Y','Z'],"9"))
   #lettersToNumbersDict = {"2":("A","B","C"),"3":("D","E","F"),"4":("G","H","I"),"5":("J","K","L")}
   #for key in lettersToNumbersDict.keys():
      # print(lettersToNumbersDict[key])
   matchingNumbers = []
   for codeWord in codes:
       codeNumberStr = ""
       for letter in list(codeWord):
           codeNumberStr += lettersToNumbersDict[letter]
           #print(lettersToNumbersDict[letter])
       #print(codeNumberStr)
       for numberStr in numbers:
           if codeNumberStr in numberStr:
               if numberStr not in matchingNumbers:
                   matchingNumbers.append(numberStr)
   matchingNumbers.sort()
   return matchingNumbers
   #print(matchingNumbers)

    # Write your code here

if __name__ == '__main__':
     vanity(["ACDEF"],["12345678","22333","122333","1223334445555"])
