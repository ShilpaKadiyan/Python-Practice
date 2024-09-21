import re #This module is intended for regualr expression, it's used to search for a specific pattern in a string.
"""class Solution:
    def isSame(self, s):
        # code here
        match = re.match(r"([a-z]+)([0-9]+)", s, re.I) #parentheses are used to create a capture group.
        if match:
            stringPart = match.group(1)
            numberPart = match.group(2)

            lengthStr = len(stringPart)
            if lengthStr == int(numberPart):
               print('Good')
            else:
               print('Bad')
solution = Solution()
print(solution.isSame("foo03"))"""

#To test how to use Regular expression
pattern = r"(\d{3})-(\d{2})-(\d{4})"
string = "123-45-6789"

"""match = re.match(pattern, string)

if match:
    print("Match found!")
    print("Full match:", match.group(0))
    print("First group:", match.group(1))
    print("Second group:", match.group(2))
    print("Third group:", match.group(3))
else:
    print("No match found.")'''

#To test string having 0 or 1 only
'''def isBinary(str):
    isBinary = false
    for char in str:
        if (char == '0' or char == '1'):
            isBinary = True
        else:
            isBinary = False
            
    if (isBinary == True):
        return True
    else:
        return False#code here"""



#To display the longest name and If there are multiple names of the longest size, return the first occurring name.
"""class Solution:
    def longest(self, names):
        longestStr = ''
        for name in names:
            leng = len(name)
            if(leng > len(longestStr)):
                longestStr = name
        return longestStr        

solution = Solution()
print(solution.longest(["John", "Doe", "Janey", "Janep"]))"""

# Program: To remove character given in a string from main string
"""Strings are immutable, so operations on strings return new strings rather than modifying the original string.
You can assign the result of such operations to the original variable (e.g., string1), effectively updating it to point to the new string."""
"""class Solution:
    def removeChars (ob, string1, string2):
        # code here 
        for subChar in string2:
            string1 = string1.replace(subChar, '')
        print(string1)    
solution = Solution()
print(solution.removeChars("shilpa", "el"))"""

# Program:  Find the repeated character present first in the string.
"""class Solution:
    def firstRep(self, s):
        # code here
        firstRepeartedChar = ''
        for char in s:
            freq = s.count(char)
            if freq > 1:
                firstRepeartedChar = char
                break
        if len(firstRepeartedChar) > 0:
            print('Repeated character found', firstRepeartedChar)
        else:   
            print('No Repeated character found')
solution = Solution()
print(solution.firstRep("shilpakkk"))"""

# Program:  To convert string into lowercase.
"""class Solution:
    def toLower(self, s):
        # code here
        print(s.lower())
solution = Solution()
print(solution.toLower("LMNOppQQ"))"""

# Program:  To remove space from string.
"""class Solution:
    def removeSpace(self, s):
        # code here
        s = s.replace(' ', '')
        print(s)
solution = Solution()
print(solution.removeSpace("geeks  for geeks"))"""

# Program:  To reverse the string.
"""class Solution:
    def myReverseSring(self, s):
        # code here
       length = len(s)
       reverseString = s[-1 : -length-1 : -1]
       print(reverseString)

solution = Solution()
print(solution.myReverseSring("Shilpa"))"""

# Program:  To check print statement with separator and end attribute in Print function.
# By Default sperator is space and end is new line.
# Chapter - 5 Input and Output

"""a, b = 10,20 #Space we are providing just for readability.
print(a, b) #Space we are providing just for readability.

#If we need seperator, we need to use sep & end attribute.
#Q: why '%' character is appearing in end while we print the output?
print(a, b, sep = ',', end = ' END ATTRIBUTE \n') #Space we are providing just for readability.

#Different ways to print the output.
print(a, b, 'is even number', sep=' : ', end='.\n')

#The Print(formatted string) statement is used to print the formatted output.

print('The value of a is %d and b is %d'  %(a, b)) # %d is used to print the integer value."""

# Program:  To check the input() function for a character.
"""ch = input('Enter the character: ')    
print("U entered: ", ch[0]) #By default input() function returns the string value."""

# Program:  To check the input() function for a integer/float from keyboard
'''intValue = int(input()) #We can skip the message to enter the value.
print("U entered : ", intValue)'''

'''floatValue = float(input('Enter float value')) #We can skip the message to enter the value.
print("U entered float value: ", floatValue)'''

# Program: To accept two integers value from keyboard and print the sum of it.
"""a = int(input('Enter first integer value: '))
b = int(input('Enter second integer value: '))
print('Sum of two integers: ', a+b)
print('Sum of', a, 'and', b, 'is', a+b)
#Using formatted string: %d, %s, %f,%c
print('Sum of two integers: a = %d and b = %d is %d Rupees' %(a,b,a+b)) #No need to provide comma here while using %
#Print fxn with replacement fields and the format method.
print('Sum of two integers: a = {} and b = {} is {} Rupees'.format(a,b,a+b)) #No need to provide comma here while using format method.""" 

#To accept more than one value from keyboard in a single line.
'''hindi, englsih, maths, evs = [float(x) for x in input("Enter hindi, english, maths, evs marks \n").split(',')]
print('1.Total Marks of all subjects: ', hindi+englsih+maths+evs)
print('2.Total Marks of all subjects: ', sum([hindi, englsih, maths, evs]))
print('3.Total Marks Hindi = %.2f English = %.2f Maths = %.2f EVS = %.2f is %.2f' %(hindi, englsih, maths, evs, hindi+englsih+maths+evs))
print('4.Total Marks Hindi = {} English = {} Maths = {} EVS = {} is = {}' .format(hindi, englsih, maths, evs, hindi+englsih+maths+evs))'''

# Program:  To accept a group of strings separated by comma and print the strings using seperate variables.
'''name1, name2, name3 = [x for x in input('Enter the strings separated by comma: ').split(',')]
print('Strings are: ', name1, name2, name3)

# Program:  To accept a group of strings separated by comma and print it as a list.
nameList = [x for x in input('Enter the strings separated by comma: ').split(',')]
print('name list is: ', nameList)

#Program: To accept a group of strings separated by comma and print it as a tuple.
nameTuple = tuple([x for x in input('Enter the strings separated by comma: ').split(',')])
print('name tuple is: ', nameTuple)'''

# Program:  To accept a group of numbers separated by comma and print it as a list.
'''scoreList = [int(x) for x in input('Enter the strings separated by comma: ').split(' ')]
print('Subject\'s Score list is: ', scoreList)'''

# Program:  To accept a group of numbers separated by comma and print it in a separate variable.
'''mathsScore, evsScore, hindiScore = [int(x) for x in input('Enter the strings separated by comma: ').split(' ')]
print('Subject\'s Scores are printing in separate variable: ', mathsScore, evsScore, hindiScore)'''

# Program: To evaluate the expression using eval() & without eval() function.
'''a, b = 10, 20
result = a+b-10
print('Result of the expression is: ', result)'''

#WHAT I FOUND HERE: there is no good use of eval() alone but it gives benefits only with input() function.
'''x, y = 10, 20
result = eval('x+y-10')
print('Result of the expression using eval() is: ', result)'''

#Program: Evaluate an expression entered from keyboard.
'''x = eval(input('Enter the expression: '))
print('Result of the expression is: ', x)'''
#Output: Enter the expression: 10+20-10
#It will give the output 20
#Output: Enter the expression: 10+20-10 without using eval() function

#WHAT I FOUND HERE: Doing int before input() function doesn't evaluate the expression.
#So we need to use eval() function to evaluate the expression.
'''x = int((input('Enter the expression: ')))
print('Result of the expression is: ', x)'''
#Output: Enter the expression: 10+20-10
#It will give Error!

#Program: Evaluate an expression entered from keyboard.
#Case-1 if we enter string value.
list = eval(input('Enter the list from keyboard: '))
print('List: ', list)
