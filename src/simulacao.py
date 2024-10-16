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
        if dia < 1 or dia > self.dias_simulacao:
            logging.error(f"Dia {dia} é inválido. O dia deve estar entre 1 e {self.dias_simulacao}.")
            return

        if dia not in self.entregas_por_dia:
            self.entregas_por_dia[dia] = []
        self.entregas_por_dia[dia].append(entrega)
        logging.info(f"Entrega adicionada ao dia {dia}: {entrega}")

    def executar_simulacao(self):
        for dia in range(1, self.dias_simulacao + 1):
            logging.info(f"Iniciando simulação do dia {dia}")
            self.simular_dia(dia)
        self.gerar_relatorio_final()


    def simular_dia(self, dia: int):
        entregas_do_dia = self.entregas_por_dia.get(dia, [])
        if not entregas_do_dia:
            logging.info(f"Sem entregas para o dia {dia}.")
            return

        roteamento = Roteamento(self.grafo, self.centros)
        logging.info(f"{len(entregas_do_dia)} entregas para o dia {dia}. Roteamento em andamento...")

        for entrega in entregas_do_dia:
            try:
                centro_mais_proximo = roteamento.encontrar_centro_mais_proximo(entrega.destino)
                roteamento.adicionar_entrega(entrega, centro_mais_proximo)
            except ValueError as e:
                logging.error(f"Erro ao encontrar centro para entrega {entrega}: {e}")
                continue

        rotas_otimizadas = roteamento.alocar_entregas()

        for centro, rotas in rotas_otimizadas.items():
            for rota in rotas:
                num_entregas = len(rota.entregas)
                self.estatisticas['entregas_realizadas'] += num_entregas
                self.estatisticas['distancia_total'] += rota.distancia_total
                entregas_atrasadas = sum(1 for e in rota.entregas if e.esta_atrasada())
                self.estatisticas['entregas_atrasadas'] += entregas_atrasadas

                logging.info(f"Centro: {centro.nome} | Rota: {rota} | "
                             f"Entregas: {num_entregas} | Atrasadas: {entregas_atrasadas}")

    def gerar_relatorio_final(self):
        total_entregas = self.estatisticas['entregas_realizadas']
        total_atrasadas = self.estatisticas['entregas_atrasadas']
        distancia_total = self.estatisticas['distancia_total']

        logging.info("Relatório Final da Simulação:")
        logging.info(f"Total de dias simulados: {self.dias_simulacao}")
        logging.info(f"Total de entregas realizadas: {total_entregas}")
        logging.info(f"Distância total percorrida: {distancia_total} km")
        logging.info(f"Número de entregas atrasadas: {total_atrasadas}")

        if total_entregas > 0:
            eficiencia = (total_entregas - total_atrasadas) / total_entregas * 100
            logging.info(f"Eficiência do sistema: {eficiencia:.2f}%")
        else:
            logging.info("Nenhuma entrega foi realizada durante a simulação.")