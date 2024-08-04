from sklearn.linear_model import LinearRegression
import numpy as np

# Dados de exemplo
X = np.array([[150, 100], [200, 150], [250, 200]])
y = np.array([[45, 30], [60, 45], [75, 60]])

model = LinearRegression()
model.fit(X, y)

target = np.array([[200, 150]])
prediction = model.predict(target)
print(f'Predicted angles for target {target}: {prediction}')
