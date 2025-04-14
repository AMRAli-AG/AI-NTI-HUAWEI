#lesson one
print("amr ali")
'''
AMR 
ALI A
ALL
LOVE 
'''

print("_____________________________________________________________ ")

X =10
y ="AMORA"
z = 0.56
print(type(X))
print(type(y))
print(type(z))

print("_____________________________________________________________ ")

x ,y ,z = 3 ,"f,e",0.12
print(x)
print(y)
print(z)

print("_____________________________________________________________ ")

x=2 
z=3
print( z+x)

#num1 = input("enter num1")
#print(num1)

def printing ():
    print("ja")

printing()

print("_____________________________________________________________ ")

import random

print(random.randrange(1,10))
print(random.randint(1,10))

#list 
list = [10,23,3,22,56,64]
print(list)
list[0]=56
print(list)
print("_____________________________________________________________ ")

lenth = len(list)
print( "lenth of list = " ,lenth)
print(list[2:5])
list[2:5]=[23,54,43]

list.insert(2,"jkjb")
print(list)
print("_____________________________________________________________ ")

list.append("amnfjb")
print(list)
listforextend =["ic ben", "frguh"]
list.extend(listforextend)
list.remove(56)
list.pop(1)
print(list)
print("_____________________________________________________________ ")

del list[2]
print(list)
print("_____________________________________________________________ ")

for i in range(len(list)):
    print(list[i ])

#tuple 
print("_____________________________________________________________ ")

tuple = ("amr","ali","linda", "kareem ")
print(tuple)
print(len(tuple))