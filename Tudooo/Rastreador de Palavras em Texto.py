from collections import Counter
import re

def word_counter(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

if __name__ == '__main__':
    text = "Python é uma elisi elisio linguagem de programação poderosa e versátil. Python elisio pode ser usada para muitos oii propósitos."
    frequencies = word_counter(text)
    print("Frequência das palavras:", frequencies)
