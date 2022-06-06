import numpy as np
"""lst1=[[1,2,3],
      [4,5,6],
      [7,8,9]]
print(lst1[1][1:],lst1[2][1:],sep="\n")"""

"""# lst=[12,13,14,15,16]
# arr=np.array(lst,dtype="float")
# print(arr,type(arr))
# print(lst,type(lst))
#
# lst2=[[1,2,3],[4,5,6],[7,8,9]]
# print(lst2,type(lst2))
# arr2=np.array(lst2)
# print(arr2,type(arr2))

lst3=[[[1,2],[4,5],[7,8]],[[1,2],[4,5],[7,8]]]
print(lst3,type(lst3))
arr3=np.array(lst3)
print(arr3,type(arr3))


print(f"""
# arr3.shape:{arr3.shape}
# arr3.size:{arr3.size}
# arr3.dtype:{arr3.dtype}
# arr3.size:{arr3.itemsize}
# arr3.dim:{arr3.ndim}
""")"""
# print(arr[0],arr[-1],arr[-2:],arr[::-1])
# lst=[12,13,14,15,16,"mohit"]
# arr=np.array(lst)
# print(arr,id(arr))
# arr[0]=100
# print(arr,id(arr))
#
# lst2=[[1,2,None],[4,5,6],[7,8,9]]
# arr2=np.array(lst2)
# print(arr2,id(arr2))
# arr2[0][1]=100
# print(arr2,id(arr2))

# arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr3[0])
# print(arr3[1])
# print(arr3[2])
# print(arr3[:,1])
# arr3[1]=[9,9,9]
# print(arr3)
# arr3[:,1]=[9,9,9]
# print(arr3)

# print(arr3[::2])
# print(arr3[::2,::2])

# arr=np.zeros((3,3,3),dtype="int")
# print(arr,"\n")
#
# arr=np.ones((3,3,3),dtype="int")
# print(arr,"\n")
#
# arr=np.arange(10)
# print(arr,"\n")
#
# arr=np.arange(2,21,2)
# print(arr,"\n")
#
# arr=np.arange(1,5,.5)
# print(arr,"\n")


arr=np.array([12,13,45,16,1,7])
print(arr*2)
print(arr[::2])
print(arr[[0,-1,1]])


arr=np.array([[1,21,23],[45,2,56],[57,89,78]])
print(arr[arr%2==0])
print(arr%2==0)

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])

arr3=np.zeros((3,3),dtype="int")
for i in range(3):
      for j in range(3):
            arr3[i][j]=arr2[i][j]+arr1[i][j]

print(arr3)
print(arr2+arr1)
print(arr2*arr1)
print(arr2-arr1)
print(arr2/arr1)
print(arr1.dot(arr2))