import numpy as np


def fk(angles, link_lengths):
	"""
	Computes the forward kinematics of a planar, n-joint robot arm.

	Given below is an illustrative example. Note the end effector frame is at
	the tip of the last link.

		q[0]   l[0]   q[1]   l[1]   end_eff
		  O-------------O--------------C

	you would call:
		fk(q, l)

	:param angles: list of angle values for each joint, in radians.
	:param link_lengths: list of lengths for each link in the robot arm.
	:returns: The end effector position (not pose!) with respect to the base
		frame (the frame at the first joint) as a numpy array with dtype
		np.float64
	"""
	# FILL in your code here
	
	q=0
	x=0
	y=0
	for angle, link in zip(angles,link_lengths):
		q=q+angle
		x=x+(link * np.cos(q))
		y=y + (link * np.sin(q))

	pos=np.array([x,y,0])
	
	return pos



if __name__ == '__main__':
	np.set_printoptions(suppress=True)

	print("A:")
	print(fk([0.0, 0.0, 0.0], [1.0, 1.0, 1.0]))
	print("B:")
	print(fk([0.3, 0.4, 0.8], [0.8, 0.5, 1.0]))
	print("C:")
	print(fk([1.0, 0.0, 0.0], [3.0, 1.0, 1.0]))
