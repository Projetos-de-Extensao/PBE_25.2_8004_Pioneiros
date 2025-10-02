---
id: diagrama_de_casos de uso
title: Diagrama de Casos de Uso
---

## Casos de Uso

### Criação de uma conta no sistema

* Atores:
	- Usuário

- Pré-Condições:
	- Nenhuma

* Fluxo Principal:
    1. Usuário fornece e-mail, senha e confirmações
    2. Dados do Usuário são validados pelo Sistema
    3. Dados do Usuário são encriptados pelo Sistema
    4. Sistema envia e-mail de verificação, com o link, para o Usuário
    5. Usuário confirma o e-mail antes do link expirar
    6. Sistema confirma que o Cadastro do Usuário foi realizado com sucesso
    7. Sistema redireciona o Usuário para a página de Entrada

- Fluxos Alternativos:
	- 2a. E-mail do Usuário é inválido
		2a1. Sistema exibe mensagem de erro
	- 2b. Senha do Usuário não respeita regras de segurança
		- 2b1. Sistema exibe mensagem de erro
	- 3a. Usuário tenta confirmar o e-mail depois de o link expirar
		- 3a1. Sistema sugere que o Usuário realize um novo Cadastro

### Entrada do usuário no sistema

- Atores:
	- Usuário

- Pré-Condições:
	Usuário deve estar cadastrado

- Fluxo Básico:
    - 1. Usuário fornece e-mail e senha
	- 2. Sistema autentica o Usuário
	- 3. Sistema redireciona o Usuário para a página inicial

- Fluxos Alternativos:
	- 2a. Dados do Usuário Inválidos
		- 2a1. Sistema exibe mensagem de erro
	- 3a. Primeio acesso do Usuário
		- 3a1. Sistema redireciona o Usuário para a página de edição de perfil

- Pós-condições: Usuário pode acessar o sistema

### Inscrever aluno no programa

- Atores:
	- Candidato

- Pré-Condições:
	- O candidato deve possuir matrícula ativa.

- Fluxo Principal:
	1. Candidato informa nome e matrícula
	2. Candidato informa curso e período
	3. Candidato seleciona matéria
	4. Candidato informa CR geral e CR da disciplina
	5. Sistema registra formulário

- Fluxos Alternativos:
	- 4a. Se CR geral < 7 ou CR da disciplina < 8, o sistema exibe uma mensagem de erro e pede nova tentativa

- Pós-condições:
	- Candidato será registrado como Candidato.

---

### Agendar entrevista

- Atores:
	- Organizador
	- Professor

- Pré-Condições:
	- Professor informa disponibilidade de horários

- Fluxo Principal:
	1. Sistema informa quantidade de candidatos
	2. Organizador informa disponibilidade do professor
	3. Sistema aloca candidatos
	4. Organizador envia emails para candidatos

- Fluxos Alternativos:
	- 1a. Se não houver candidatos, o sistema não pede a disponibilidade do professor e envia mensagem de concluído
	- 4a. Se o email de algum candidato for inválido, sistema apresenta nome do aluno e seus dados

- Pós-condições:
	- Candidatos serão alocados e notificados.

- Regras de Negócio:
	- Somente organizador e professores podem enviar emails.

---

### Preencher formulário de frequências

- Atores:
	- Teaching Assistant

- Pré-Condições:
	- Nenhuma

- Fluxo Principal:
	1. TA informa nome e matrícula
	2. TA informa unidade, curso e disciplina
	3. TA informa data da monitoria
	4. TA informa modalidade da monitoria
	5. TA informa existência de participação de monitorados
	6. TA informa tema, nome e matrícula dos alunos que participaram

- Fluxos Alternativos:
	- 3a. Se data já registrada para a mesma unidade, curso e disciplina, o sistema pede nova data
	- 4a. Se monitoria online, TA deve informar o link da monitoria
	- 5a. Se não houve participação, sistema não pede tema, nome e matrícula dos alunos que participaram

- Pós-condições:
	- Formulário enviado e informações salvas no sistema.

- Regras de Negócio:
	- Somente o TA pode registrar formulários de frequência

---
### Enviar informativos por email

- Atores:
	- Organizador
	- Professor

- Descrição:
	- Permite que informativos sejam enviados para candidatos ou TAs.

- Pré-Condições:
	- Devem ter emails de alunos ou TAs cadastrados no sistema.

- Fluxo Principal:
	1. Organizador escolhe a categoria de usuários ou usuário específico
	2. Organizador define o assunto e a mensagem
	3. Sistema envia email

- Fluxos Alternativos:
	- 1a. Se a categoria estiver vazia, o sistema exibe uma mensagem de erro e pede outra categoria
	- 3a. Se o email de algum candidato for inválido, sistema apresenta nome do aluno e seus dados

- Pós-condições:
	- Os emails serão enviados para os candidatos ou TAs