import matplotlib.pyplot as plt
import numpy as np

def generate_color_pattern():
    data = np.random.rand(10, 10, 3)
    plt.imshow(data)
    plt.axis('off')
    plt.savefig('color_pattern.png', bbox_inches='tight', pad_inches=0)

if __name__ == '__main__':
    generate_color_pattern()
    print("Padrão de cores gerado e salvo como 'color_pattern.png'")
