#!/bin/python

import math
import os
import random
import re
import sys

#accepts input of the following set:

#[ArraySize, eachNumberInArray]
#examples: 
#numbers1 = [3,1,6,10]
#numbers2 = [3,21,11,7]
def countSum(numbers):
        totalSum = 0    #numbersCode
        for k in numbers[1:]: #k is each num in the array
#
                totalSum += 1#always divisible by 1
                if k % 2 == 1 and k != 1:
                        totalSum += k   #odd num * 1 added to sum
#
                halfNum = k / 2
                for divisorIteration in range(2,halfNum +1):
                        divisorMod = k % divisorIteration #checks for validity
                        if divisorMod == 0:
                                divisorResult = k / divisorIteration
                                if divisorResult % 2 == 1:
                                        totalSum += divisorResult
#               print(halfNum)

        return totalSum
