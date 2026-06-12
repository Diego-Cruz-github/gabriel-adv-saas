# SaaS Jurídico - Automação para Advocacia

> [English](README.md) | **Português (BR)**

Automação de triagem de clientes e onboarding digital para escritório de advocacia.

> **Visão geral do case** - o código de produção é privado (projeto de cliente). Esta página
> documenta o problema, a arquitetura e as decisões de engenharia.

## O problema

Todo cliente em potencial chegava pelo mesmo canal e esperava um humano ler,
classificar e responder. Casos urgentes ficavam na mesma fila dos rotineiros, e a
coleta de documentos se arrastava por dias de vai-e-vem.

## A solução

- **Triagem automática por área do direito** (cível, trabalhista, previdenciário)
  desde o primeiro contato, com classificação de urgência antes de qualquer
  revisão humana.
- **Onboarding digital**: coleta de documentos automatizada com passos guiados -
  o cliente envia tudo uma vez, estruturado.
- **Integrações via webhook** conectando o formulário de captação, a automação de
  mensagens e o CRM do escritório.
- Tempo de resposta ao primeiro contato: **abaixo de um minuto**.

## Arquitetura

```
Formulário de captação --> [ Webhooks ] --> [ Backend (Python + Node.js) ] --> CRM
                                                  |
                                  [ Triagem: regras de área + urgência ]
                                                  |
                                  [ Mensageria automatizada + onboarding ]
```

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Python, Node.js |
| Integração | Webhooks, APIs REST |
| Segurança | Autenticação JWT, validação server-side |
| Infra | Nginx, Docker |

## Notas de engenharia

- **Regras antes de IA**: a triagem usa regras determinísticas - em contexto
  jurídico, classificação previsível vale mais que esperteza probabilística.
- **Validação na borda**: todo payload de webhook é validado server-side antes
  de tocar a lógica de negócio.

## Status

Entregue. Engenheiro único: backend, integrações e infraestrutura.
