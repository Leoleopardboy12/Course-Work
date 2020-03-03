Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def bubble_Sort(arr):
	def swap(i,j):
		alg_count[0,0]
		arr[i],arr[j]=arr[j],arr[i]
	n=len(arr)
	swapped = True
	x=-1
	while swapped:
		swapped =False
		x=x+1
		for i in range(1,n-x):
			alg_count[0]+=1
			if arr[i-1]>arr[i]:
				alg_count[1]+=1
				swap(i-1,i)
				swapped=True
	return alg_count

>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[1, 33, 72, 33, 27, 6, 10, 93, 50, 56]
>>> bubble_Sort(arr)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    bubble_Sort(arr)
  File "<pyshell#2>", line 12, in bubble_Sort
    alg_count[0]+=1
NameError: name 'alg_count' is not defined
>>> def bubble_Sort(arr):
	alg_count=[0,0]
	def swap(i,j):
		
		arr[i],arr[j]=arr[j],arr[i]
	n=len(arr)
	swapped = True
	x=-1
	while swapped:
		swapped =False
		x=x+1
		for i in range(1,n-x):
			alg_count[0]+=1
			if arr[i-1]>arr[i]:
				alg_count[1]+=1
				swap(i-1,i)
				swapped=True
	return alg_count

>>> bubble_Sort(arr)
[35, 16]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[2, 68, 40, 10, 7, 65, 14, 63, 88, 90]
>>> bubble_Sort(arr)
[30, 12]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[44, 5, 49, 5, 51, 22, 73, 10, 26, 61]
>>> bubble_Sort(arr)
[39, 16]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[51, 92, 18, 83, 43, 95, 54, 50, 0, 33]
>>> bubble_Sort(arr)
[45, 29]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[35, 87, 72, 53, 27, 0, 14, 53, 18, 79]
>>> bubble_Sort(arr)
[42, 26]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[97, 53, 25, 54, 11, 32, 24, 10, 81, 28]
>>> bubble_Sort(arr)
[44, 29]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[51, 9, 78, 56, 32, 7, 93, 4, 60, 81]
>>> bubble_Sort(arr)
[44, 20]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[13, 57, 83, 60, 13, 35, 57, 43, 20, 67]
>>> bubble_Sort(arr)
[42, 20]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> 
>>> print(arr)
[81, 78, 31, 46, 59, 78, 2, 41, 89, 32]
>>> bubble_Sort(arr)
[44, 26]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[85, 83, 26, 26, 52, 59, 16, 11, 3, 1]
>>> bubble_Sort(arr)
[45, 39]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[93, 49, 96, 1, 13, 25, 64, 53, 22, 31]
>>> 
>>> bubble_Sort(arr)
[42, 26]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[42, 24, 67, 36, 58, 55, 34, 68, 9, 64]
>>> bubble_Sort(arr)
[45, 21]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[89, 64, 86, 48, 57, 19, 41, 52, 57, 34]
>>> bubble_Sort(arr)
[45, 33]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[90, 68, 94, 41, 34, 99, 62, 33, 93, 82]
>>> bubble_Sort(arr)
[44, 25]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[33, 86, 9, 67, 53, 88, 35, 64, 5, 78]
>>> bubble_Sort(arr)
[45, 22]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[13, 98, 81, 90, 88, 5, 97, 92, 67, 54]
>>> bubble_Sort(arr)
[44, 25]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[92, 64, 28, 75, 3, 55, 91, 69, 70, 8]
>>> bubble_Sort(arr)
[45, 26]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[26, 59, 7, 85, 75, 9, 91, 39, 95, 100]
>>> bubble_Sort(arr)
[35, 11]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[32, 77, 10, 42, 14, 9, 30, 4, 12, 100]
>>> bubble_Sort(arr)
[44, 26]
>>> print(arr)
[4, 9, 10, 12, 14, 30, 32, 42, 77, 100]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[5, 84, 16, 87, 74, 52, 8, 72, 67, 0]
>>> bubble_Sort(arr)
[45, 27]
>>> arr = [random.randint(0,100) for iter in range(10)]
>>> print(arr)
[5, 22, 94, 64, 91, 50, 95, 80, 27, 11]
>>> bubble_Sort(arr)
[45, 22]
>>> 
