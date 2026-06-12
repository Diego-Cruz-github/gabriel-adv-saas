# Legal SaaS - Law Firm Automation

Client triage and digital onboarding automation for a law office.

> **Case overview** - the production code is private (client engagement). This page
> documents the problem, the architecture and the engineering decisions.

## The problem

Every prospective client arrived through the same channel and waited for a
human to read, classify and reply. Urgent cases sat in the same queue as
routine ones, and document collection dragged over days of back-and-forth.

## The solution

- **Automatic triage by legal area** (civil, labor, social security) from the
  first contact, with urgency classification before any human review.
- **Digital onboarding**: automated document collection with guided steps -
  the client sends everything once, structured.
- **Webhook-driven integrations** connecting the capture form, the messaging
  automation and the firm's CRM.
- Response time to first contact: **under one minute**.

## Architecture

```
Capture form --> [ Webhooks ] --> [ Backend (Python + Node.js) ] --> CRM
                                        |
                          [ Triage: area + urgency rules ]
                                        |
                          [ Automated messaging + onboarding ]
```

## Stack

| Layer | Technology |
|---|---|
| Backend | Python, Node.js |
| Integration | Webhooks, REST APIs |
| Security | JWT authentication, server-side input validation |
| Infra | Nginx, Docker |

## Engineering notes

- **Rules before AI**: triage uses deterministic rules - in a legal context,
  predictable classification beats probabilistic cleverness.
- **Validation at the edge**: every webhook payload is validated server-side
  before touching business logic.

## Status

Delivered. Sole engineer: backend, integrations and infrastructure.
