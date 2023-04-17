a = [1, 4, 6]
b = [11, 33, 22]

def list_sort(a, b):
	i = len(b) - 1
	while i != 1:
		if b[i] < b[i - 1]:
			a[i - 1], a[i] = a[i], a[i - 1]
		i -= 1

list_sort(a, b)

print(a)
