# -*- coding: utf-8 -*-
"""
Aidan Hunt
4/4/2023
Loop Examples
"""

#%% Loop Example 1
numList = [1, 2, 3, 4]
list1 = []
for num in numList: # For each number in numList...
    list2 = []      # Create a second list
    for i in range(5): # For numbers between 0 and 4
        list2.append(num * i) # Tack on to the end of list2 num * i
    
    list1.append(list2) # Tack on to the end of list1 the list that we just made

print(list1)

#%% Loop Example 2

wordList = ['what', 'is', 'this', 'for', 'loop', 'doing']
for i, word in enumerate(wordList):
    wordList[i] = len(word)
    
print(wordList)

#%% Loop Example 3

colorList = ['green', 'blue', 'purple', 'red']
foodList = ['cheese', 'apple', 'sandwich', 'taco']

for food, color in zip(colorList, foodList):
    print("Would you like to eat a", color, food, "?")
    
#%% Loop (?) Example 4

listOfLists = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6]]

listOfLists = [[(num+1)**2 for num in numList] for numList in listOfLists]

print(listOfLists)
