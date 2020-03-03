Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def selectionSort(arr,dim):
	alg_count=[0,0]
	for i in range(len(arr)):
		minimum =i
		for j in range(i+1,len(arr)):
			alg_count[0]+=1
			#Select smallest number
			if arr[j]<arr[minimum]:
				minimum=j
				alg_count[1]+=1
			
		arr[minimum], arr[i]=arr[i],arr[minimum]
	return alg_count

>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[6, 6, 1, 10, 25, 100, 39, 29, 94, 37]
>>> dim=len(arr)
>>> selectionSort(arr,dim)
[45, 6]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[50, 53, 15, 76, 79, 24, 31, 2, 8, 1]
>>> selectionSort(arr,dim)
[45, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[80, 74, 62, 31, 39, 39, 64, 14, 96, 51]
>>> selectionSort(arr,dim)
[45, 14]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[15, 32, 12, 45, 40, 49, 100, 8, 20, 49]
>>> selectionSort(arr,dim)
[45, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[66, 38, 75, 11, 11, 2, 85, 64, 84, 67]
>>> selectionSort(arr,dim)
[45, 10]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[55, 16, 30, 44, 75, 30, 49, 13, 43, 50]
>>> selectionSort(arr,dim)
[45, 7]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[41, 25, 74, 38, 18, 72, 2, 82, 31, 65]
>>> selectionSort(arr,dim)
[45, 14]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[25, 100, 27, 98, 50, 2, 61, 18, 81, 45]
>>> selectionSort(arr,dim)
[45, 12]
>>> print(arr)
[2, 18, 25, 27, 45, 50, 61, 81, 98, 100]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[95, 24, 11, 36, 12, 28, 89, 66, 56, 41]
>>> selectionSort(arr,dim)
[45, 13]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[82, 91, 28, 44, 43, 46, 46, 48, 33, 96]
>>> selectionSort(arr,dim)
[45, 10]
>>> print(arr)
[28, 33, 43, 44, 46, 46, 48, 82, 91, 96]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[14, 1, 52, 1, 58, 82, 92, 74, 10, 100]
>>> selectionSort(arr,dim)
[45, 9]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[35, 29, 9, 56, 64, 49, 83, 45, 41, 42]
>>> selectionSort(arr,dim)
[45, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[89, 3, 61, 89, 79, 74, 44, 0, 13, 74]
>>> selectionSort(arr,dim)
[45, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[78, 7, 45, 83, 36, 35, 97, 94, 72, 3]
>>> selectionSort(arr,dim)
[45, 11]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[92, 8, 67, 68, 28, 14, 21, 27, 81, 75]
>>> selectionSort(arr,dim)
[45, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[82, 68, 99, 23, 25, 10, 3, 37, 41, 70]
>>> selectionSort(arr,dim)
[45, 14]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[60, 56, 43, 74, 66, 50, 21, 73, 90, 5]
>>> selectionSort(arr,dim)
[45, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[59, 62, 61, 10, 99, 27, 61, 50, 86, 77]
>>> selectionSort(arr,dim)
[45, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[63, 0, 60, 7, 39, 67, 20, 2, 80, 59]
>>> selectionSort(arr,dim)
[45, 10]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[66, 44, 76, 77, 17, 60, 18, 47, 74, 59]
>>> selectionSort(arr,dim)
[45, 15]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[24, 44, 97, 67, 58, 12, 21, 11, 58, 13]
>>> selectionSort(arr,dim)
[45, 15]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[68, 28, 11, 90, 14, 57, 41, 99, 47, 85]
>>> selectionSort(arr,dim)
[45, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[17, 38, 21, 79, 79, 56, 86, 6, 68, 32]
>>> selectionSort(arr,dim)
[45, 11]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[40, 77, 36, 21, 17, 71, 98, 35, 18, 78]
>>> selectionSort(arr,dim)
[45, 13]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[3, 11, 34, 86, 66, 14, 78, 4, 30, 60]
>>> selectionSort(arr,dim)
[45, 13]
>>> 
