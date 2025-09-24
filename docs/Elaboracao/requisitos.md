---
id: requisitos
title: Elicitação de Requisitos
---

## Requisitos

### Requisitos funcionais:

- Permitir inscrição de alunos no programa. - aluno
- Validar critérios de elegibilidade. - sistema
- Agendar entrevistas entre professor e aluno. - organizador/professor
- Enviar email - organizador/sistema
- Registrar assinatura de termo de participação.
- Acompanhar desempenho dos alunos que participam da monitoria.
- Gerar relatórios de acompanhamento.


### Requisitos não funcionais:
- O sistema deve ser implementado em Django.
- O banco de dados deve ser relacional.
- O sistema deve garantir segurança e autenticação por perfil.
- Deve permitir escalabilidade para múltiplas unidades e disciplinas.
- Deve ser simples de usar pelos diferentes perfis.
- Possibilitar integração com e-mail e WhatsApp. (a definir)

### Regras de Negócio:
- Somente professor pode aprovar o aluno
- Somente o casa pode agendar entrevistas
- Somente casa e professor podem enviar email
- Somente o casa e professor pode acompanhar desempenho dos alunos

