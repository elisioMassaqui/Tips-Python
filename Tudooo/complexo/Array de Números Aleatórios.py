#Use a biblioteca numpy para
#  criar um array de números aleatórios e 
# calcule a média e o desvio padrão dos valores.
import numpy as np

array = np.random.randint(0, 10, size=10)
media = np.mean(array)
desvio_padrao = np.std(array)

print(f"Array: {array}")
print(f'Média: {media}')
print(f'Desvião Padrão: {desvio_padrao}')
