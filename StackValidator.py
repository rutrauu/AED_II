# Criar um validador de expressões matemáticas

# Os delimitadores são { }, [ ] e ( )
# Cada delimitador de abertura deve ter um delimitador de fechamento
# Toda { deve ser seguida por um }
# Exemplos:
# c[d] - Ok
# a{b[c]d}e - Ok
# a{b(c]d}e - Erro
# a[b{c}d]e} - Erro


class Pilha:
    def __init__(self):  
        self.__topo = -1
        self.__valores = []

    def pilha_vazia(self):
        if self.__topo == -1:
            return True
        return False

    def empilhar(self, valor):
            self.__topo += 1
            self.__valores.insert(self.__topo, valor)

    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha está vazia.")
            return -1   
        else:
            valor = self.__valores[self.__topo]
            self.__topo -= 1
            return valor  

    def ver_topo(self):
        if not self.pilha_vazia():
            return self.__valores[self.__topo]
        return -1


def validar_expressao(pilha, expressao):
    print('-'*30)
    print(f"Analisando: {expressao}")
    expressao = expressao.strip()
    if expressao == "":
        print("Expressão vazia.")
        return
    caracteres_abertura = "{[("
    caracteres_fechamento = "}])"
    for i, caracter in enumerate(expressao):
        if caracter in caracteres_abertura:
            pilha.empilhar(caracter)
        elif caracter in caracteres_fechamento:
            if not pilha.pilha_vazia():
                caracter_topo = pilha.ver_topo() 
                if (caracter == '}' and caracter_topo != '{') or \
                    (caracter == ']' and caracter_topo != '[') or \
                    (caracter == ')' and caracter_topo != '('):
                    print('Erro ', caracter, ' na posição', i)
                    break
                pilha.desempilhar()
            else:
                print('Erro ', caracter, ' na posição', i)
    if not pilha.pilha_vazia():
        print("Erro.")
    else:
        print("Expressão válida.")
    print()

expressoes = \
""" 3 * [(5 - 2) + (4 - 2)]
    a[d]
    a{b[c]d}e
    a{b(c]d}e
    a[b{c}d]e}
    a{b(c)
"""    

pilha = Pilha()

def lista():
    lista = []
    for linha in expressoes.splitlines():
        lista.append(linha.strip())
    return lista
    # return [linha.strip() for linha in expressoes.splitlines()]

def main():
    for expressao in lista():
        validar_expressao(pilha, expressao)
# main()
# exit()

















def gerador():
    for linha in expressoes.splitlines():
            yield linha
            
def main2(): 
    for expressao in gerador():
        validar_expressao(pilha, expressao)
# main2()
# exit()















class Expressoes:
    def __init__(self, expressoes):
        self.lista_expressoes = [linha.strip() for linha in expressoes.splitlines()]
    
    def __iter__(self):
        return iter(self.lista_expressoes)
    
    def __len__(self):
        return len(self.lista_expressoes)


def main3():
    obj = Expressoes(expressoes)
    for expressao in obj:
        validar_expressao(pilha, expressao)

# main3()
# exit()















def lista_lambda():
    return (lambda texto: texto.splitlines())(expressoes)

def main4():
    for expressao in lista_lambda(): #(lambda texto: texto.splitlines())(expressoes):
        validar_expressao(pilha, expressao)

main4()
exit()






