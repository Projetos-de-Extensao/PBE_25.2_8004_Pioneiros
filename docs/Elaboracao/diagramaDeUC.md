%% Diagrama de Casos de Uso - Sistema de Monitoria Pioneiros
%% filepath: c:\Users\Guilherme\Documents\Back End\PBE_25.2_8004_Pioneiros\docs\Elaboracao\casos_de_uso.mmd
usecaseDiagram
    actor Usuario
    actor Candidato
    actor Organizador
    actor Professor
    actor "Teaching Assistant" as TA

    Usuario -- (Criar Conta)
    Usuario -- (Entrar no Sistema)

    Candidato -- (Inscrever-se no Programa)

    Organizador -- (Agendar Entrevista)
    Professor -- (Agendar Entrevista)

    TA -- (Preencher Formulário de Frequência)

    Organizador -- (Enviar Informativos por Email)
    Professor -- (Enviar Informativos por Email)
    