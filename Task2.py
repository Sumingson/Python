a, b = int(input()),int(input())
if a <= b:
	for i in range (a,b+1):
		if (i//1000 == i%10) and ((i//100)%10 == (i%100)//10):
			print (i)
else:
	for i in range (a,b-1, -1):
		if (i//1000 == i%10) and ((i//100)%10 == (i%100)//10):
			print (i)
