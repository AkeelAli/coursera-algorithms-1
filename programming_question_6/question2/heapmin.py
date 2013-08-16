import heapq

def heapify(x):
	heapq.heapify(x)

def heappush(heap, item):
	heapq.heappush(heap, item)

def heappop(heap):
	return heapq.heappop(heap)

def heappeek(heap):
	return heap[0]
