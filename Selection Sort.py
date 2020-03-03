Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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

>>> 
>>> arr=[5,47,3,74,7,38,8,48,4,82]
>>> def selectionSort(arr):
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

>>> arr=[5,47,3,74,7,38,8,48,4,82]
>>> selectionSort(arr)
[45, 8]
>>> 
