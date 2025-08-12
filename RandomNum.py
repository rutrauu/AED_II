import random

def escolher_numeros():
    return random.sample(range(1, 51), 10)  # range é exclusivo no final

# Teste
print(escolher_numeros())