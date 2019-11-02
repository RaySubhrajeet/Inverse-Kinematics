import numpy as np


def line_sphere_intersection(p1, p2, c, r):
	"""
	Implements the line-sphere intersection algorithm.
	https://en.wikipedia.org/wiki/Line-sphere_intersection

	:param p1: start of line segment
	:param p2: end of line segment
	:param c: sphere center
	:param r: sphere radius
	:returns: discriminant (value under the square root) of the line-sphere
		intersection formula, as a np.float64 scalar
	"""
	# FILL in your code here

	line_vector=np.subtract(p2,p1)       #np.array([p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2] ])
	val=np.sqrt(np.sum([(p2 - p1)**2
						   for p1, p2 in zip(p1,p2)]))

	if val==0:
		unit_vector=np.array([0,0,0])
	else:
		unit_vector=[linevec/val for linevec in line_vector]
	vecO_C=np.subtract(p1,c)
		
	res=np.dot(unit_vector,vecO_C)* np.dot(unit_vector,vecO_C) - ( np.dot(vecO_C, vecO_C) - r*r )
	return res
