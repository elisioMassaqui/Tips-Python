# Uma fila é uma estrutura de dados que segue o princípio FIFO (First In, First Out).

from collections import deque

# Criando uma fila
queue = deque(["Eric", "John", "Michael"])

# Adicionando elementos à fila
queue.append("Terry")
queue.append("Graham")
print(queue)  # Output: deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

# Removendo elementos da fila
queue.popleft()  # Output: 'Eric'
print(queue)  # Output: deque(['John', 'Michael', 'Terry', 'Graham'])
