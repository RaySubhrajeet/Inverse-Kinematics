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
    Tab = np.array([
                 	[np.cos(angles[0]), (-1)*np.sin(angles[0]), 0, link_lengths[0]* np.cos(angles[0]) ], 
				    [np.sin(angles[0]),  np.cos(angles[0]), 0, link_lengths[0]* np.sin(angles[0])],
			        [0, 0, 1, 0],
			        [0, 0, 0, 1]])

    Tbc = np.array([
    				[np.cos(angles[1]), (-1)*np.sin(angles[1]), 0, link_lengths[1]* np.cos(angles[1]) ], 
				    [np.sin(angles[1]),  np.cos(angles[1]), 0, link_lengths[1]* np.sin(angles[1])],
			        [0, 0, 1, 0],
			        [0, 0, 0, 1]])


    Tcd = np.array([
    				[np.cos(angles[2]), (-1)*np.sin(angles[2]), 0, link_lengths[2]* np.cos(angles[2]) ], 
				    [np.sin(angles[2]),  np.cos(angles[2]), 0, link_lengths[2]* np.sin(angles[2])],
			        [0, 0, 1, 0],
			        [0, 0, 0, 1]])

    Tad=np.dot(Tab, np.dot(Tbc,Tcd))

    return np.array([Tad[0][3], Tad[1][3]])



if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    print("A:")
    print(fk([0.0, 0.0, 0.0], [1.0, 1.0, 1.0]))
    print("B:")
    print(fk([0.3, 0.4, 0.8], [0.8, 0.5, 1.0]))
    print("C:")
    print(fk([1.0, 0.0, 0.0], [3.0, 1.0, 1.0]))
