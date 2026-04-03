#store the folowing word meaning in a python dictionary .......
dictionary={
    "table":{
        "meaning1":"a piece of furniture",
        "meaning2":"list of facts & figure",
    },
    "cat":"a small animal"
}
print(dictionary)

#we have a list of subjects for students. assume one classroom is requird for 1 subject.how many classroom are nedeed by all students
listt={"python","java","c++","python","java","java","python","c++","c"}# this is a set
print(len(listt))

# A programe to enter marks of 3 subjects from the user and store them in a dictionary.
a=input("Enter 1st subject name:")
a2=input("Enter marks:")
b=input("Enter 2nd subject name:")
b2=input("Enter marks:")
c=input("Enter 3rd subject name:")
c2=input("Enter marrks:")

dcc={
    "subject name":[a,b,c],
    "marks":[a2,b2,b2]
}
print (dcc)