
# 1. Write a Python program to get a single string from two given strings, separated by a space, and swap the first two characters of each string
string1=("enter first string")
string2=("enter second string")
x=string1[0:2]
string1=string2.replace(string1[0:2],string2[0:2])
string2=string2.replace(string2[0:2],x)

print("first string has become;-string2")
# 2.  Write a Python function that takes a list of words and returns the longest word and the
#  length of the longest one
def longest_word(words_list):
    word_len=[]
    for n in words_list:
        word_len.sort()
        
        return word_len[-1][0],word_len[-1][1]
    result= longest_word(["python","Javascript"])
    print("\n longest word")
    print("lenght of the losngest string",result[0])


# 3. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).

# 4.. Write a Python function that takes two lists and returns True if they have at least one common member.
    def common_member( list1,list2):
        for i in list1:
            if i in list2:
                return True
        else:
                return False
        list1=[1,4,3,5]
        list2=[87,89,4]
        print(common_member(list1,list2))

# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
["Back","Red","Maroon","yellow"]
["#000000","#FF000","#8000000","#FFF00"]
{'color_name','Red','color_code','#FF0000'}
{'color_name','Maroon','color_code','#80000'}
{'color_name','Yellow','color_code','#FFFF00'}

names=["Black","Red","Maroon","Yellow"]
codes=["#000000","#ff0000","#8000000","#FFFF00"]
colors_list=["Black","Red","Maroon","Yellow"]
print(colors_list)


# 6. Write a Python program to check whether all dictionaries in a list are empty or not
my_list=[{},{},{}]
my_list1=[{1:2},{},{}]
print(all(not d for d in my_list))
print(all(not d for d in my_list))
# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
list=[11,33,44,55]
for i in list:
        if(i%2 !=0):
            list.remove(i)

print("list after removing ODD numbers:")
print (list)
# 8. Find the common numbers in two lists (without using a tuple or set) 
list_a =[ 1, 2, 3, 4,] 
list_b = [2, 3, 4, 5 ]
common=[a for a in list_a if a in list_b]
print(common)

# 9. Use a nested list comprehension to find all of the numbers from 1-1000 
# that are divisible by any single digit besides 1 (2-9)
no_number=set()
for n in range(1,100):
     for x in range(2,20):
          if n % x==0:
               no_number.add(n)
               print(no_number)
               print()
result =[number for number in range(1,100)if True in [True for x in range(2,20) if number%==0]]
print(result)
# 10. Write a Python function to remove all vowels in a string

     