"""
Aidan Hunt
4/3/2023
"""

# Example function:
def countLetters(nameIn):
    '''
    Given an input name (as a string), prints how many letters are in the name.
    '''
    numLetters = len(nameIn)
    print('The name', nameIn, 'has', numLetters, 'letters in it!')
    
# name1 = 'Aidan'
# name2 = 'Bob'
# name3 = 'Terrence'
# name4 = 'Garrett'

# countLetters(name1)
# countLetters(name2)
# countLetters(name3)
# countLetters(name4)

nameList = ['Aidan', 'Bob', 'Terrence', 'Garrett']
# countLetters(nameList)

# countLetters(nameList[0])
# countLetters(nameList[1])
# countLetters(nameList[2])
# countLetters(nameList[3])

# countLetters(nameList[i])

# For loop
# for i in range(len(nameList)):
#     print(i)
#     countLetters(nameList[i])
    
# Can we make this simpler?

for currName in nameList:
    print(currName)
    countLetters(currName)
    



    
