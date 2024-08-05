import numpy as np

def forward_kinematics(joint_angles, lengths):
    x = y = 0
    angle = 0
    for i in range(len(joint_angles)):
        angle += joint_angles[i]
        x += lengths[i] * np.cos(angle)
        y += lengths[i] * np.sin(angle)
    return x, y

def inverse_kinematics(x, y, lengths):
    joint_angles = [0] * len(lengths)
    for i in range(len(lengths)):
        dx = x - sum([lengths[j] * np.cos(sum(joint_angles[:j])) for j in range(i)])
        dy = y - sum([lengths[j] * np.sin(sum(joint_angles[:j])) for j in range(i)])
        joint_angles[i] = np.arctan2(dy, dx)
    return joint_angles

lengths = [100, 100]
target_x, target_y = 150, 100

angles = inverse_kinematics(target_x, target_y, lengths)
print(f'Joint angles to reach ({target_x}, {target_y}): {angles}')
