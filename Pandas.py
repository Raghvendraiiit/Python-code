import pandas as pd 
import numpy as np 
array_1 = np.array([1,2,3,4])
print(array_1)

array_2 = np.array([[1,2,3,4],[5,6,7,8]])
print(array_2)
##########################################################
l1 = [2,6,7,8,4]
def first_max(l1):
    max_1 = float('-inf')
    for i in l1:
        if i > max_1:
            max_1 = i
    return max_1
first_max(l1)
################################
        
# Sort the array without use any prebuilt function..
l1 = [2,4,9,7,5,4,6,7,4,2]

def sort(l1):
    for i in range(len(l1)):
        for j in range(0, len(l1)-i-1):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    return l1
sort(l1)
        