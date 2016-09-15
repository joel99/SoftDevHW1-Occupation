#!/usr/bin/python
import random

#Winston Venderbush and Joel Ye
#9/15/16

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
			return key
		else:
			percentctr += d[key]

print randSelect()




