nterms=int(input("Enter a value : "))
f1=0
f2=1
f0=0
i=0
if nterms==1:
	print("Fibonacci series upto ",nterms," :",f1,f2,)
else:
	print("Fibonacci series upto ",nterms," :")
	while i < nterms:
		print(f1,end=',')
		f0=f1+f2
		f1=f2
		f2=f0
		i+=1