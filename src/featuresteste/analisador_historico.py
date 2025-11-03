import pdfplumber
import sys


class AnalisadorHistorico:

    def __init__(self, disciplina):

        self.disciplina_alvo = disciplina

        # Estes são os "mapas" que definem o que procurar
        self.config = {
            "horas_cursadas": {
                "keyword": "Carga Horária Total",
                "index": 2,
                "valor": 0,
                "valor_min": 800.0,
            },
            "cr_especifico": {
                "keyword": self.disciplina_alvo,
                "index": 7,
                "valor": 0,
                "valor_min": 8.0,
            },
            "cr_periodo_soma": {
                "keyword": "C.R. do Período:",
                "index": 8,
                "valor": 0,
                "count": 0,
            },
            "cr_geral": {"valor": 0.0, "valor_min": 7.0},
        }

    # --- Leitura do PDF ---

    @staticmethod
    def ler_tabelas(caminho_pdf):
        with pdfplumber.open(caminho_pdf) as pdf:
            tabelas = []

            for i in range(len(pdf.pages)):
                pagina_atual = pdf.pages[i]
                tabelas += pagina_atual.extract_tables()

            if not tabelas:
                raise ValueError

            return tabelas

    # --- Extração dos dados ---

    @staticmethod
    def tratar_valor( elemento):
        return float(elemento.replace(",", "."))

    def procura_keyword(self, linha, mapa):
        if mapa["keyword"] in linha:
            return True
        return False

    def extrair_dados_linha(self, linha, mapa, adicionar=False):
        possui_keyword = self.procura_keyword(linha, mapa)

        if possui_keyword:
            elemento_tratado = self.tratar_valor(linha[mapa["index"]])

            if adicionar:
                mapa["valor"] += elemento_tratado
                mapa["count"] += 1
            else:
                mapa["valor"] = elemento_tratado

    def extrair_cr_geral(self):
        cr_periodo_soma = self.config["cr_periodo_soma"]
        cr_geral = self.config["cr_geral"]

        cr_geral["valor"] = cr_periodo_soma["valor"] / cr_periodo_soma["count"]

    # Função principal
    def extrair_dados_tabelas(self, tabelas):
        for tabela in tabelas:
            for linha in tabela:
                self.extrair_dados_linha(linha, self.config["horas_cursadas"])
                self.extrair_dados_linha(linha, self.config["cr_especifico"])
                self.extrair_dados_linha(linha, self.config["cr_periodo_soma"], True)
        self.extrair_cr_geral()

    # --- Análise dos dados ---

    @staticmethod
    def valor_suficiente(mapa):
        if mapa["valor"] >= mapa["valor_min"]:
            return True
        return False

    def candidato_apto(self):
        horas_cursadas = self.config["horas_cursadas"]
        cr_especifico = self.config["cr_especifico"]
        cr_geral = self.config["cr_geral"]

        return (
            self.valor_suficiente(horas_cursadas)
            and self.valor_suficiente(cr_especifico)
            and self.valor_suficiente(cr_geral)
        )
    

