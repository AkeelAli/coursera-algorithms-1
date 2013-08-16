import heapmin
import heapmax

hmin = [] # higher half of numbers
hmax = [] # lowest half of numbers
median_sum = 0


def find_median(hmin, hmax):
	size = len(hmax) + len(hmin)

	if len(hmax) == 0:
		return heapmin.heappeek(hmin)

	# if even
	if size % 2 == 0:
		return heapmax.heappeek(hmax)
	
	# if odd
	else:
		if len(hmin) > len(hmax):
			return heapmin.heappeek(hmin)
		else:
			return heapmax.heappeek(hmax)


def rebalance(hmin, hmax):
	delta = len(hmax) - len(hmin)

	if delta < 2 and delta >-2:
		return
	if delta >= 2:
		#move one over from hmax to hmin
		move = heapmax.heappop(hmax)
		#print "moving over %d from hmax to hmin" % move
		heapmin.heappush(hmin, move)

#		delta = len(hmax) - len(hmin)
#		if delta >=2 or delta <= -2:
#			return rebalance(hmin, hmax)
#		else:
#			return
	if delta <= -2:
		#move one over from hmin to hmax
		move = heapmin.heappop(hmin)
		#print "moving over %d from hmin to hmax" % move
		heapmax.heappush(hmax, move)
		
#		delta = len(hmax) - len(hmin)
#		if delta >=2 or delta <= -2:
#			return rebalance(hmin, hmax)
#		else:
#			return
		


f = open("Median.txt", 'r')

lines = f.readlines()

for line in lines:
	num = int(line)

	min_size = len(hmin)
	max_size = len(hmax)

	#Beginning when size is 0
	if min_size == 0 and max_size == 0:
		heapmin.heappush(hmin, num)
	elif max_size == 0:
		if num > heapmin.heappeek(hmin):
			heapmin.heappush(hmin, num)
			rebalance(hmin, hmax)
		else:
			heapmax.heappush(hmax, num)
	elif min_size == 0:
		if num < heapmax.heappeek(hmax):
			heapmax.heappush(hmax, num)
			rebalance(hmin, hmax)
		else:
			heapmin.heappush(hmax, num)
		
	elif num < heapmax.heappeek(hmax):
		heapmax.heappush(hmax, num)
		rebalance(hmin, hmax)
	else:
		heapmin.heappush(hmin, num)
		rebalance(hmin, hmax)
	
	
	#print hmin
	#print hmax
	#print find_median(hmin, hmax)
	#print " "

	median_sum += find_median(hmin, hmax)

print median_sum % 10000	

f.close()
