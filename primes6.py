def primelister(x):

	x=int(x)

	if x<2:
		print('Please enter a number bigger than 2')
		exit()

	primelist = [2]
	s=3

	while s <= x:
		p=0
		for m in primelist:
			if m <= int(s**(0.5)) and p==0:
				p += not(s%m)

		if p ==0:
			primelist.append(s)
		s+=1
	return primelist




def primenumber(x):

	
	return len(primelister(x))





x = input('check up to? ')

print('The list of primes up to and including ' + str(x) + ' is:') 

print(primelister(x))

print('There are ' + str(primenumber(x)) + ' primes in the list')