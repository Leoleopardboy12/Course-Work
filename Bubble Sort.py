Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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

>>> arr=[5,47,3,74,7,38,8,48,4,82]
>>> bubble_Sort(arr)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    bubble_Sort(arr)
  File "<pyshell#1>", line 12, in bubble_Sort
    alg_count[0]+=1
NameError: name 'alg_count' is not defined
>>> def bubble_Sort(arr):
	alg_count[0,0]
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

>>> arr=[5,47,3,74,7,38,8,48,4,82]
>>> bubble_Sort(arr)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    bubble_Sort(arr)
  File "<pyshell#5>", line 2, in bubble_Sort
    alg_count[0,0]
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

>>> arr=[5,47,3,74,7,38,8,48,4,82]bubble_Sort(arr)
SyntaxError: invalid syntax
>>> arr=[5,47,3,74,7,38,8,48,4,82]
>>> bubble_Sort(arr)
[44, 17]
>>> 
