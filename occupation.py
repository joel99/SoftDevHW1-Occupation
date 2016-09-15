#!/usr/bin/python
import random
import copy

f = open("occupations.csv", "r")

d = {}
flag = False

for line in f:
	if flag == False:
		flag = True
	else:
		ind = line.rfind(',');
		key = line[:ind]
		val = line[ind+1:]
		val = float(val)
		d[key] = val
d.pop(key)


def randSelect():
	f = random.random() * 100
	percentctr = 0.0
	for key in d:
		if f < percentctr + d[key]:
			print "run"
			return key
		else:
			percentctr += d[key]
			#print "This shouldn't happen"

#print randSelect()


def checker():
	d2 = copy.deepcopy(d)
	for key in d2:
		d2[key] = 0
		
	print d2

	runs = 1000
	while runs > 0:
		key = randSelect()
		d2[key] = d2[key] + 1
	return d2

print checker()



