import sys
import time

# Criando um texto grande para simular um arquivo
texto = "linha de texto\n" * 1_000_000  # 1 milhão de linhas
linhas = texto.splitlines()

# Função usando return (tudo de uma vez)
def ler_tudo():
    return [linha for linha in linhas]

# Função usando yield (um de cada vez)
def ler_lazy():
    for linha in linhas:
        yield linha

# Teste com return
inicio = time.time()
dados = ler_tudo()
fim = time.time()

print(f"[RETURN] Tempo: {fim - inicio:.4f}s | Memória: {sys.getsizeof(dados) / (1024 * 1024) } Mbytes")

# Teste com yield
inicio = time.time()
dados_gen = ler_lazy()  # Isso só cria o gerador
cont = 0
for linha in dados_gen:  # Só processa quando precisa
    cont += 1
fim = time.time()

print(f"[YIELD]  Tempo: {fim - inicio:.4f}s | Memória: {sys.getsizeof(dados_gen) / (1024 * 1024)} Mbytes")