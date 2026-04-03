# A program to input user's first name & print its length. 
a=str(input("Enter your first name."))
print(len(a))

# A program to find the occurence of $ in a string 
b="i have alots of $s.\ni play in $s.\nbut the cloud is that i dont need $s."
print(b.count("$"))


# A program to ask the user to enter name of their three favourite fruite and store them in a list 
fruite=[]
a=str(input("Enter 1st fruite name:"))
b=str(input("Enter 2nd fruite name:"))
c=str(input("Enter 3rd fruite name:"))
fruite.append(a)
fruite.append(b)
fruite.append(c)
print(fruite)

# A programe to check is a list contain a palindrome of element.(hint: use copy() method)
fruite2=fruite.copy()
fruite2.reverse()
if(fruite2==fruite):
    print("palindrome")
else:
    print("not palindrome") 

# A program to count the number of student with the "A"grade in the following tupple
#   ("C","D","A","A","B","B","A")
tup=["C","D","A","A","B","B","A"]
print(tup.count("A"))
tup.sort()
print(tup)


    