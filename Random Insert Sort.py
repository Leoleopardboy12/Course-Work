Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def insert(arr,dim):
	alg_count = [0,0]
	for i in range(1,dim):
		temp = arr[i]
		j=i-1
		while j>=0:
			alg_count[0]+=1
			if arr[j]>temp:
				alg_count[1]+=1
				arr[j+1]=arr[j]
				arr[j]=temp
			j-=1
	return alg_count

>>> arrs = [random.randint(0,100) for iter in range(10)]
>>> dim = len(arr)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dim = len(arr)
NameError: name 'arr' is not defined
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> dim=len(arr)
>>> print(arr)
[77, 3, 51, 66, 14, 53, 92, 0, 12, 98]
>>> insert(arr,dim)
[45, 21]
>>> 
================================ RESTART: Shell ================================
>>> import random
>>> def insert(arr,dim):
	alg_count = [0,0]
	for i in range(1,dim):
		temp = arr[i]
		j=i-1
		while j>=0:
			alg_count[0]+=1
			if arr[j]>temp:
				alg_count[1]+=1
				arr[j+1]=arr[j]
				arr[j]=temp
			j-=1
	return alg_count

>>> arr = [random.randint(0,100) for iter in range(10)]
>>> dim = len(arr)
>>> print(arr)
[93, 27, 94, 1, 98, 37, 87, 6, 27, 0]
>>> insert(arr,dim)
[45, 30]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[92, 29, 39, 42, 95, 93, 0, 97, 97, 75]
>>> insert(arr,dim)
[45, 15]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[17, 76, 82, 83, 97, 59, 20, 50, 62, 42]
>>> insert(arr,dim)
[45, 25]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[37, 78, 90, 50, 12, 86, 5, 83, 83, 8]
>>> insert(arr,dim)
[45, 25]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[4, 48, 48, 67, 78, 65, 47, 49, 61, 30]
>>> insert(arr,dim)
[45, 21]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[40, 81, 35, 48, 21, 1, 61, 79, 76, 45]
>>> insert(arr,dim)
[45, 21]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[45, 6, 68, 39, 66, 5, 2, 84, 19, 93]
>>> insert(arr,dim)
[45, 20]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[71, 69, 95, 51, 44, 20, 5, 34, 9, 10]
>>> insert(arr,dim)
[45, 38]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[94, 80, 6, 48, 46, 67, 15, 29, 19, 46]
>>> insert(arr,dim)
[45, 30]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[47, 68, 87, 86, 6, 54, 60, 48, 72, 20]
>>> insert(arr,dim)
[45, 26]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[73, 24, 90, 59, 40, 88, 81, 91, 91, 59]
>>> insert(arr,dim)
[45, 15]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[50, 59, 3, 72, 7, 84, 25, 66, 8, 17]
>>> insert(arr,dim)
[45, 23]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[43, 18, 11, 99, 9, 89, 54, 52, 20, 92]
>>> insert(arr,dim)
[45, 19]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[43, 66, 29, 11, 15, 83, 97, 28, 36, 47]
>>> insert(arr,dim)
[45, 20]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[25, 56, 13, 18, 77, 84, 2, 16, 60, 23]
>>> insert(arr,dim)
[45, 22]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[74, 61, 72, 25, 0, 61, 40, 73, 69, 31]
>>> insert(arr,dim)
[45, 26]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[16, 8, 63, 99, 14, 66, 64, 36, 26, 78]
>>> insert(arr,dim)
[45, 17]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[21, 31, 66, 21, 34, 35, 56, 40, 0, 28]
>>> insert(arr,dim)
[45, 21]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[77, 37, 42, 10, 14, 85, 44, 66, 73, 73]
>>> insert(arr,dim)
[45, 16]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[60, 26, 99, 51, 12, 92, 11, 92, 99, 50]
>>> insert(arr,dim)
[45, 21]
>>> 
