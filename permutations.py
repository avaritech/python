from itertools import permutations


#def Join_Tuples() -> str:

#input
#number of strings
#string 1
#string 2


def Permutate(inputStr,count):
    permutated = list(permutations(inputStr,count))
    tupleJoinedList = []
    for tuple in permutated:
        word = ""
        for element in tuple:
            word = word + element
        tupleJoinedList.append(word)
    return tupleJoinedList



inputList = input().split(' ')
stringToPermutate = inputList[0]
permCount = 0
if len(inputList) > 1:
    permCount = int(inputList[1])
else:
    permCount = len(inputList[0])

permutatedList = Permutate(stringToPermutate, permCount)
permutatedList.sort()



for item in permutatedList:
    print(item)
