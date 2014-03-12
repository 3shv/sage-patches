import sys
from sage.all import *
from sage.matroids.advanced import *
from itertools import combinations

def Kconnectivity(M,k):

	if k < 0:
		raise ValueError("k should be non-negative")

	E = M.groundset()
	rank = M.rank()

	for X in list(combinations(E,k)):
		for Y in list(combinations(E-frozenset(X),k)):

			req = rank + k - M.rank(X) - M.rank(Y)

			M1 = (M.contract(X)).delete(Y)
			M2 = (M.contract(Y)).delete(X)
			if len(M1.intersection(M2)) < req:
				return False
	return True

def connectivity(M):

	ans = 0
	E = M.groundset()

	for i in range(1,len(E)+1):
		if not Kconnectivity(M,i):
			return i
	return float('inf')







