import math

def primeFactors(n):
	t=1
	while n % 2 == 0:
		t=t*2
		n = n / 2

	for i in range(3,int(math.sqrt(n))+1,2):

		while n % i== 0:
			t=t*2
			n = n / i

	if n > 2:
		t=t*2

	return t

def S(N):
	s=0
	for i in range(1,N,1):
		s=s+primeFactors(N)

S(pow(10,8))
