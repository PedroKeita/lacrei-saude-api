
# Introdução

Esse Backlog tem a função de detalhar as tarefas necessárias para o desenvolvimento da API de Gerenciamento de Consultas Médicas proposta pela Lacrei Saúde, priorizando por impacto técnico e requisitos do desafio.

# Épica 1: Setup e Infraestrutura

Objetivo: Configurar o ambiente de desenvolvimento e padrões de qualidade.

- [x] Task 1.1: Inicializar o projeto Django com Poetry e fazer as devidas configurações. 
- [ ] Task 1.2: Configurar Docker e Docker Compose
- [ ] Task 1.3: Configurar variáveis de ambiente e suporte a múltiplos ambientes.
- [ ] Task 1.4: Configurar Linter e ferramentas de formatação no CI.
- [ ] Task 1.5: Criar Pipeline inicial no GitHub Actions


# Épica 2: Núcleo da API (CRUD + Negócio)

Objetivo: Entregas os Requisitos Funcionais e Regras de Negócio

- [ ] Task 2.1: Implementar Modelo Profissional e Migrations (RN02, RN03, RN04, RN08, RN09).
- [ ] Task 2.2: Criar Serializers e Views para CRUD de Profissionais (RF01 até RF05).
- [ ] Task 2.3: Implementar modelo Consulta com FK para Profissional (RN01 e RN05).
- [ ] Task 2.4: Criar Serializers e Views para CRUD de Consultas (RF06, RF07, RF09, RF10).
- [ ] Task 2.5: Implementar endpoint de busca de consultas por ID de profissional (RF08).
- [ ] Task 2.6: Implementar lógica de bloqueio de exclusão de profissional com consultas ativas (RN06).
- [ ] Task 2.7: Validar choque de horários para consultas do mesmo profissional (RN07).


# Épica 3: Segurança, Qualidade e Documentação

Objetivo: Requisitos Não Funcionais de segurança e estabilidade.

- [ ] Task 3.1: COnfigurar autenticação JWT e token nos endpoints sensíveis (RNF03).
- [ ] Task 3.2: Configurar CORS (RNF04).
- [ ] Task 3.3: Implementar Middlewares para Logs de Acesso e Erro (RNF05, RNF06).
- [ ] Task 3.4: Desenvolver Testes automatizados com cobertura maior que 70% (RNF09).
- [ ] Task 3.5: Revisar limpeza de inputs nos Serializers (RNF01 e RNF02).
- [ ] Task 3.6: Desenhar arquitetura de integração com Gateway Assas para pagamentos.
- [ ] Task 3.7: Gerar documentação interativa com Swagger.

# Épica 4: Deploy e DevOps

Objetivo: Colocar a aplicação em produção via AWS e garantir CI/CD.

- [ ] Task 4:1: Configurar AWS para ambientes de Staging e Produção.
- [ ] Task 4.2: Finalizar Pipeline CI/CD seguindo o fluxo: TESTES -> BUILD DOCKER -> DEPLOY (RNF12).
- [ ] Task 4.3: Implementar estratégia de Rollback
- [ ] Task 4.4: Documentação técnica final: README, fluxograma de deploy e guia API via Swagger e Postman