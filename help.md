Pelo que li no PDF falta isso:

1. Aprimorar a classe Simulacao
2. Melhorar o algoritmo de roteamento
3. Considerar os limites de tempo de operação dos caminhões
4. Adicionar relatórios e análise de desempenho

Fiz essas alterações:

1. Aprimorando a classe Simulacao:

```python
import logging
from typing import List, Dict
from centro_distribuicao import CentroDistribuicao
from entrega import Entrega
from grafo_distancias import GrafoDistancia
from roteamento import Roteamento

class Simulacao:
    def __init__(self, grafo: GrafoDistancia, centros: List[CentroDistribuicao], dias_simulacao: int):
        self.grafo = grafo
        self.centros = centros
        self.dias_simulacao = dias_simulacao
        self.entregas_por_dia: Dict[int, List[Entrega]] = {}
        self.estatisticas = {
            'entregas_realizadas': 0,
            'distancia_total': 0,
            'entregas_atrasadas': 0
        }

    def adicionar_entrega(self, entrega: Entrega, dia: int):
        if dia not in self.entregas_por_dia:
            self.entregas_por_dia[dia] = []
        self.entregas_por_dia[dia].append(entrega)

    def executar_simulacao(self):
        for dia in range(1, self.dias_simulacao + 1):
            logging.info(f"Iniciando simulação do dia {dia}")
            self.simular_dia(dia)
        self.gerar_relatorio_final()

    def simular_dia(self, dia: int):
        entregas_do_dia = self.entregas_por_dia.get(dia, [])
        roteamento = Roteamento(self.grafo, self.centros)
        
        for entrega in entregas_do_dia:
            centro_mais_proximo = roteamento.encontrar_centro_mais_proximo(entrega.destino)
            roteamento.adicionar_entrega(entrega, centro_mais_proximo)

        rotas_otimizadas = roteamento.alocar_entregas()
        
        for centro, rotas in rotas_otimizadas.items():
            for rota in rotas:
                self.estatisticas['entregas_realizadas'] += len(rota.entregas)
                self.estatisticas['distancia_total'] += rota.distancia_total
                self.estatisticas['entregas_atrasadas'] += sum(1 for e in rota.entregas if e.esta_atrasada())

    def gerar_relatorio_final(self):
        logging.info("Relatório Final da Simulação:")
        logging.info(f"Total de dias simulados: {self.dias_simulacao}")
        logging.info(f"Total de entregas realizadas: {self.estatisticas['entregas_realizadas']}")
        logging.info(f"Distância total percorrida: {self.estatisticas['distancia_total']} km")
        logging.info(f"Número de entregas atrasadas: {self.estatisticas['entregas_atrasadas']}")
        eficiencia = (self.estatisticas['entregas_realizadas'] - self.estatisticas['entregas_atrasadas']) / self.estatisticas['entregas_realizadas'] * 100
        logging.info(f"Eficiência do sistema: {eficiencia:.2f}%")

```

2. Melhorando o algoritmo de roteamento:

```python
from typing import List, Dict
from centro_distribuicao import CentroDistribuicao
from entrega import Entrega
from grafo_distancias import GrafoDistancia
from caminhao import Caminhao

class Rota:
    def __init__(self, caminhao: Caminhao):
        self.caminhao = caminhao
        self.entregas: List[Entrega] = []
        self.distancia_total = 0

    def adicionar_entrega(self, entrega: Entrega, distancia: int):
        self.entregas.append(entrega)
        self.distancia_total += distancia

class Roteamento:
    def __init__(self, grafo: GrafoDistancia, centros: List[CentroDistribuicao]):
        self.grafo = grafo
        self.centros = centros

    def encontrar_centro_mais_proximo(self, destino: str) -> CentroDistribuicao:
        centro_mais_proximo = None
        menor_distancia = float('inf')

        for centro in self.centros:
            distancia = self.grafo.encontrarRotaMaisCurta(centro.cidade, destino)[1]
            if distancia < menor_distancia:
                menor_distancia = distancia
                centro_mais_proximo = centro

        return centro_mais_proximo

    def adicionar_entrega(self, entrega: Entrega, centro: CentroDistribuicao):
        centro.adicionar_entrega(entrega)

    def alocar_entregas(self) -> Dict[CentroDistribuicao, List[Rota]]:
        rotas_por_centro: Dict[CentroDistribuicao, List[Rota]] = {centro: [] for centro in self.centros}

        for centro in self.centros:
            entregas_ordenadas = sorted(centro.entregas, key=lambda e: e.prazo)
            
            for entrega in entregas_ordenadas:
                rota_alocada = False
                for rota in rotas_por_centro[centro]:
                    if rota.caminhao.pode_adicionar_entrega(entrega):
                        distancia = self.grafo.encontrarRotaMaisCurta(rota.caminhao.localizacaoAtual, entrega.destino)[1]
                        rota.adicionar_entrega(entrega, distancia)
                        rota.caminhao.adicionar_entrega(entrega)
                        rota_alocada = True
                        break
                
                if not rota_alocada:
                    for caminhao in centro.caminhoes:
                        if caminhao.esta_disponivel() and caminhao.pode_adicionar_entrega(entrega):
                            nova_rota = Rota(caminhao)
                            distancia = self.grafo.encontrarRotaMaisCurta(caminhao.localizacaoAtual, entrega.destino)[1]
                            nova_rota.adicionar_entrega(entrega, distancia)
                            caminhao.adicionar_entrega(entrega)
                            rotas_por_centro[centro].append(nova_rota)
                            break

        return rotas_por_centro

```

3. Considerando os limites de tempo de operação dos caminhões:

```python
class Caminhao:
    def __init__(self, idCaminhao: int, capacidade: int, horas_operacao_max: int):
        self.idCaminhao = idCaminhao
        self.capacidade = capacidade
        self.horas_operacao_max = horas_operacao_max
        self.localizacaoAtual = None
        self.carga_atual = 0
        self.horas_operacao_atual = 0
        self.disponivel = True

    def adicionar_entrega(self, entrega: Entrega):
        self.carga_atual += entrega.quantidade_carga
        self.horas_operacao_atual += self.estimar_tempo_entrega(entrega)
        self.localizacaoAtual = entrega.destino

    def pode_adicionar_entrega(self, entrega: Entrega) -> bool:
        carga_total = self.carga_atual + entrega.quantidade_carga
        horas_total = self.horas_operacao_atual + self.estimar_tempo_entrega(entrega)
        return carga_total <= self.capacidade and horas_total <= self.horas_operacao_max

    def estimar_tempo_entrega(self, entrega: Entrega) -> int:
        # Este é um método simplificado. Na prática, você usaria o GrafoDistancia
        # para calcular o tempo real baseado na distância.
        return 2

    def esta_disponivel(self) -> bool:
        return self.disponivel and self.horas_operacao_atual < self.horas_operacao_max

    def resetar_dia(self):
        self.carga_atual = 0
        self.horas_operacao_atual = 0
        self.disponivel = True

```

4. Adicionando relatórios e análise de desempenho:

Já incluí algumas estatísticas básicas na classe Simulacao aprimorada. Para uma análise mais detalhada adicionei uma classe separada para relatórios:

```python
from typing import Dict, List
from centro_distribuicao import CentroDistribuicao
from roteamento import Rota
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

class Relatorio:
    def __init__(self, dias_simulacao: int, centros: List[CentroDistribuicao]):
        self.dias_simulacao = dias_simulacao
        self.centros = centros
        self.estatisticas_por_dia: Dict[int, Dict] = {}

    def registrar_dia(self, dia: int, rotas_por_centro: Dict[CentroDistribuicao, List[Rota]]):
        estatisticas_dia = {
            'entregas_realizadas': 0,
            'distancia_total': 0,
            'entregas_atrasadas': 0,
            'utilizacao_caminhoes': {}
        }

        for centro, rotas in rotas_por_centro.items():
            for rota in rotas:
                estatisticas_dia['entregas_realizadas'] += len(rota.entregas)
                estatisticas_dia['distancia_total'] += rota.distancia_total
                estatisticas_dia['entregas_atrasadas'] += sum(1 for e in rota.entregas if e.esta_atrasada())
                
                utilizacao = (rota.caminhao.carga_atual / rota.caminhao.capacidade) * 100
                estatisticas_dia['utilizacao_caminhoes'][rota.caminhao.idCaminhao] = utilizacao

        self.estatisticas_por_dia[dia] = estatisticas_dia

    def gerar_relatorio_final(self, file_path="../docs/relatorio_simulacao.pdf"):
        total_entregas = sum(dia['entregas_realizadas'] for dia in self.estatisticas_por_dia.values())
        total_distancia = sum(dia['distancia_total'] for dia in self.estatisticas_por_dia.values())
        total_atrasos = sum(dia['entregas_atrasadas'] for dia in self.estatisticas_por_dia.values())

        eficiencia = (total_entregas - total_atrasos) / total_entregas * 100 if total_entregas > 0 else 0
        media_utilizacao_caminhoes = self.calcular_media_utilizacao_caminhoes()

        c = canvas.Canvas(file_path, pagesize=letter)
        c.drawString(100, 750, f"Relatório Final Detalhado da Simulação:")
        c.drawString(100, 730, f"Total de dias simulados: {self.dias_simulacao}")
        c.drawString(100, 710, f"Total de entregas realizadas: {total_entregas}")
        c.drawString(100, 690, f"Distância total percorrida: {total_distancia:.2f} km")
        c.drawString(100, 670, f"Número total de entregas atrasadas: {total_atrasos}")
        c.drawString(100, 650, f"Eficiência geral do sistema: {eficiencia:.2f}%")
        c.drawString(100, 630, f"Utilização média dos caminhões: {media_utilizacao_caminhoes:.2f}%")

        self.gerar_grafico_entregas_por_dia(file_path)

        c.showPage()
        c.drawImage("grafico_entregas_por_dia.png", 100, 400, width=400, height=300)
        c.save()

        os.remove("./temp/grafico_entregas_por_dia.png")

    def calcular_media_utilizacao_caminhoes(self) -> float:
        total_utilizacao = 0
        total_caminhoes = 0
        for dia in self.estatisticas_por_dia.values():
            total_utilizacao += sum(dia['utilizacao_caminhoes'].values())
            total_caminhoes += len(dia['utilizacao_caminhoes'])
        return total_utilizacao / total_caminhoes if total_caminhoes > 0 else 0

    def gerar_grafico_entregas_por_dia(self, file_path: str):
        dias = list(self.estatisticas_por_dia.keys())
        entregas = [dia['entregas_realizadas'] for dia in self.estatisticas_por_dia.values()]

        plt.figure(figsize=(10, 6))
        plt.plot(dias, entregas, marker='o', linestyle='-', color='b', label='Entregas por Dia')
        
        plt.title('Entregas Realizadas por Dia')
        plt.xlabel('Dia')
        plt.ylabel('Número de Entregas')
        plt.grid(True)
        
        plt.legend()

        plt.savefig("./temp/grafico_entregas_por_dia.png")
        plt.close()
```

Estas melhorias abordam os principais pontos. Essas foram as mudanças:

1. A classe `Simulacao` agora suporta múltiplos dias de simulação e múltiplos centros de distribuição.
2. O `Roteamento` foi melhorado para considerar múltiplos centros e escolher o mais próximo para cada entrega.
3. A classe `Caminhao` agora considera as horas de operação e tem métodos para verificar se pode adicionar mais entregas.
4. Uma nova classe `Relatorio` foi adicionada para gerar análises detalhadas do desempenho do sistema.

Para finalizar o projeto, você precisará integrar essas classes atualizadas na main, garantir que todas as partes do sistema estejam funcionando corretamente juntas, e adicionar testes unitários para validar o comportamento do sistema.

Além disso dá para criar uma interface de terminal para facilitar a utilização