class TrajectoryController:
    def __init__(self, robot, kp=1.0):
        self.robot = robot
        self.kp = kp

    def move_to(self, target_angles, steps=100):
        current_angles = np.array(self.robot.get_joint_angles())
        target_angles = np.array(target_angles)
        for step in range(steps):
            error = target_angles - current_angles
            velocity = self.kp * error
            self.robot.set_joint_velocities(velocity[0], velocity[1])
            current_angles += velocity * (1 / steps)
            self.robot.set_joint_angles(current_angles[0], current_angles[1])
            self.robot.record_state()

    def get_trajectory(self):
        return self.robot.get_history()
