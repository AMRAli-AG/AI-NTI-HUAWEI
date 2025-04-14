import numpy as np

vector1 = np.array([1,2,3])

vector2 = np.array([[10],[20],[30]])


print(vector1)
print(vector2)
 

arr = np.array ([[1,2,3],[4,5,6,]])

print(arr)
print("_____________________________________________________________ ")
list1 = [1,2,3 ]
list2 = [3,4,5 ]

arr2 = np.array ([list1,list2])
print (arr2)
print("_____________________________________________________________ ")
list3 = np.arange(start =1 , stop =13 , step = 1)
# list4 = np.arange(start =13 , stop =22 , step = 1)
# arr3 = np.array ([list3,list4])

arr4 = np.array(list3.reshape(3,4))
print(list3)
print(arr4)
print("_____________________________________________________________ ")

list5 = [1,2,3 ]
list6 = [3,4,5 ]

arr5 = np.array (list5)
arr6 = np.array (list5)

sum1 = arr5 +arr6

print(sum1)

print("_____________________________________________________________ ")
from numpy import array
from numpy.linalg import norm

arr7 = array ([1,2,3,4,5])

print (arr7)

norm_1 = norm(arr7,1)
norm_2 = norm(arr7,2)
print (norm_1)
print (norm_2)


print("_____________________________________________________________ ")


from numpy.linalg import det

arr8 = np.array([[10,20],[30,40]])

det1 = np.linalg.det (arr8)

print (int(det1))

print("_____________________________________________________________ ")

arr9 = np.array([[3,7],[2,5]])
print(arr9)

arr9_inv = np.linalg.inv(arr9)
print(array(arr9_inv))

print("_____________________________________________________________ ")


from numpy.linalg import eig

arr10 = np.array([[3,7],[2,5]])

w,v=eig(arr10)

print(v)
print(w)





