#Use o Pandas DataFrame para armazenar e manipular dados de maneira tabular, especialmente útil para análise e visualização de dados.
import pandas as pd

data = pd.DataFrame(columns=["joint1_angle", "joint2_angle", "joint1_velocity", "joint2_velocity"])

def add_joint_state(data, angle1, angle2, velocity1, velocity2):
    data = data.append({
        "joint1_angle": angle1,
        "joint2_angle": angle2,
        "joint1_velocity": velocity1,
        "joint2_velocity": velocity2
    }, ignore_index=True)
    return data

def get_latest_joint_state(data):
    return data.iloc[-1]

