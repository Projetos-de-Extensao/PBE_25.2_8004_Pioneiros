---
id: brainstorm
title: Brainstorm
---
 
## Introdução
<p align = "justify">
O brainstorm é uma técnica de elicitação de requisitos que consiste em reunir a equipe e discutir sobre diversos tópicos gerais do projeto apresentados no documento problema de negócio. No brainstorm o diálogo é incentivado e críticas são evitadas para permitir que todos colaborem com suas próprias ideias.
</p>
 
## Metodologia
<p align = "justify">
A equipe se reuniu para debater ideias gerais sobre o projeto via..., começou .... e terminou..., onde o XXXX XXXX foi o moderador, direcionando a equipe com questões pré-elaboradas, e transcrevendo as respostas para o documento.
</p>
 
## Brainstorm
 
## Versão 1.0
 
## Perguntas
 
### 1. Qual o objetivo principal da aplicação?
 
<p align = "justify">
<b>1</b> - Deve ser uma plataforma onde qualquer pessoa possa se candidatar e acompanhar seu status no processo seletivo de TA e Monitoria de forma simples e centralizada.<br>
<b>2</b> - A plataforma deve fornecer as ferramentas para automatizar a comunicação, o agendamento de entrevistas e o envio de devolutivas a todos os envolvidos.<br>
<b>3</b> - O objetivo da aplicação é conectar coordenadores, professores e alunos, otimizando todo o fluxo de seleção e acompanhamento do programa.<br>
<b>4</b> - O principal objetivo da aplicação é a eliminação do trabalho manual da equipe do CASA, permitindo um gerenciamento de ponta a ponta que seja eficiente, rastreável e escalável.<br>
<b>5</b> - A plataforma deve gerenciar as inscrições, a elegibilidade dos candidatos, a agenda de entrevistas e o registro de frequência dos monitores de forma integrada.<br>
</p>
 
---
 
### 2. Como será o processo para cadastrar um novo cliente?
 
<p align = "justify">
<b>1</b> - O Instituto CASA deverá fazer login e cadastrar as disciplinas e vagas disponíveis para o programa, definindo os pré-requisitos para a candidatura.<br>
<b>2</b> - O cliente (aluno) acessará o portal e iniciará sua inscrição para o programa de TA/Monitoria, fornecendo suas informações básicas como nome, matrícula, curso e período.<br>
<b>3</b> - Com o usuário logado, ele deverá selecionar a disciplina desejada, preencher os campos de elegibilidade (CR geral e CR da disciplina) e anexar os documentos necessários, como o histórico escolar.<br>
<b>4</b> - O cliente receberá uma confirmação imediata do sistema. Caso não atenda aos critérios (CR, horas), será notificado automaticamente sobre a sua inelegibilidade.<br>
<b>5</b> - O cliente que atender aos pré-requisitos terá sua inscrição confirmada e seu status alterado para "Candidato", aguardando as próximas etapas do processo seletivo.<br>
</p>
 
---
 
### 3. Como será a forma de adicionar produtos?
 
<p align = "justify">
<b>1</b> - O cliente (professor), ao cadastrar uma nova vaga de monitoria, deverá acessar seu perfil no sistema e selecionar a opção "Publicar Vaga".<br>
<b>2</b> - O produto (a vaga) tem campos específicos que precisam ser preenchidos, como a disciplina, os pré-requisitos (CR mínimo, horas), as responsabilidades do monitor e o número de vagas ofertadas.<br>
<b>3</b> - O produto (a vaga), após o cadastro inicial, fica com o status "Pendente de Aprovação", aguardando a validação do Instituto CASA para se tornar pública.<br>
<b>4</b> - O produto (a vaga), uma vez aprovado, se torna visível no portal para que os alunos possam se candidatar.<br>
</p>
 
---
 
### 4. Outras perguntas pertinentes ao contexto

<p align = "justify">
<b>1</b> - Com a localização centralizada das informações, o sistema enviará notificações automáticas por e-mail em cada etapa: confirmação de inscrição, agendamento de entrevista e resultado final (aprovado ou não).<br>
<b>2</b> - O cliente (aluno) receberá um convite com as opções de horários de entrevista, que são baseadas na disponibilidade previamente informada pelo professor e gerenciada pelo Instituto CASA.<br>
<b>3</b> - O cliente (monitor aprovado) deverá registrar a frequência e o tema de cada sessão de monitoria diretamente no sistema, permitindo que o professor e o Instituto CASA acompanhem o andamento e o impacto do programa.<br>
</p>
 
---
 
### 5. "Outras perguntas pertinentes ao contexto", Como seria a forma de adicionar do cliente adicionar os produtos ?
<p align = "justify">
<b>XXX</b> - O cliente....
</p>
 
### 6. Quais informações seriam interessante para o cliente?
<p align = "justify">
<b>1</b> - Informações sobre o status da candidatura em tempo real, o desempenho dos monitores e o impacto geral do programa no rendimento acadêmico dos alunos assistidos.<br>
<b>2</b> - O cliente usuário (professor) poderá acessar informações detalhadas sobre cada candidato inscrito em sua vaga, como o histórico acadêmico, o CR na disciplina e o status atual no processo seletivo.<br>
<b>3</b> - O usuário (aluno) poderá ver todo o andamento de sua inscrição, os agendamentos de entrevistas, o resultado final e, após aprovado, um dashboard com suas horas registradas e o feedback de seu desempenho.<br>

</p>
 
### Requisitos elicitados
 
|ID|Descrição|
|----|-------------|
|BS01| O cliente (aluno) deve poder se inscrever no programa de TA/Monitoria através de um formulário online.|
|BS02| O cliente (aluno) deve poder visualizar todas as vagas de monitoria disponíveis, com seus respectivos pré-requisitos e descrições.|
|BS03| O cliente (aluno) deve poder acompanhar o status de sua candidatura em tempo real (recebida, em análise, entrevista agendada, aprovado, reprovado).|
|BS04| O cliente (monitor aprovado) deve poder registrar a frequência, a data e o tema de cada sessão de monitoria realizada.|
|BS05| O cliente (professor) deve poder cadastrar novas vagas de monitoria para suas disciplinas, especificando os requisitos necessários.|
|BS06| O cliente (professor) deve poder acessar a lista de todos os candidatos inscritos para sua vaga, visualizando suas informações e elegibilidade.|
|BS07| O cliente (professor) deve poder informar sua disponibilidade de horários no sistema para a realização das entrevistas.|
|BS08| O cliente (Instituto CASA) deve poder aprovar ou rejeitar as vagas de monitoria cadastradas pelos professores antes de serem publicadas.|
|BS09| O cliente (Instituto CASA) deve poder visualizar um dashboard com as métricas gerais do programa (total de inscritos, vagas preenchidas, etc.).|
|BS10| O produto (sistema) deve validar automaticamente os critérios de elegibilidade do candidato (CR geral, CR na disciplina, horas cursadas) no momento da inscrição.|
|BS11| O produto (sistema) deve enviar notificações automáticas por e-mail para os envolvidos em cada etapa chave do processo.|
|BS12| O produto (sistema) deve cruzar a disponibilidade do professor com a dos alunos interessados para sugerir horários de entrevista.|
|BS13| O produto (sistema) deve gerenciar diferentes perfis de usuário (Aluno, Professor, Instituto CASA), cada um com suas permissões específicas de acesso e ação.|
|BS14| O produto (sistema) deve gerar relatórios sobre a frequência dos alunos nas monitorias e o desempenho geral do programa.|
|BS15| O produto (sistema) deve registrar a assinatura digital do termo de compromisso pelo aluno aprovado.|

## Conclusão
<p align = "justify">
Através da aplicação da técnica, foi possível elicitar alguns dos primeiros requisitos do projeto.
</p>
## Referências Bibliográficas
 
> BARBOSA, S. D. J; DA SILVA, B. S. Interação humano-computador. Elsevier, 2010.
 
 
## Autor(es)
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 22/09/2025 | 1.0 | Criação do documento | Arthur Maurity |
