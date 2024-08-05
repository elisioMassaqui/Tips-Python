import numpy as np

class Joint:
    def __init__(self, angle=0.0, velocity=0.0):
        self.angle = angle
        self.velocity = velocity

class Robot:
    def __init__(self):
        self.joint1 = Joint()
        self.joint2 = Joint()
        self.history = []

    def set_joint_angles(self, angle1, angle2):
        self.joint1.angle = angle1
        self.joint2.angle = angle2

    def get_joint_angles(self):
        return self.joint1.angle, self.joint2.angle

    def set_joint_velocities(self, velocity1, velocity2):
        self.joint1.velocity = velocity1
        self.joint2.velocity = velocity2

    def get_joint_velocities(self):
        return self.joint1.velocity, self.joint2.velocity

    def record_state(self):
        state = {
            "joint1_angle": self.joint1.angle,
            "joint2_angle": self.joint2.angle,
            "joint1_velocity": self.joint1.velocity,
            "joint2_velocity": self.joint2.velocity
        }
        self.history.append(state)

    def get_history(self):
        return self.history
