from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Projeto de Otimização Logística com Múltiplos Centros de Distribuição", ln=True, align='C')

pdf.ln(10)
pdf.set_font("Arial", size=10)
intro_text = (
    "Este projeto visa desenvolver uma solução para otimizar o processo de entrega de produtos "
    "por uma empresa de logística que opera em várias cidades do Brasil. A empresa possui quatro "
    "centros de distribuição localizados em Belém, Recife, São Paulo e Curitiba. O objetivo é minimizar "
    "o custo de transporte, garantindo que todas as entregas sejam realizadas dentro do prazo estipulado."
)
pdf.multi_cell(0, 10, intro_text)

pdf.ln(5)
pdf.set_font("Arial", 'B', size=10)
pdf.cell(0, 10, "Objetivos", ln=True)

pdf.set_font("Arial", size=10)
objectives_text = (
    "- Determinar a melhor rota para os caminhões que partem dos centros de distribuição e realizam as entregas.\n"
    "- Reduzir o custo total de transporte, levando em consideração a distância percorrida e o tempo de viagem.\n"
    "- Garantir que todas as entregas sejam efetuadas dentro do prazo."
)
pdf.multi_cell(0, 10, objectives_text)

pdf.ln(5)
pdf.set_font("Arial", 'B', size=10)
pdf.cell(0, 10, "Estrutura do Sistema", ln=True)

pdf.set_font("Arial", size=10)
structure_text = (
    "O sistema é composto pelos seguintes elementos principais:\n"
    "- Centros de Distribuição\n"
    "- Caminhões\n"
    "- Entregas\n"
    "- Mapa de Distâncias"
)
pdf.multi_cell(0, 10, structure_text)

pdf.ln(5)
pdf.set_font("Arial", 'B', size=10)
pdf.cell(0, 10, "Estrutura de Arquivos", ln=True)

pdf.set_font("Courier", size=10)
file_structure = (
"/otimizacao_logistica/           <- O nome da pasta do projeto\n"
"|\n"
"|-- data/                        <- Dados sobre os centros e entregas.\n"
"|   |-- centros_distribuicao.csv  <- Lista de centros de distribuição.\n"
"|   |-- entregas.csv              <- Lista de entregas com destinos e prazos.\n"
"|   `-- distancias.csv            <- Um 'mapa' com as distâncias entre centros e destinos.\n"
"|\n"
"|-- src/                         <- Código do sistema.\n"
"|   |-- main.py                   <- Arquivo principal que faz o sistema funcionar.\n"
"|   |-- banco_dados.py            <- Arquivo para lidar com dados dos CSV.\n"
"|   |-- centro_distribuicao.py     <- Define como os centros de distribuição funcionam.\n"
"|   |-- caminhao.py                <- Define as características dos caminhões.\n"
"|   |-- entrega.py                 <- Define como as entregas são organizadas.\n"
"|   |-- grafo_distancias.py        <- Cria o 'mapa' com as distâncias.\n"
"|   |-- roteamento.py              <- Calcula a rota mais curta para cada caminhão.\n"
"|   `-- simulacao.py               <- Simula diferentes cenários para testar o sistema.\n"
"|\n"
"`-- docs/                        <- Documentação e relatórios.\n"
"    |-- relatorio_projeto.pdf      <- Relatório que descreve o que foi feito no projeto.\n"
"    `-- pitch_video_link.txt       <- Link para o vídeo explicando o projeto."
)
pdf.multi_cell(0, 10, file_structure)

pdf_output_path = "./docs/projeto_otimizacao_logistica.pdf"
pdf.output(pdf_output_path)