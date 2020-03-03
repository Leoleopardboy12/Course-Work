Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def selectionSort(arr):
	alg_count=[0,0]
	for i in range(len(arr)):
		maximum =i
		for j in range(i+1,len(arr)):
			alg_count[0]+=1
			#Select smallest number
			if arr[j]>arr[maximum]:
				maximum=j
				alg_count[1]+=1
			
		arr[i],arr[maximum]=arr[maximum],arr[i]
	return alg_count

>>> arr=[5,47,3,74,7,38,8,48,4,82]
>>> selectionSort(arr)
[45, 10]
>>> print(arr)
[82, 74, 48, 47, 38, 8, 7, 5, 4, 3]
>>> 
