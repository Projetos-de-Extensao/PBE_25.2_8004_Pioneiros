import pdfplumber
from .models import Vaga

class AnalisadorHistorico:

    def __init__(self, vaga_recebida: Vaga):

        self.vaga_alvo = vaga_recebida.disciplina.nome.upper()

        self.config = {
            "horas_cursadas": {
                "keyword": "Carga Horária Total",
                "index": 2,
                "valor": 0,
                "valor_min": 800.0,
            },
            "cr_especifico": {
                "keyword": self.vaga_alvo,
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

    @staticmethod
    def ler_tabelas(url_pdf):
        try:
            with pdfplumber.open(url_pdf) as pdf:
                tabelas = []
                for page in pdf.pages:
                    tabelas_pagina = page.extract_tables()
                    if tabelas_pagina:
                        tabelas.extend(tabelas_pagina)
                    
            if not tabelas:
                print(f"AVISO: Nenhuma tabela encontrada no PDF: {url_pdf}")
                return []
                    
            return tabelas
        except Exception as e:
            print(f"ERRO ao ler PDF: {e}")
            return []

    @staticmethod
    def tratar_valor(elemento):
        if elemento is None:
            return 0.0
        try:
            return float(elemento.strip().replace(",", "."))
        except (ValueError, TypeError):
            return 0.0

    def procura_keyword(self, linha, mapa):
        if not mapa.get("keyword"):
            return False
        
        linha_texto = " ".join(filter(None, linha))
        
        if mapa["keyword"] in linha_texto:
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
        else:
            return

    def extrair_cr_geral(self):
        cr_periodo_soma = self.config["cr_periodo_soma"]
        cr_geral = self.config["cr_geral"]

        cr_geral["valor"] = cr_periodo_soma["valor"] / cr_periodo_soma["count"]

    def extrair_dados_tabelas(self, tabelas):
        for tabela in tabelas:
            for linha in tabela:
                self.extrair_dados_linha(linha, self.config["horas_cursadas"])
                self.extrair_dados_linha(linha, self.config["cr_especifico"])
                self.extrair_dados_linha(linha, self.config["cr_periodo_soma"], True)
        self.extrair_cr_geral()

    @staticmethod
    def valor_suficiente(mapa):
        if mapa["valor"] >= mapa["valor_min"]:
            return True
        return False

    def candidato_apto(self):
        horas_cursadas = self.config["horas_cursadas"]
        cr_especifico = self.config["cr_especifico"]
        cr_geral = self.config["cr_geral"]

        print(f"Horas: {horas_cursadas['valor']} (Min: {horas_cursadas['valor_min']})")
        print(f"CR Específico: {cr_especifico['valor']} (Min: {cr_especifico['valor_min']})")
        print(f"CR Geral: {cr_geral['valor']} (Min: {cr_geral['valor_min']})")

        return (
            self.valor_suficiente(horas_cursadas)
            and self.valor_suficiente(cr_especifico)
            and self.valor_suficiente(cr_geral)
        )
    

    def analisar_e_decidir(self, url_pdf: str) -> str:
        print(f"Iniciando análise do PDF: {url_pdf}")
        
        tabelas = self.ler_tabelas(url_pdf)
        if not tabelas:
            print("Análise falhou: PDF sem tabelas ou ilegível.")
            return "PENDENTE" 


        self.extrair_dados_tabelas(tabelas)
        
        if self.candidato_apto():
            print("Resultado: APROVADO (automaticamente)")
            return "APROVADO"
        else:
            print("Resultado: PENDENTE (critérios não atingidos)")
            return "PENDENTE"