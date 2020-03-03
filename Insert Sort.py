Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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

>>> arr=[5,47,3,74,7,38,8,48,4,82]
>>> dim =len(arr)
>>> insert(arr,dim)
[45, 17]
>>> 
