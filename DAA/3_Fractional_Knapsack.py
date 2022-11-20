arr = [[500,30]]
w = 10
price = 0

arr = sorted(arr, key = lambda x : x[0] / x[1], reverse = True)

for i in range(len(arr)):
	itemWt = arr[i][1]
	itemP = arr[i][0]
	if(itemWt > w):
		price += w*(itemP / itemWt)
	else:
		price += itemP	
		w -= itemWt

print(price)
