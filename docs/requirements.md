
# 1. Visão Geral 

O sistema consiste em uma **API RESTful** com a finalidade de gerenciar consultas médicas e profissionais de saúde, preparada para produção e integração futura com outros serviços da Lacrei Saúde.

# 2. Requisitos Funcionais

| **ID** | **Nome**                          | **Descrição**                                      | **Entrada Esperada**                      | Saída Esperada                                  | **Prioridade** |
| ------ | --------------------------------- | -------------------------------------------------- | ----------------------------------------- | ----------------------------------------------- | -------------- |
| RF01   | Cadastrar Profissional            | Permitir cadastrar um profissional da saúde        | Nome social, profissão, endereço, contato | Profissional criado com ID                      | Alta           |
| RF02   | Listar Profissionais              | Retornar todos os profissionais cadastrados        | Nenhuma                                   | Lista de profissionais                          | Alta           |
| RF03   | Atualizar Profissional            | Atualizar os dados de um profissional              | ID e campos editáveis                     | Profissional atualizado                         | Alta           |
| RF04   | Excluir Profissional              | Remover um profissional do sistema                 | ID válidado                               | Confirmação de exclusão                         | Média          |
| RF05   | Buscar Profissional por ID        | Retornar um profissional específico                | ID                                        | Dadps do profissional                           | Alta           |
| RF06   | Cadastrar Consulta                | Criar uma consulta vinculada a um profissional     | Data, ID do profissional                  | Consulta criada com ID                          | Alta           |
| RF07   | Listar Consultas                  | Listar todas as consultas                          | Nenhuma                                   | Lista de consultas                              | Alta           |
| RF08   | Buscar Consultas por Profissional | Listar consultas filtrando pelo ID do profissional | ID do profissional                        | Lista de consultas do profissional identificado | Alta           |
| RF09   | Atualizar Consulta                | Atualizar data ou profissional da consulta         | ID e novos dados                          | Consulta atualizada                             | Média          |
| RF10   | Excluir Consulta                  | Remover uma consulta                               | ID válido                                 | Confirmação de exclusão                         | Média          |
| RF11   | Retornar dados em JSON            | Todas as respostas devem estar no formato JSON     | ////                                      | JSON padronizado                                | Alta           |



# 3. Requisitos Não Funcionais


| **ID** | Nome                          | Categoria      | Descrição                                                | Critérios de Aceitação              | Prioridade |
| ------ | ----------------------------- | -------------- | -------------------------------------------------------- | ----------------------------------- | ---------- |
| RNF01  | Validação de Dados            | Segurança      | Limpar e validar todos os dados de entrada               | Nenhum campo aceita dados inválidos | Alta       |
| RNF02  | Proteção contra SQL Injection | Segurança      | O sistema deve prevenir ataques de injeção SQL           | Uso exclusivo do ORM                | Alta       |
| RNF03  | Autenticação de Usuário       | Segurança      | O acesso a API deve exigir autenticação                  | Token/JWT obrigatório               | Alta       |
| RNF04  | Controle de CORS              | Segurança      | A API deve permitir acesso apenas de origens autorizadas | CORS configurado                    | Alta       |
| RNF05  | Registro de Logs de Acesso    | Segurança      | O sistema deve registrar todas as requisições            | Log por requisição                  | Médio      |
| RNF06  | Registro de Logs de Erro      | Segurança      | O sistema deve registrar falhas e exceções               | Log por exceção                     | Médio      |
| RNF07  | Tempo de Resposta             | Performance    | O tempo médio de resposta da API deve ser baixo          | menor igual a 500 ms                | Baixo      |
| RNF08  | Organização do Código         | Qualidade      | O código deve ser modular e organizado                   | Separação por apps                  | Alta       |
| RNF09  | Cobertura de Testes           | Qualidade      | O sistema deve possuir testes automatizados              | maior igual a 70%                   | Alta       |
| RNF10  | Banco de Dados PostgreSQL     | Infraestrutura | O sistema deve utilizar PostgreSQL                       | PostgreSQL ativo                    | Alta       |
| RNF11  | Containerização               | Infraestrutura | O sistema deve ser executado em contêiner                | Docker configurado                  | Alta       |
| RNF12  | Pipeline CI/CD                | Infraestrutura | O projeto deve possuir integração contínua               | GitHub Actions                      | Alta       |
| RNF13  | Separação de Ambientes        | Infraestrutura | Deve haver ambientes separados                           | Staging e Produção                  | Médio      |
| RNF14  | Mecanismo de Rollback         | Confiabilidade | O sistema deve permitir retorno a versões anteriores     | Deploy reversível                   | Médio      |

# 4. Regras de Negócio

| ID   | Regra                                                                               | Tipo        |
| ---- | ----------------------------------------------------------------------------------- | ----------- |
| RN01 | Uma consulta só pode existir se houver um profissional válido                       | Obrigatória |
| RN02 | Nome social do profissional é obrigatório                                           | Obrigatória |
| RN03 | Profissão é obrigatória                                                             | Obrigatória |
| RN04 | Contato é obrigatório                                                               | Obrigatória |
| RN05 | Data da consulta deve ser futura ou presente                                        | Obrigatória |
| RN06 | Não é permitido excluir profissional com consultas ativas                           | Opcional    |
| RN07 | Não é permitido cadastrar duas consultas no mesmo horário para o mesmo profissional | Opcional    |
| RN08 | Endereço não pode estar vazio                                                       | Obrigatória |
| RN09 | IDs devem ser únicos e autogerados                                                  | Obrigatória |
