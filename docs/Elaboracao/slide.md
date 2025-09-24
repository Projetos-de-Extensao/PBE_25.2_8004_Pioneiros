---
marp: true
theme: default
paginate: true
title: Sistema de Monitoria - Pioneiros
---

# Sistema de Monitoria  
## Pioneiros

- Documentação de requisitos e casos de uso
- Proposta de solução para gestão de monitoria acadêmica

---

# Sumário

1. Requisitos do Sistema
2. Casos de Uso
3. Fluxos Principais
4. Regras de Negócio

---

# Requisitos Funcionais

- Inscrição de alunos no programa
- Validação de elegibilidade
- Agendamento de entrevistas
- Envio de e-mails
- Registro de assinatura de termo
- Acompanhamento de desempenho
- Geração de relatórios

---

# Requisitos Não Funcionais

- Implementação em Django
- Banco de dados relacional
- Segurança e autenticação por perfil
- Escalabilidade para múltiplas unidades/disciplinas
- Usabilidade para diferentes perfis
- Integração com e-mail e WhatsApp (a definir)

---

# Regras de Negócio

- Apenas professor pode aprovar aluno
- Apenas organizador pode agendar entrevistas
- Apenas organizador e professor podem enviar e-mails
- Apenas organizador e professor podem acompanhar desempenho

---

# Casos de Uso - Visão Geral

- **Contas:** Criação, entrada, alteração, recuperação de senha, exclusão lógica, visualização
- **Perfis:** Edição, pesquisa, visualização, seguir/deixar de seguir
- **Postagens:** Criação, exclusão, interação, visualização
- **Mensagens:** Criação, exclusão, visualização
- **Galerias, Blogs, Grupos**

---

# Caso de Uso: Inscrever Aluno

**Atores:** Candidato  
**Pré-condição:** Matrícula ativa

**Fluxo Principal:**
1. Informar nome, matrícula, curso, período, matéria, CR geral e da disciplina
2. Sistema valida e registra

**Alternativa:**  
- CR geral < 7 ou CR da disciplina < 8 → mensagem de erro

---

# Caso de Uso: Agendar Entrevista

**Atores:** Organizador, Professor  
**Pré-condição:** Professor informa disponibilidade

**Fluxo Principal:**
1. Sistema informa candidatos
2. Organizador informa disponibilidade
3. Sistema aloca candidatos
4. Organizador envia e-mails

**Alternativas:**  
- Sem candidatos: sistema finaliza  
- E-mail inválido: sistema exibe dados do aluno

---

# Caso de Uso: Preencher Frequência

**Atores:** Teaching Assistant

**Fluxo Principal:**
1. Informar dados da monitoria e participantes
2. Sistema salva formulário

**Alternativas:**  
- Data já registrada: pedir nova data  
- Monitoria online: informar link  
- Sem participação: não pedir tema/alunos

---

# Caso de Uso: Gerar Relatórios

**Atores:** Organizador  
**Pré-condição:** Pelo menos um formulário preenchido

**Fluxo Principal:**
1. Selecionar disciplina, curso e unidade
2. Sistema gera relatório (.xlsx)

---

# Obrigado!

---