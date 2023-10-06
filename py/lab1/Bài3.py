# function which return reverse of a string
#1
'''
def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
'''
#2
'''
# Python program to demonstrate
# symmetry and palindrome of the
# string


# Function to check whether the
# string is palindrome or not
def palindrome(a):

	# finding the mid, start 
	# and last index of the string
	mid = (len(a)-1)//2	 #you can remove the -1 or you add <= sign in line 21 
	start = 0			 #so that you can compare the middle elements also.
	last = len(a)-1
	flag = 0

	# A loop till the mid of the
	# string
	while(start <= mid):

		# comparing letters from right
		# from the letters from left
		if (a[start]== a[last]):
			
			start += 1
			last -= 1
			
		else:
			flag = 1
			break;
			
	# Checking the flag variable to 
	# check if the string is palindrome
	# or not
	if flag == 0:
		print("The entered string is palindrome")
	else:
		print("The entered string is not palindrome")
		
# Function to check whether the
# string is symmetrical or not	 
def symmetry(a):
	
	n = len(a)
	flag = 0
	
	# Check if the string's length
	# is odd or even
	if n%2:
		mid = n//2 +1
	else:
		mid = n//2
		
	start1 = 0
	start2 = mid
	
	while(start1 < mid and start2 < n):
		
		if (a[start1]== a[start2]):
			start1 = start1 + 1
			start2 = start2 + 1
		else:
			flag = 1
			break
	
	# Checking the flag variable to 
	# check if the string is symmetrical
	# or not
	if flag == 0:
		print("The entered string is symmetrical")
	else:
		print("The entered string is not symmetrical")
		
# Driver code
string = 'amaama'
palindrome(string)
symmetry(string)
'''
#3
'''
# Python code
# To reverse words in a given string

# input string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
	# appending reversed words to l
	l.append(i)
# printing reverse words
print(" ".join(l))
'''
#4
'''
# Initializing String
test_str = "GeeksForGeeks"

# Removing char at pos 3
# using replace
new_str = test_str.replace('e', '')

# Printing string after removal
# removes all occurrences of 'e'
print("The string after removal of i'th character( doesn't work) : " + new_str)

# Removing 1st occurrence of s, i.e 5th pos.
# if we wish to remove it.
new_str = test_str.replace('s', '', 1)

# Printing string after removal
# removes first occurrences of s
print("The string after removal of i'th character(works) : " + new_str)
'''
#5
'''
# Take input from users 
MyString1 = "A geek in need is a geek indeed"

if "need" in MyString1: 
	print("Yes! it is present in the string") 
else: 
	print("No! it is not present") 
'''
#6
'''
from collections import Counter

# initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# printing original string
print("The original string is : " + str(test_str))

# Words Frequency in String Shorthands
# using Counter() + split()
res = Counter(test_str.split())

# Printing result
print("The words frequency : " + str(dict(res)))
'''
#7
'''
# initializing string
test_str = 'geeksforgeeks_is_best'

# printing original string
print("The original string is : " + test_str)

# Convert Snake case to Pascal case
# Using title() + replace()
res = test_str.replace("_", " ").title().replace(" ", "")

# printing result 
print("The String after changing case : " + str(res)) 
'''
#8
'''
str = "geeks"
print(len(str))
'''
#9
'''
#input string 
n="This is a python language"
#splitting the words in a given string
s=n.split(" ") 
for i in s: 
#checking the length of words
if len(i)%2==0: 
	print(i)
'''
#10
'''
def check(string):
	string = string.replace(' ', '')
	string = string.lower()
	vowel = [string.count('a'), string.count('e'), string.count(
		'i'), string.count('o'), string.count('u')]

	# If 0 is present int vowel count array
	if vowel.count(0) > 0:
		return('not accepted')
	else:
		return('accepted')


# Driver code
if __name__ == "__main__":

	string = "SEEquoiaL"

	print(check(string))
'''