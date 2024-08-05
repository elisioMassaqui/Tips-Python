#Use dicionários para armazenar estados e comandos do robô.
robot_state = {
    "joint1": {"angle": 0.0, "velocity": 0.0},
    "joint2": {"angle": 0.0, "velocity": 0.0}
}

def set_joint_angles(state, angle1, angle2):
    state["joint1"]["angle"] = angle1
    state["joint2"]["angle"] = angle2

def get_joint_angles(state):
    return state["joint1"]["angle"], state["joint2"]["angle"]

def set_joint_velocities(state, velocity1, velocity2):
    state["joint1"]["velocity"] = velocity1
    state["joint2"]["velocity"] = velocity2

def get_joint_velocities(state):
    return state["joint1"]["velocity"], state["joint2"]["velocity"]
