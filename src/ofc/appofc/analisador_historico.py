import pdfplumber
from .models import Vaga, Aluno
from django.contrib.auth.models import User
import re


class AnalisadorHistorico:

    def __init__(self, vaga_recebida: Vaga, aluno_recebido: Aluno):

        self.vaga_alvo = vaga_recebida.disciplina.nome.upper()

        self.matricula_alvo = aluno_recebido.matricula

        self.matricula_encontrada_no_pdf = False

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

    def ler_tabelas_academicas(self, url_pdf):
        try:
            with pdfplumber.open(url_pdf) as pdf:
                tabelas = []
                for page in pdf.pages:
                    tabelas_pagina = page.extract_tables()
                    if tabelas_pagina:
                        tabelas.extend(tabelas_pagina[1:]) 
                
                if not tabelas:
                    print(f"AVISO: Nenhuma tabela de NOTAS encontrada no PDF: {url_pdf}")
                    return []
                return tabelas
        except Exception as e:
            print(f"ERRO ao ler tabelas do PDF: {e}")
            return []

    def ler_texto_cabecalho(self, url_pdf):
        try:
            with pdfplumber.open(url_pdf) as pdf:
                primeira_pagina = pdf.pages[0]
                return primeira_pagina.extract_text()
        except Exception as e:
            print(f"ERRO ao extrair texto do PDF: {e}")
            return None

    def verificar_matricula_pdf(self, texto_cabecalho: str):
        keyword_label = "Matrícula:"
        
        if not texto_cabecalho:
            print("AVISO: Não foi possível ler o texto do cabeçalho.")
            return 


        if keyword_label in texto_cabecalho:
            numeros_no_texto = "".join(re.findall(r'\d+', texto_cabecalho))
    
            if self.matricula_alvo in numeros_no_texto:
                self.matricula_encontrada_no_pdf = True
                print(f"INFO: Matrícula {self.matricula_alvo} encontrada no cabeçalho.")
                return
        
        print(f"AVISO: Matrícula {self.matricula_alvo} NÃO encontrada no cabeçalho.")
        self.matricula_encontrada_no_pdf = False
    
    @staticmethod
    def tratar_valor(elemento):
        if elemento is None:
            return 0.0
        try:
            return float(elemento.strip().replace(",", "."))
        except (ValueError, TypeError):
            return 0.0

    def procura_keyword(self, linha: list, mapa: dict) -> bool:
        if not mapa.get("keyword"): return False
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

    def extrair_dados_tabelas(self, tabelas_academicas: list):
        if not tabelas_academicas: return

        for tabela in tabelas_academicas:
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

        matricula_valida = self.matricula_encontrada_no_pdf

        print(f"Procurando Matrícula: {self.matricula_alvo}")
        print(f"Matrícula Encontrada no PDF: {matricula_valida}")
        print(f"Horas: {horas_cursadas['valor']} (Min: {horas_cursadas['valor_min']})")
        print(f"CR Específico: {cr_especifico['valor']} (Min: {cr_especifico['valor_min']})")
        print(f"CR Geral: {cr_geral['valor']} (Min: {cr_geral['valor_min']})")

        if not matricula_valida:
            print("Validação falhou: Matrícula não encontrada ou não compatível.")
            return False

        return (
            self.valor_suficiente(horas_cursadas)
            and self.valor_suficiente(cr_especifico)
            and self.valor_suficiente(cr_geral)
        )
    

    def analisar_e_decidir(self, url_pdf: str) -> str:
        print(f"Iniciando análise do PDF: {url_pdf}")
        
        texto_cabecalho = self.ler_texto_cabecalho(url_pdf)
        if not texto_cabecalho:
            print("Análise falhou: PDF sem texto ou ilegível.")
            return "PENDENTE" 
        
        tabelas_notas = self.ler_tabelas_academicas(url_pdf)
        if not tabelas_notas:
            print("Análise falhou: PDF sem tabelas de notas.")
            return "PENDENTE" 

        self.verificar_matricula_pdf(texto_cabecalho)
        self.extrair_dados_tabelas(tabelas_notas)
        
        if self.candidato_apto():
            print("Resultado: CANDIDATURA APROVADA (automaticamente)")
            return "CANDIDATURA APROVADA"
        else:
            print("Resultado: REJEITADO (critérios não atingidos ou matrícula inválida)")
            return "REJEITADO"