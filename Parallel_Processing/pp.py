import time
import signal
import sys
import math
import multiprocessing as mp

signal.alarm(120)


def worker_bee(a, b, q):
	s = 0
	for n in range(a, b+1):
		prime = True
		
		if (n%2) == 0:
			prime = False
		i = 3
		while i < math.sqrt(n)+1:
			if(n%i == 0):
				prime = False
				break
			else:
				i +=2
	
		if prime:
			s += 1
	q.put(s)
	signal.alarm(120)


procs = []
q = mp.Queue()
n = len(sys.argv)-1
arg1_step = 1
arg2_step = 2
f = n//2

for i in range(n//2):
    lo = int(sys.argv[arg1_step])
    hi = int(sys.argv[arg2_step])
    p = mp.Process(target=worker_bee, args=(lo,hi,q))
    procs.append(p)
    arg1_step += 2
    arg2_step += 2

start_time = time.time()
for p in procs:
    p.start()

for p in procs:
    p.join()

total_time = time.time()-start_time

s = 0
list_of_primes = []
for p in procs:
	list_of_primes.append(q.get())
	
for n in list_of_primes:
	s += n

print ("%0.2f" % total_time, s, (" ".join(map(str,list_of_primes))) )
