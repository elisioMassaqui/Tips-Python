#Use listas para armazenar históricos de ângulos e velocidades das juntas.
joint_angles = [[0.0, 0.0]]  # Lista de ângulos das juntas [joint1, joint2]
joint_velocities = [[0.0, 0.0]]  # Lista de velocidades das juntas [joint1, joint2]

def add_joint_state(angles, velocities, angle1, angle2, velocity1, velocity2):
    angles.append([angle1, angle2])
    velocities.append([velocity1, velocity2])

def get_latest_joint_state(angles, velocities):
    return angles[-1], velocities[-1]
