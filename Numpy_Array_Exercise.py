import numpy as np
import time
import sys
a = [1,2,3,4,5,6]
a = np.array([[a]])
print(a)
print(a.dtype)
print(sys.getsizeof(a))
print(a.nbytes)
print(type(a))
print(a.ndim)
print(len(a))
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
c=np.array([[[]]])
print(c.ndim)
print(c.shape)

range = np.arange(1,20,2)
print(range)
range1 = np.linspace(1,20,10)
print(range1)

arr = np.logspace(1,2,num=5,base=3)
print(arr)

arr = np.zeros([2,3])
print(arr)

arr = np.ones([2,3,4,5])
print(arr)

arr=np.full(10,2)
print(arr)

arr=np.full([2,3],2)
print(arr)

arr = np.random.rand(2,3)
print(arr)

arr=np.random.randint(10,20,5)
print(arr)


arr=np.array([1,2,3,4,5,6,7,8,9], dtype=np.float64)
print(arr)
print(arr.dtype)

arr=arr.astype(np.int32)
print(arr)
print(arr.dtype)
print(arr.itemsize)

arr1=np.array([[1,2,3,4],[1,2,3,4]])
print(arr1.shape)
print(arr1.itemsize)

arrRe=arr1.reshape(4,2)
print(arrRe)
print(arrRe.shape)
print(arrRe.ravel())
print(arrRe.flatten())

#arthematic operations
arr1=np.array([[1,2,3,4],[1,2,3,4]])
arr2=np.array([[1,2,3,4],[1,2,3,4]])
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)
print(arr1**arr2)
print(arr1**2)
print(arr1.sum())
print(arr1.min())
print(arr1.max())
print(arr1.mean())
print(arr1.std())
print(np.sqrt(arr1))
print(np.exp(arr1))
print(np.log(arr1))
print(np.log10(arr1))
print(np.sin(arr1))
print(np.cos(arr1))
print(np.tan(arr1)) 
print(np.exp(arr1))


#Indexing Slicing

arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[-1:-4:-1])

print(arr[::3])

matrix=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(matrix[0:2, :2])
print(matrix[1:,1:])


arr = np.array([1,2,3,4,5,6,7,8,9])
ind=[0,2]
print(np.take(arr,ind))

for arr in np.nditer(arr):
    print(arr, end=" ")

arr = np.array([[1,2,3,4],[5,6,7,8]])
for ind,arr in np.ndenumerate(arr):
    print(ind,arr)
    
arr4=np.array([[1,2,3,4],[5,6,7,8]])
print(arr4)
arr2=arr4[0:2,0:2].copy()
print(arr2)                                      

print(arr2.transpose())
print(arr2)

#concatenation
a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[9,10,11,12],[13,14,15,16]])
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))
print(np.vstack((a,b)))
print(np.hstack((a,b))) 
print(a+b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))

#split
a=np.array([[1,2,3,4],[5,6,7,8]])   
print(np.split(a,2,axis=0))
print(np.split(a,4,axis=1))

print(np.hsplit(a,2))
print(np.vsplit(a,2))

print(np.repeat(a,2))

print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.argmin(a))
print(np.argmax(a))
print(np.sort(a))
print(np.cumsum(a))
print(np.cumprod(a))

print(np.where(a>3,"low","high"))

print(np.argwhere(a>3))










