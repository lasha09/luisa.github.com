print("how old will you be in 2025?")

born=input("what year were you born?")
born=int(born)
age=(2025-born)
print(age)
print("in the year 2025 you will be", age , "years old!")

print()
print()
#while loop
i=0
while i<5:
	print(i)
	i +=1
print()
print(i)

i=-1
while True:
	i+=1

	if(i>20):
	break

	# i is odd
	if(i % 2 !=0):
		continue

	print(i)
