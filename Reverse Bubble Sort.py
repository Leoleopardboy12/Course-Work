Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
			if arr[i-1]<arr[i]:
				alg_count[1]+=1
				swap(i-1,i)
				swapped=True
	return alg_count

>>> arr=[5,47,3,74,7,38,8,48,4,82]
>>> bubble_Sort(arr)
[45, 28]
>>> print(arr)
[82, 74, 48, 47, 38, 8, 7, 5, 4, 3]
>>> 
