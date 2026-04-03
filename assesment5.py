#A programe to print the length of a list

numbers=[1,2,3,4,5]
alphabets=["a","b","c"]
def length(list):
    print(len(list))
print(len(numbers))
print(len(alphabets))

#A programe to print the elememnts of a list in a single line

students=["urwa","rubab","momna","raahima","javaria"]
marks=[89,99,97,98,95]
def elemtns(list):
    print(list)
print(students)
print(marks)

# A funtion to find the factorial n
n=int(input("enter a number"))
def fctorial(n):
    if(n==0):
        return
    print(n)
    fctorial(n-1)
fctorial(n)

#A programe to convert $ into Rs 

c=int(input("enter amount in US dollers:")) 
def converter(c):
    d=c*450
    print(d,"is your amount in  pakistani rupees")
converter(c)

#A programe of recurrsive function to calculate the sum of first n natural number 
n=int(input("Enter a natural number"))
def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n
h=sum(n)
print(h)


#A programe pf recurrsive function to print all elements in list
def marks(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    marks(list,idx+1)

numbers = [56,67,78]
marks(numbers)



