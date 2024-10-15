### 1. **O que é o projeto?**
Esse projeto é sobre uma empresa de logística que precisa entregar produtos para várias cidades no Brasil. A empresa tem quatro centros de distribuição nas cidades de **Belém**, **Recife**, **São Paulo** e **Curitiba**. O **objetivo** é:
- Achar a melhor rota para os caminhões saírem dos centros de distribuição e fazerem as entregas.
- Reduzir o custo de transporte, seja em termos de **distância percorrida** ou **tempo de viagem**.
- Garantir que as entregas sejam feitas dentro do **prazo**.

### 2. **O que precisamos fazer?**
Precisamos criar um **programa** que:
- Recebe os **dados** das entregas (para onde vão, quanto de carga levam, prazo) e dos caminhões (quantos são, capacidade de carga, quanto tempo podem dirigir por dia).
- Calcula a **rota mais curta e eficiente** para os caminhões, considerando a carga e o tempo disponível.
- Aloca caminhões aos centros de distribuição e decide como será feita cada entrega.

### 3. **Elementos principais (os blocos do sistema)**

#### a) **Centros de Distribuição**
Esses são os pontos de partida para as entregas. Cada centro tem:
- **Caminhões** disponíveis que fazem as entregas.
- **Entregas** que precisam ser feitas para os destinos.

#### Exemplo de código:

```python
class CentroDistribuicao:
    def __init__(self, nome, localizacao):
        self.nome = nome  # Nome do centro (ex: 'Recife')
        self.localizacao = localizacao  # Cidade onde está o centro (ex: 'Recife')
        self.caminhoes = []  # Lista de caminhões disponíveis no centro
        self.entregas = []   # Lista de entregas que o centro precisa realizar

    def adicionar_caminhao(self, caminhao):
        self.caminhoes.append(caminhao)

    def adicionar_entrega(self, entrega):
        self.entregas.append(entrega)
```

#### b) **Caminhões**
Cada caminhão tem uma **capacidade máxima de carga** (quanto peso ele pode carregar) e um **limite de horas** que ele pode dirigir por dia.

#### Exemplo de código:

```python
class Caminhao:
    def __init__(self, capacidade_maxima, horas_operacao):
        self.capacidade_maxima = capacidade_maxima  # Ex: 1000 kg de carga máxima
        self.horas_operacao = horas_operacao  # Ex: 8 horas de operação por dia
        self.carga_atual = 0  # Inicialmente, o caminhão está vazio
        self.tempo_disponivel = horas_operacao  # Tempo restante para dirigir

    def carregar(self, carga):
        # Tenta carregar o caminhão, se a carga não ultrapassar o limite
        if self.carga_atual + carga <= self.capacidade_maxima:
            self.carga_atual += carga
            return True  # Conseguiu carregar
        return False  # Carga excedeu a capacidade
```

#### c) **Entregas**
Cada entrega tem um **destino**, uma **quantidade de carga** a ser transportada e um **prazo** (em dias) para ser entregue.

#### Exemplo de código:

```python
class Entrega:
    def __init__(self, destino, quantidade_carga, prazo):
        self.destino = destino  # Ex: 'Fortaleza'
        self.quantidade_carga = quantidade_carga  # Ex: 500 kg
        self.prazo = prazo  # Prazo em dias (ex: 3 dias para a entrega)
```

#### d) **Mapa de Distâncias (Grafo)**
Vamos criar um "mapa" que mostra as **distâncias entre os centros de distribuição e os destinos**. Isso nos ajuda a calcular as rotas mais curtas para os caminhões.

#### Exemplo de código:

```python
class GrafoDistancias:
    def __init__(self):
        self.adjacencias = {}  # Dicionário onde as chaves são os locais e os valores são listas de destinos e distâncias

    def adicionar_vertice(self, local):
        if local not in self.adjacencias:
            self.adjacencias[local] = []

    def adicionar_aresta(self, origem, destino, distancia):
        # Adiciona a distância entre dois locais (bidirecional)
        self.adjacencias[origem].append((destino, distancia))
        self.adjacencias[destino].append((origem, distancia))
```

### 4. **Como o sistema vai funcionar?**
Aqui está como as etapas do sistema funcionam:

- **Passo 1**: Para cada entrega, o sistema calcula qual é o centro de distribuição mais próximo.
- **Passo 2**: Calculamos a **rota mais curta** para o caminhão fazer a entrega.
- **Passo 3**: O caminhão é **alocado** para a entrega, respeitando sua capacidade e o tempo de operação disponível.

#### Exemplo prático:
Imagine que uma entrega precisa ser feita para **Fortaleza** e o centro de distribuição mais próximo é o de **Recife**. O sistema vai calcular a melhor rota para um caminhão sair de Recife, carregar os produtos e fazer a entrega em Fortaleza, considerando a capacidade e o tempo disponível.

### 5. **Roteamento com o Algoritmo de Dijkstra**
O **algoritmo de Dijkstra** vai ajudar a calcular a **rota mais curta** entre o centro de distribuição e o destino.

#### Exemplo de código:

```python
import heapq  # Biblioteca para usar fila de prioridade

def dijkstra(grafo, origem):
    distancias = {local: float('infinity') for local in grafo.adjacencias}
    distancias[origem] = 0  # A distância do ponto de origem é zero
    fila_prioridade = [(0, origem)]  # Iniciamos com o ponto de origem

    while fila_prioridade:
        distancia_atual, local_atual = heapq.heappop(fila_prioridade)

        for vizinho, distancia in grafo.adjacencias[local_atual]:
            distancia_total = distancia_atual + distancia

            if distancia_total < distancias[vizinho]:
                distancias[vizinho] = distancia_total
                heapq.heappush(fila_prioridade, (distancia_total, vizinho))

    return distancias  # Retorna as distâncias da origem para todos os locais
```

Aqui, o algoritmo de Dijkstra encontra a **rota mais curta** do centro de distribuição até o destino da entrega.

### 6. **Como o sistema é organizado?**
Vamos organizar tudo em pastas e arquivos. Aqui está a estrutura do sistema:

```plaintext
/otimizacao_logistica/           <- O nome da pasta do projeto
│
├── data/                        <- Dados sobre os centros e entregas.
│   ├── centros_distribuicao.csv  <- Lista de centros de distribuição.
│   ├── entregas.csv              <- Lista de entregas com destinos e prazos.
│   └── distancias.csv            <- Um "mapa" com as distâncias entre centros e destinos.
│
├── src/                         <- Código do sistema.
│   ├── main.py                   <- Arquivo principal que faz o sistema funcionar.
|   ├── banco_dados.py            <- Arquivo para lidar com dados dos CSV.
│   ├── centro_distribuicao.py     <- Define como os centros de distribuição funcionam.
│   ├── caminhao.py                <- Define as características dos caminhões.
│   ├── entrega.py                 <- Define como as entregas são organizadas.
│   ├── grafo_distancias.py        <- Cria o "mapa" com as distâncias.
│   ├── roteamento.py              <- Calcula a rota mais curta para cada caminhão.
│   └── simulacao.py               <- Simula diferentes cenários para testar o sistema.
│
└── docs/                        <- Documentação e relatórios.
    ├── relatorio_projeto.pdf      <- Relatório que descreve o que foi feito no projeto.
    └── pitch_video_link.txt       <- Link para o vídeo explicando o projeto.
```

### 7. **Como testar o sistema?**
Vamos testar o sistema simulando diferentes cenários:

- **Cenário 1**: Poucas entregas, para destinos próximos.
- **Cenário 2**: Muitas entregas, para destinos mais distantes.

Avaliações:
- O **tempo** que o sistema leva para calcular as rotas.
- Se as **rotas escolhidas** são eficientes.

### 8. **Integração do `line_profiler` para medir tempo de execução linha por linha**
Uma parte importante de sistemas de logística é **otimizar o tempo de execução**, especialmente ao calcular rotas e alocar caminhões. O **`line_profiler`** é uma ferramenta que mede **quanto tempo cada linha de código leva** para ser executada. Isso é útil para encontrar gargalos de desempenho e otimizar o código.

#### Como instalar:
Primeiro, precisamos instalar a biblioteca `line_profiler`:

```bash
pip install line_profiler
```

#### Exemplo de uso do `line_profiler`:
Vamos adicionar o

 **`line_profiler`** ao nosso código para medir o tempo de execução da função que faz o roteamento das entregas.

```python
from line_profiler import LineProfiler

# Função que queremos perfilhar
def roteamento_e_alocacao(centros_distribuicao, grafo):
    for centro in centros_distribuicao:
        for entrega in centro.entregas:
            distancias = dijkstra(grafo, centro.localizacao)
            print(f"Distância de {centro.localizacao} para {entrega.destino}: {distancias[entrega.destino]} km")

# Criando o profiler
profiler = LineProfiler()

# Adicionando a função para ser monitorada
profiler.add_function(roteamento_e_alocacao)

# Executando a função perfilada
profiler.run('roteamento_e_alocacao(centros_distribuicao, grafo)')

# Exibindo as estatísticas de tempo de execução
profiler.print_stats()
```

O `line_profiler` vai mostrar **quanto tempo cada linha de código na função `roteamento_e_alocacao` está demorando**. Isso ajuda a identificar se há alguma parte específica do código que pode ser otimizada para rodar mais rápido.

Vamos adicionar um arquivo para lidar com o "banco de dados" que, neste caso, será composto por arquivos CSV contendo as informações dos centros de distribuição, entregas e distâncias. O código vai ler e processar esses dados para uso no sistema. Vamos usar a biblioteca `csv` para facilitar a leitura dos arquivos.

### 9. **Arquivo para manipulação dos dados (banco de dados)**

Vamos usar o arquivo chamado **`banco_dados.py`**. Este arquivo será responsável por carregar os dados dos CSV e transformá-los em objetos dentro do sistema, como `CentroDistribuicao`, `Caminhao`, `Entrega` e a construção do `GrafoDistancias`.

### 9.1 **Leitura dos CSV em `banco_dados.py`**

Aqui, vamos implementar a função para ler os arquivos CSV e carregar os dados no sistema. 

#### Exemplo de `banco_dados.py`:

```python
import csv
from centro_distribuicao import CentroDistribuicao
from caminhao import Caminhao
from entrega import Entrega
from grafo_distancias import GrafoDistancias

def carregar_centros(filename):
    centros = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            centro = CentroDistribuicao(row['nome'], row['localizacao'])
            centros.append(centro)
    return centros

def carregar_caminhoes(filename, centros):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            caminhao = Caminhao(int(row['capacidade_maxima']), int(row['horas_operacao']))
            for centro in centros:
                if centro.nome == row['centro_nome']:
                    centro.adicionar_caminhao(caminhao)
                    break

def carregar_entregas(filename, centros):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            entrega = Entrega(row['destino'], int(row['quantidade_carga']), int(row['prazo']))
            for centro in centros:
                if centro.nome == row['centro_nome']:
                    centro.adicionar_entrega(entrega)
                    break

def carregar_grafo_distancias(filename):
    grafo = GrafoDistancias()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            grafo.adicionar_vertice(row['origem'])
            grafo.adicionar_vertice(row['destino'])
            grafo.adicionar_aresta(row['origem'], row['destino'], int(row['distancia']))
    return grafo
```

### 9.2 **Exemplo dos arquivos CSV**

#### **`centros_distribuicao.csv`**:
Este arquivo contém os centros de distribuição com seus nomes e locais.

```plaintext
nome,localizacao
Recife,Recife
São Paulo,São Paulo
Curitiba,Curitiba
Belém,Belém
```

#### **`caminhoes.csv`**:
Este arquivo relaciona os caminhões aos centros de distribuição e define sua capacidade e horas de operação.

```plaintext
centro_nome,capacidade_maxima,horas_operacao
Recife,1000,8
São Paulo,2000,10
Curitiba,1500,9
Belém,1200,8
```

#### **`entregas.csv`**:
Este arquivo contém as entregas a serem feitas, incluindo o centro de origem, o destino, a quantidade de carga e o prazo.

```plaintext
centro_nome,destino,quantidade_carga,prazo
Recife,Fortaleza,500,3
São Paulo,Rio de Janeiro,800,2
Curitiba,Porto Alegre,700,4
Belém,Manaus,600,5
```

#### **`distancias.csv`**:
Este arquivo contém a matriz de distâncias entre os centros e os destinos.

```plaintext
origem,destino,distancia
Recife,Fortaleza,800
São Paulo,Rio de Janeiro,400
Curitiba,Porto Alegre,600
Belém,Manaus,900
```

### 9.3 **Exemplo de uso**

Agora, vamos mostrar como usar as funções de **`banco_dados.py`** para carregar os dados no sistema e executar uma simulação:

```python
from banco_dados import carregar_centros, carregar_caminhoes, carregar_entregas, carregar_grafo_distancias

# Carregar dados dos CSV
centros = carregar_centros('data/centros_distribuicao.csv')
carregar_caminhoes('data/caminhoes.csv', centros)
carregar_entregas('data/entregas.csv', centros)
grafo = carregar_grafo_distancias('data/distancias.csv')

# Agora temos os centros, caminhões, entregas e grafo prontos para uso
# Podemos então rodar as funções de roteamento e simulação
```

### 9.4 **Explicação**
- **`carregar_centros`**: Lê o arquivo CSV dos centros de distribuição e cria objetos `CentroDistribuicao`.
- **`carregar_caminhoes`**: Associa caminhões a cada centro de distribuição.
- **`carregar_entregas`**: Cria objetos `Entrega` e associa cada um a um centro.
- **`carregar_grafo_distancias`**: Constrói o grafo de distâncias entre os centros de distribuição e os destinos.

### 10. **Conclusão**
Esse projeto visa otimizar o transporte de produtos de uma empresa, garantindo que os caminhões façam as entregas de maneira eficiente, dentro do prazo e com o menor custo possível. Estamos criando um sistema que faz todos esses cálculos de forma automática, com base em dados de entregas e rotas e mantendo persistência de dados.