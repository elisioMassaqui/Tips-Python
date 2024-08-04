import numpy as np

joint_angles = np.array([0.0, 0.0])
joint_velocities = np.array([0.0, 0.0])

def set_joint_angles(angles, angle1, angle2):
    angles[0] = angle1
    angles[1] = angle2

def get_joint_angles(angles):
    return angles[0], angles[1]

def set_joint_velocities(velocities, velocity1, velocity2):
    velocities[0] = velocity1
    velocities[1] = velocity2

def get_joint_velocities(velocities):
    return velocities[0], velocities[1]
