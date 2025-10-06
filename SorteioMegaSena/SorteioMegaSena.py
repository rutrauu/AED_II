import csv
import time
import requests
from typing import List, Optional
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

# --- Módulo 1: Modelo de Dados ---

class ResultadoSorteio:
    """
    Classe para armazenar os dados de um único sorteio da Mega-Sena.
    As dezenas são sempre mantidas em ordem crescente internamente.
    """
    def __init__(self, concurso: int, dezenas: List[int]):
        if len(dezenas) != 6:
            raise ValueError("Um resultado da Mega-Sena deve ter 6 dezenas.")
        
        self.concurso = concurso
        # Garante que as dezenas de um mesmo sorteio estejam sempre ordenadas
        self.dezenas = sorted(dezenas)

    def __repr__(self):
        """Representação textual do objeto para debug."""
        return f"Concurso {self.concurso}: {self.dezenas}"

    def formatar_saida(self) -> str:
        """Formata a saída conforme o padrão solicitado."""
        dezenas_formatadas = [f"{dezena:02d}" for dezena in self.dezenas]
        return f"[{','.join(dezenas_formatadas)}] - {self.concurso}"

# --- Módulo 2: Acesso aos Dados ---

class MegaSenaAPI:
    """
    Responsável por baixar e processar os dados dos sorteios.
    Esta versão está otimizada para baixar apenas os últimos 100 concursos.
    """
    API_URL_BASE = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"

    def baixar_ultimos_100_resultados(self) -> Optional[List[ResultadoSorteio]]:
        """
        Baixa os últimos 100 resultados da Mega-Sena, consultando
        cada concurso individualmente.
        """
        print("Iniciando o download dos últimos 100 sorteios da Mega-Sena...")
        
        try:
            # 1. Obter o último concurso para saber onde começar
            print("Verificando o número do último concurso...")
            response_ultimo = requests.get(self.API_URL_BASE, verify=False)
            response_ultimo.raise_for_status()
            ultimo_concurso_num = response_ultimo.json().get('numero')

            if not ultimo_concurso_num:
                print("Não foi possível determinar o número do último concurso.")
                return None
            
            # --- PONTO CHAVE DA MUDANÇA ---
            # Define o ponto de partida para o loop
            primeiro_concurso_a_buscar = ultimo_concurso_num - 99
            
            print(f"O último concurso é o {ultimo_concurso_num}. Baixando do concurso {primeiro_concurso_a_buscar} em diante.")

            # 2. Fazer o loop para baixar os últimos 100
            todos_resultados = []
            # O loop agora começa do número calculado
            for i in range(primeiro_concurso_a_buscar, ultimo_concurso_num + 1):
                print(f"Baixando concurso {i}/{ultimo_concurso_num}...")
                url_concurso = f"{self.API_URL_BASE}/{i}"
                
                try:
                    response = requests.get(url_concurso, verify=False)
                    if response.status_code != 200:
                        print(f"  -> Falha ao baixar o concurso {i}, pulando.")
                        continue

                    sorteio_data = response.json()
                    concurso = sorteio_data.get('numero')
                    dezenas_str = sorteio_data.get('listaDezenas', [])
                    
                    dezenas_int = [int(d) for d in dezenas_str]

                    if concurso and len(dezenas_int) == 6:
                        resultado = ResultadoSorteio(concurso=concurso, dezenas=dezenas_int)
                        todos_resultados.append(resultado)
                    
                    time.sleep(0.05)

                except requests.exceptions.RequestException as e:
                    print(f"  -> Erro de conexão no concurso {i}: {e}, pulando.")
                    continue
            
            print(f"\n{len(todos_resultados)} sorteios foram baixados e processados com sucesso.")
            return todos_resultados

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API da Mega-Sena: {e}")
            return None
        except (ValueError, KeyError) as e:
            print(f"Erro ao processar os dados JSON recebidos: {e}")
            return None


class RadixSortMegaSena:
    """
    Implementa o Radix Sort adaptado para ordenar listas de resultados da Mega-Sena.
    """
    def __init__(self, resultados: List[ResultadoSorteio]):
        self.resultados = resultados
        # Os números da Mega-Sena vão de 1 a 60
        self._range_max = 60

    def _counting_sort_por_coluna(self, dados: List[ResultadoSorteio], coluna: int):
        """
        Ordena a lista de resultados com base em uma "coluna" (índice da dezena).
        Utiliza Counting Sort, que é um algoritmo estável.
        """
        n = len(dados)
        saida = [None] * n
        contagem = [0] * (self._range_max + 1) # Índices de 0 a 60

        # 1. Contar a frequência de cada número na coluna especificada
        for i in range(n):
            numero_dezena = dados[i].dezenas[coluna]
            contagem[numero_dezena] += 1

        # 2. Fazer a contagem cumulativa para saber a posição final
        for i in range(1, self._range_max + 1):
            contagem[i] += contagem[i-1]

        # 3. Construir a lista de saída, garantindo a estabilidade
        i = n - 1
        while i >= 0:
            resultado_atual = dados[i]
            numero_dezena = resultado_atual.dezenas[coluna]
            
            posicao_saida = contagem[numero_dezena] - 1
            saida[posicao_saida] = resultado_atual
            contagem[numero_dezena] -= 1
            i -= 1
        
        return saida

    def sort(self) -> List[ResultadoSorteio]:
        print("\nIniciando a ordenação com Radix Sort...")
        
        dados_para_ordenar = list(self.resultados)
        num_dezenas = 6

        # Itera da dezena menos significativa (índice 5) para a mais significativa (índice 0)
        for i in range(num_dezenas - 1, -1, -1):
            print(f"Ordenando pela {i+1}ª dezena...")
            dados_para_ordenar = self._counting_sort_por_coluna(dados_para_ordenar, coluna=i)
        
        print("Ordenação concluída!")
        self.resultados = dados_para_ordenar
        return self.resultados
    
def exportar_para_csv(resultados: List[ResultadoSorteio], nome_arquivo: str):
    """
    Exporta a lista de resultados da Mega-Sena para um arquivo CSV.
    Args:
        resultados: A lista de objetos ResultadoSorteio a ser exportada.
        nome_arquivo: O nome do arquivo CSV a ser criado (ex: 'dados.csv').
    """
    print(f"\nIniciando a exportação para o arquivo '{nome_arquivo}'...")
    
    # Define o cabeçalho do arquivo CSV
    cabecalho = ['Concurso', 'Dezena1', 'Dezena2', 'Dezena3', 'Dezena4', 'Dezena5', 'Dezena6']

    try:
        # Abre o arquivo no modo de escrita ('w')
        # newline='' evita que linhas em branco sejam criadas no Windows
        # encoding='utf-8' garante a compatibilidade com caracteres especiais
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            # Cria um "escritor" de CSV
            escritor_csv = csv.writer(arquivo_csv, delimiter=';')

            # Escreve a primeira linha, que é o cabeçalho
            escritor_csv.writerow(cabecalho)

            # Itera sobre cada resultado e escreve uma linha no arquivo
            for resultado in resultados:
                # Cria a linha de dados. O '*' desempacota a lista de dezenas.
                linha = [resultado.concurso, *resultado.dezenas]
                escritor_csv.writerow(linha)

        print(f"Dados exportados com sucesso para '{nome_arquivo}'!")

    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}")

# --- Módulo 4: Execução Principal ---

if __name__ == "__main__":
    # 1. Baixar os dados
    api = MegaSenaAPI()
    ultimos_100_resultados = api.baixar_ultimos_100_resultados()

    if ultimos_100_resultados:
        sorter = RadixSortMegaSena(ultimos_100_resultados)
        resultados_ordenados = sorter.sort()

        print("\n--- Últimos 100 Resultados da Mega-Sena Ordenados ---\n")
        for resultado in resultados_ordenados:
            print(resultado.formatar_saida())

        nome_do_arquivo = 'resultados_megasena.csv'
        exportar_para_csv(resultados_ordenados, nome_do_arquivo)