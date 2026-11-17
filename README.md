# Grimório — API de Fichas de RPG

## Identificação do projeto

- **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Piauí (IFPI)

- **Disciplina:** Programação Web

- **Professor responsável:** Anthony Irlan Marques Luz

- **Integrantes:**
  - José Otavio Luciano Sousa Chagas
  - Ronalty Hauan Gomes Galvão dos Santos

## Finalidade acadêmica

O **Grimório** é um projeto acadêmico da disciplina de Programação Web. Seu objetivo é aplicar conceitos de desenvolvimento de APIs, arquitetura cliente-servidor, modelagem de dados, autenticação, autorização, testes automatizados, documentação e versionamento.

## Regra arquitetural obrigatória

O Grimório será desenvolvido como uma **API REST pura para comunicação Máquina para Máquina (Machine to Machine — M2M)**.

A aplicação não terá interface de usuário em HTML, páginas web, formulários, painel visual, templates ou qualquer camada de apresentação acoplada ao backend. A comunicação será feita exclusivamente por clientes automatizados, outros serviços, scripts, aplicações móveis ou ferramentas HTTP capazes de consumir uma API.

### Regras de comunicação

1. As requisições de entrada utilizarão HTTP e payloads JSON.

1. As respostas da API utilizarão JSON, inclusive em situações de erro.

1. A API não renderizará HTML.

1. A API não dependerá de interação manual em navegador para executar suas operações.

1. Não serão utilizadas sessões baseadas em cookies ou estado de interface.

1. A autenticação será feita por tokens enviados no cabeçalho `Authorization`.

1. A documentação principal será o contrato OpenAPI em JSON/YAML

1. Operações que exigiriam upload de arquivo, como imagens, serão substituídas por metadados JSON ou URLs externas.

1. A API não gerará PDF, páginas para impressão ou outros formatos de apresentação na primeira versão.

1. Um cliente M2M será responsável por interpretar os dados e apresentar qualquer interface, caso isso seja necessário fora do escopo deste projeto.

> **Nota:** Swagger UI e ReDoc são ferramentas HTML e, portanto, não serão considerados parte da aplicação. O arquivo OpenAPI poderá ser disponibilizado como especificação estática para consumo por ferramentas automatizadas.

## Sobre o projeto
O Grimório permitirá que sistemas clientes organizem fichas de personagens de RPG. A API oferecerá operações para usuários, personagens, atributos, perícias, habilidades, inventário, campanhas e evolução dos personagens.

O backend será implementado em Python com FastAPI. O foco será a definição de contratos claros, validação rigorosa, regras de negócio, persistência relacional e respostas previsíveis para consumidores automatizados.

A proposta será desenvolvida progressivamente, utilizando como referência a metodologia prática do curso [FastAPI do Zero](https://fastapidozero.dunossauro.com/estavel/01/).

## Objetivos

- Desenvolver uma API REST pura orientada a comunicação M2M.

- Aplicar Python e FastAPI na construção de serviços HTTP.

- Implementar operações CRUD para os recursos do sistema.

- Validar requisições e respostas com Pydantic.

- Modelar e integrar um banco de dados relacional.

- Implementar autenticação por token e autorização por proprietário do recurso.

- Padronizar códigos HTTP e respostas JSON de sucesso e erro.

- Criar testes automatizados para rotas, regras de negócio e persistência.

- Documentar a API por meio de OpenAPI.

- Utilizar Git e GitHub para versionamento e colaboração.

- Aplicar práticas de segurança, organização e manutenção de código.

## Tecnologias

| Tecnologia | Finalidade |
| --- | --- |
| Python | Linguagem principal do backend. |
| FastAPI | Criação da API REST e gerenciamento das rotas. |
| Pydantic | Validação e serialização dos dados. |
| SQLAlchemy | Mapeamento objeto-relacional e acesso ao banco. |
| SQLite | Banco inicial para desenvolvimento e testes locais. |
| PostgreSQL | Banco previsto para produção. |
| Alembic | Versionamento e execução das migrações. |
| JSON | Formato exclusivo de troca de dados da API. |
| OpenAPI | Especificação do contrato da API. |
| JWT ou token equivalente | Autenticação das requisições protegidas. |
| pytest | Testes automatizados. |
| Ruff | Linting e formatação do código Python. |
| Git e GitHub | Versionamento e colaboração. |
| Docker | Opcional, caso seja exigido na implantação. |

As dependências e suas versões serão declaradas no `pyproject.toml`.

## Escopo funcional

### Usuários e autenticação

- [ ] Cadastrar usuário por requisição JSON.

- [ ] Autenticar usuário por credenciais enviadas em JSON.

- [ ] Emitir token de acesso.

- [ ] Consultar os dados do usuário autenticado.

- [ ] Atualizar os dados básicos do usuário.

- [ ] Excluir a própria conta.

- [ ] Armazenar senhas somente em formato de hash.

- [ ] Validar tokens e rejeitar tokens inválidos ou expirados.

- [ ] Impedir o acesso a dados pertencentes a outros usuários.

- [ ] Implementar revogação de tokens somente se ela for necessária à estratégia de autenticação adotada.

O login não será uma tela HTML. Será uma operação de API em que um cliente M2M envia credenciais JSON e recebe um token JSON.

### Personagens

- [ ] Criar personagem.

- [ ] Listar personagens do usuário autenticado.

- [ ] Consultar uma ficha por identificador.

- [ ] Atualizar parcialmente uma ficha.

- [ ] Excluir uma ficha.

- [ ] Duplicar uma ficha.

- [ ] Marcar ou desmarcar personagem como favorito.

- [ ] Registrar nome, apelido, idade, gênero e outros dados opcionais.

- [ ] Registrar raça, espécie, classe, profissão ou arquétipo.

- [ ] Registrar nível, experiência, alinhamento e sistema de RPG.

- [ ] Registrar origem, história, personalidade, objetivos e anotações.

- [ ] Associar o personagem a uma campanha.

- [ ] Informar uma `image_url` opcional, sem upload de arquivo e sem processamento de imagem pelo backend.

- [ ] Registrar datas de criação e atualização.

Todos os dados serão enviados e retornados como JSON. Campos específicos de determinado sistema de RPG deverão ser representados por estruturas JSON validadas ou por regras específicas do sistema suportado.

### Atributos e características

- [ ] Cadastrar atributos padrão ou personalizados.

- [ ] Registrar valores, bônus e penalidades.

- [ ] Validar valores permitidos.

- [ ] Calcular modificadores quando houver regra configurada.

- [ ] Atualizar os cálculos após alterações.

- [ ] Retornar os atributos em estruturas JSON previsíveis.

As fórmulas não serão consideradas universais. Cada regra deverá ser configurável ou implementada separadamente para os sistemas de RPG suportados.

### Perícias e proficiências

- [ ] Cadastrar perícias.

- [ ] Definir valores e proficiências.

- [ ] Associar perícias a atributos.

- [ ] Calcular bônus quando a regra estiver implementada.

- [ ] Permitir perícias personalizadas.

### Combate e recursos

- [ ] Registrar pontos de vida máximos e atuais.

- [ ] Registrar mana, energia ou recurso equivalente.

- [ ] Registrar defesa, iniciativa, deslocamento e velocidade.

- [ ] Registrar resistências, imunidades e vulnerabilidades.

- [ ] Controlar condições temporárias.

- [ ] Registrar ataques, bônus, dano, alcance e propriedades.

- [ ] Atualizar recursos por requisição JSON.

- [ ] Validar limites configurados para os recursos.

A API retornará valores numéricos e estados estruturados. Barras visuais, cores e outros elementos de apresentação não fazem parte do backend.

### Habilidades, talentos e poderes

- [ ] Cadastrar habilidades, talentos, poderes e magias.

- [ ] Registrar nome, descrição, categoria e nível.

- [ ] Registrar custo, alcance, duração, tempo de execução e pré-requisitos.

- [ ] Registrar efeitos e limitações.

- [ ] Associar habilidades a personagens.

- [ ] Editar e remover habilidades.

- [ ] Controlar usos disponíveis quando aplicável.

### Inventário e equipamentos

- [ ] Adicionar itens ao inventário.

- [ ] Atualizar e remover itens.

- [ ] Registrar nome, descrição, categoria, quantidade, peso e valor.

- [ ] Controlar moedas e outros recursos.

- [ ] Marcar itens como equipados ou guardados.

- [ ] Registrar armas, armaduras, acessórios, consumíveis e itens mágicos.

- [ ] Associar propriedades e bônus aos equipamentos.

- [ ] Calcular o peso total carregado.

- [ ] Registrar itens consumidos, perdidos ou transferidos.

### Magias e recursos especiais

- [ ] Cadastrar magias e recursos sobrenaturais.

- [ ] Registrar níveis, círculos, custos e requisitos.

- [ ] Registrar componentes, alcance e duração.

- [ ] Controlar espaços ou cargas disponíveis.

- [ ] Associar magias conhecidas e preparadas ao personagem.

- [ ] Restaurar recursos conforme regras configuradas.

### Evolução do personagem

- [ ] Registrar experiência e nível.

- [ ] Manter histórico de evolução.

- [ ] Registrar alterações de atributos, habilidades e classe.

- [ ] Consultar mudanças anteriores.

- [ ] Aplicar progressão automática quando as regras estiverem implementadas.

### Campanhas e sessões

- [ ] Criar, consultar, atualizar e excluir campanhas.

- [ ] Associar personagens a campanhas.

- [ ] Registrar mestre, participantes e sistema de RPG.

- [ ] Registrar sessões, datas, títulos e resumos.

- [ ] Registrar missões, objetivos e recompensas.

- [ ] Controlar o estado das missões.

- [ ] Registrar NPCs, organizações e notas privadas.

### Importação e exportação JSON

- [ ] Exportar uma ficha como resposta JSON.

- [ ] Importar uma ficha enviando um objeto JSON no corpo da requisição.

- [ ] Validar o objeto antes da persistência.

- [ ] Informar erros de validação em JSON.

- [ ] Utilizar versão de esquema para compatibilidade futura.

- [ ] Evitar sobrescrita acidental por meio de validações e identificadores explícitos.

Não haverá importação por formulário HTML, upload multipart, impressão ou geração de PDF no escopo da API pura.

## Requisitos funcionais

| Código | Requisito |
| --- | --- |
| RF01 | A API deve permitir cadastrar usuários por JSON. |
| RF02 | A API deve autenticar clientes por credenciais JSON e emitir token. |
| RF03 | A API deve permitir criar, consultar, atualizar e excluir personagens. |
| RF04 | A API deve associar cada personagem ao seu proprietário. |
| RF05 | A API deve gerenciar atributos e perícias. |
| RF06 | A API deve gerenciar habilidades e poderes. |
| RF07 | A API deve gerenciar inventário e equipamentos. |
| RF08 | A API deve controlar recursos do personagem. |
| RF09 | A API deve registrar a evolução dos personagens. |
| RF10 | A API deve organizar personagens em campanhas. |
| RF11 | A API deve permitir pesquisa, filtragem, paginação e ordenação por parâmetros HTTP. |
| RF12 | A API deve validar requisições e respostas conforme schemas. |
| RF13 | A API deve importar e exportar fichas em JSON. |
| RF14 | A API deve retornar respostas de sucesso e erro em JSON estruturado. |
| RF15 | A API deve impedir acesso não autorizado aos recursos. |

## Requisitos não funcionais

| Código | Requisito |
| --- | --- |
| RNF01 | A aplicação deve funcionar como API REST pura M2M. |
| RNF02 | A aplicação não deve renderizar HTML nem depender de interface web. |
| RNF03 | As requisições e respostas de negócio devem utilizar JSON. |
| RNF04 | A API deve utilizar códigos HTTP coerentes com o resultado da operação. |
| RNF05 | A API deve ser implementada em Python com FastAPI. |
| RNF06 | Os dados persistentes devem ser armazenados em banco relacional. |
| RNF07 | O código deve ser modular e manter responsabilidades separadas. |
| RNF08 | As operações principais devem possuir testes automatizados. |
| RNF09 | Senhas nunca devem ser armazenadas em texto puro. |
| RNF10 | Segredos e credenciais devem ficar fora do código-fonte. |
| RNF11 | As migrações do banco devem ser versionadas. |
| RNF12 | O contrato da API deve ser publicado em OpenAPI JSON ou YAML. |
| RNF13 | A API deve retornar erros sem expor detalhes internos. |
| RNF14 | O projeto deve utilizar Git para controle de versão. |
| RNF15 | A API deve permitir manutenção e inclusão de recursos sem reescrita completa. |

## Padrão de respostas

### Resposta de sucesso

As respostas devem conter dados JSON compatíveis com o schema do endpoint. Exemplo:

```json
{
  "id": 1,
  "nome": "Arannis",
  "sistema_rpg": "fantasia",
  "nivel": 3,
  "criado_em": "2026-01-01T12:00:00Z"
}
```

### Resposta de erro

Os erros devem seguir um formato previsível e não devem expor stack trace ou detalhes internos:

```json
{
  "erro": {
    "codigo": "VALIDACAO_INVALIDA",
    "mensagem": "Os dados enviados são inválidos.",
    "detalhes": [
      {
        "campo": "nome",
        "motivo": "O campo é obrigatório."
      }
    ],
    "request_id": "7d6e2c1a"
  }
}
```

Códigos HTTP esperados:

- `200 OK` para consultas e atualizações bem-sucedidas.

- `201 Created` para criação de recursos.

- `204 No Content` para exclusões sem corpo de resposta.

- `400 Bad Request` para requisição semanticamente inválida.

- `401 Unauthorized` para ausência ou invalidade de autenticação.

- `403 Forbidden` para falta de permissão.

- `404 Not Found` para recurso inexistente ou não acessível.

- `409 Conflict` para conflitos de unicidade ou estado.

- `422 Unprocessable Entity` para falha de validação do schema.

- `500 Internal Server Error` para falhas inesperadas, sem detalhes internos.

## Arquitetura

```
Cliente M2M / Sistema Externo
          |
          | HTTP + JSON + Authorization: Bearer <token>
          v
API REST FastAPI
          |
          | Schemas Pydantic e validação
          v
Serviços e regras de negócio
          |
          v
Repositórios / SQLAlchemy
          |
          v
SQLite ou PostgreSQL
```

Não haverá camada de templates, frontend, sessão de navegador ou controlador de páginas HTML.

## Organização inicial do projeto

```
grimorio/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── database/
│   │   ├── session.py
│   │   └── models.py
│   ├── schemas/
│   │   ├── usuario.py
│   │   ├── autenticacao.py
│   │   ├── personagem.py
│   │   ├── habilidade.py
│   │   └── inventario.py
│   ├── routers/
│   │   ├── usuarios.py
│   │   ├── autenticacao.py
│   │   ├── personagens.py
│   │   ├── habilidades.py
│   │   ├── inventario.py
│   │   └── campanhas.py
│   └── services/
│       ├── personagens.py
│       ├── campanhas.py
│       └── autenticacao.py
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_personagens.py
│   └── test_schemas.py
├── alembic/
├── openapi.yaml
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── Dockerfile
```

## Endpoints previstos

Todos os endpoints abaixo receberão ou retornarão JSON, salvo respostas `204 No Content`. Os endpoints protegidos exigirão o cabeçalho:

```
Authorization: Bearer <token>
```

### Usuários e autenticação

| Método | Rota | Descrição |
| --- | --- | --- |
| `POST` | `/usuarios` | Cadastrar usuário. |
| `POST` | `/auth/token` | Autenticar e emitir token. |
| `GET` | `/usuarios/me` | Consultar usuário autenticado. |
| `PATCH` | `/usuarios/me` | Atualizar perfil. |
| `DELETE` | `/usuarios/me` | Excluir a própria conta. |

### Personagens

| Método | Rota | Descrição |
| --- | --- | --- |
| `POST` | `/personagens` | Criar personagem. |
| `GET` | `/personagens` | Listar personagens com filtros e paginação. |
| `GET` | `/personagens/{personagem_id}` | Consultar ficha. |
| `PATCH` | `/personagens/{personagem_id}` | Atualizar ficha. |
| `DELETE` | `/personagens/{personagem_id}` | Excluir ficha. |
| `POST` | `/personagens/{personagem_id}/duplicar` | Duplicar ficha. |
| `GET` | `/personagens/{personagem_id}/exportar` | Obter ficha em JSON. |
| `POST` | `/personagens/importar` | Validar e importar ficha JSON. |

### Atributos, perícias e habilidades

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/personagens/{personagem_id}/atributos` | Listar atributos. |
| `PUT` | `/personagens/{personagem_id}/atributos` | Substituir atributos. |
| `GET` | `/personagens/{personagem_id}/pericias` | Listar perícias. |
| `POST` | `/personagens/{personagem_id}/habilidades` | Associar habilidade. |
| `PATCH` | `/habilidades/{habilidade_id}` | Atualizar habilidade. |
| `DELETE` | `/habilidades/{habilidade_id}` | Remover habilidade. |

### Inventário e campanhas

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/personagens/{personagem_id}/inventario` | Consultar inventário. |
| `POST` | `/personagens/{personagem_id}/inventario` | Adicionar item. |
| `PATCH` | `/itens/{item_id}` | Atualizar item. |
| `DELETE` | `/itens/{item_id}` | Remover item. |
| `POST` | `/campanhas` | Criar campanha. |
| `GET` | `/campanhas` | Listar campanhas. |
| `GET` | `/campanhas/{campanha_id}` | Consultar campanha. |
| `PATCH` | `/campanhas/{campanha_id}` | Atualizar campanha. |
| `DELETE` | `/campanhas/{campanha_id}` | Excluir campanha. |

Os endpoints são uma proposta inicial. Seus schemas, parâmetros e permissões deverão ser definidos no código e refletidos no arquivo OpenAPI.

## Modelagem inicial do banco de dados

Entidades previstas:

- **Usuario:** e-mail, hash da senha, perfil e datas de controle.

- **Personagem:** proprietário, dados básicos, sistema de RPG, nível e informações opcionais.

- **Atributo:** nome, valor, bônus e personagem associado.

- **Pericia:** nome, valor, proficiência e personagem associado.

- **Habilidade:** nome, descrição, categoria, custo e requisitos.

- **PersonagemHabilidade:** associação entre personagem e habilidade.

- **Item:** nome, descrição, categoria, peso e valor.

- **InventarioItem:** personagem, item, quantidade e estado.

- **Campanha:** proprietário, nome, descrição e sistema de RPG.

- **CampanhaPersonagem:** associação entre personagens e campanhas.

- **Sessao:** campanha, data, título e resumo.

- **Missao:** campanha, descrição, objetivo e estado.

- **HistoricoEvolucao:** personagem, data, nível e descrição das mudanças.

Os relacionamentos, restrições de integridade, índices e regras de exclusão serão controlados pelo SQLAlchemy e pelo Alembic.

## Etapas de desenvolvimento

### Etapa 1 — Configuração

- [ ] Criar o repositório Git.

- [ ] Configurar o ambiente virtual Python.

- [ ] Criar o `pyproject.toml`.

- [ ] Instalar FastAPI e dependências.

- [ ] Configurar Ruff e pytest.

- [ ] Criar a aplicação mínima sem rotas HTML.

- [ ] Definir configurações por variáveis de ambiente.

### Etapa 2 — Contrato e primeira API

- [ ] Definir schemas Pydantic.

- [ ] Criar rotas de usuários e personagens.

- [ ] Implementar CRUD básico.

- [ ] Definir respostas JSON de sucesso e erro.

- [ ] Definir códigos HTTP.

- [ ] Gerar e revisar o contrato OpenAPI.

- [ ] Testar com `pytest` e clientes HTTP automatizados.

### Etapa 3 — Persistência

- [ ] Configurar SQLAlchemy.

- [ ] Criar modelos e relacionamentos.

- [ ] Integrar SQLite.

- [ ] Configurar Alembic.

- [ ] Criar migrações.

- [ ] Validar persistência entre reinicializações.

### Etapa 4 — Autenticação e segurança

- [ ] Implementar cadastro e autenticação.

- [ ] Configurar hash seguro de senhas.

- [ ] Emitir e validar tokens.

- [ ] Proteger rotas privadas.

- [ ] Validar propriedade dos recursos.

- [ ] Testar isolamento entre usuários.

### Etapa 5 — Recursos da ficha

- [ ] Implementar atributos e perícias.

- [ ] Implementar habilidades e poderes.

- [ ] Implementar combate e recursos.

- [ ] Implementar inventário.

- [ ] Implementar evolução.

- [ ] Implementar campanhas e sessões.

- [ ] Adicionar regras específicas dos sistemas de RPG escolhidos.

### Etapa 6 — Testes e qualidade

- [ ] Criar testes unitários.

- [ ] Criar testes de integração das rotas.

- [ ] Testar autenticação e autorização.

- [ ] Testar entradas inválidas.

- [ ] Testar importação e exportação JSON.

- [ ] Testar persistência e relacionamentos.

- [ ] Verificar respostas e códigos HTTP.

### Etapa 7 — Finalização

- [ ] Revisar o contrato OpenAPI.

- [ ] Atualizar o README.

- [ ] Configurar variáveis de ambiente.

- [ ] Preparar PostgreSQL, se necessário.

- [ ] Configurar Docker, se exigido.

- [ ] Automatizar testes em integração contínua.

- [ ] Validar a implantação da API.

## Escopo do MVP

A primeira versão deverá priorizar uma API pequena, funcional e coerente com a regra M2M:

- [ ] Cadastro de usuários.

- [ ] Autenticação por token.

- [ ] CRUD de personagens.

- [ ] Atributos básicos.

- [ ] Habilidades básicas.

- [ ] Inventário básico.

- [ ] Persistência em SQLite.

- [ ] Controle de acesso por usuário.

- [ ] Validação Pydantic.

- [ ] Respostas de erro padronizadas em JSON.

- [ ] Testes das operações principais.

- [ ] Contrato OpenAPI em JSON/YAML.

- [ ] Documentação de execução e consumo por cliente HTTP.

Ficam fora do MVP: frontend HTML, painel visual, upload de imagens, PDF, impressão, notificações visuais, múltiplos sistemas complexos de regras, compartilhamento avançado e infraestrutura de produção não exigida pela atividade.

## Como executar

### Pré-requisitos

- Python em versão compatível com o `pyproject.toml`.

- Git.

- Terminal.

### Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd grimorio
```

### Criar e ativar o ambiente virtual

Linux ou macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Instalar dependências

```bash
pip install -e ".[dev]"
```

O extra `dev` deverá estar declarado no `pyproject.toml`.

### Configurar variáveis de ambiente

```bash
cp .env.example .env
```

No Windows, copie o arquivo manualmente caso o comando `cp` não esteja disponível. Nunca versione o arquivo `.env` com credenciais reais.

### Executar a API

```bash
fastapi dev app/main.py
```

A API ficará disponível em `http://127.0.0.1:8000`.

O contrato OpenAPI poderá ser consultado em formato JSON no endpoint padrão:

```
http://127.0.0.1:8000/openapi.json
```

A rota `/docs` ou qualquer outra interface HTML não é necessária para executar ou consumir o sistema. O consumo deve ser feito por cliente HTTP, script, teste automatizado ou outro serviço.

### Exemplo de consumo M2M

Cadastro de usuário:

```bash
curl -X POST http://127.0.0.1:8000/usuarios \
  -H "Content-Type: application/json" \
  -d '{
    "email": "jogador@example.com",
    "senha": "uma-senha-segura"
  }'
```

Criação de personagem:

```bash
curl -X POST http://127.0.0.1:8000/personagens \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Arannis",
    "sistema_rpg": "fantasia",
    "nivel": 1,
    "atributos": {
      "forca": 10,
      "destreza": 12
    }
  }'
```

Esses exemplos representam comunicação entre máquinas. O README não pressupõe uma tela ou ação manual em navegador.

## Testes

Executar toda a suíte:

```bash
pytest
```

Os testes deverão cobrir:

- Cadastro e autenticação.

- Emissão, expiração e rejeição de tokens.

- CRUD de personagens.

- Validação de campos obrigatórios.

- Dados inválidos e respostas `4xx`.

- Autorização e isolamento entre usuários.

- Persistência e relacionamentos.

- Importação e exportação JSON.

- Códigos HTTP e formato de erros.

## Segurança e boas práticas

- Senhas armazenadas somente por hash seguro.

- Segredos em variáveis de ambiente.

- `.env` incluído no `.gitignore`.

- Validação de todos os payloads com Pydantic.

- Verificação de autorização em todas as operações protegidas.

- Consultas parametrizadas e uso seguro do ORM.

- Tratamento de exceções sem exposição de stack trace.

- Controle de integridade e migrações do banco.

- Limitação de dados retornados conforme a autorização do cliente.

- Testes automatizados das regras críticas.

- Registro de `request_id` para facilitar rastreamento de erros.

- Revisão das configurações antes da implantação.

## Resultados esperados

Ao final da atividade, espera-se obter uma **API REST pura e funcional para gerenciamento de fichas de RPG**, capaz de ser consumida por clientes M2M por meio de HTTP e JSON.

O projeto deverá demonstrar conhecimentos de arquitetura cliente-servidor, contratos OpenAPI, validação, autenticação, autorização, persistência, regras de negócio, testes e versionamento, sem depender de interface HTML ou interação manual em navegador.

## Referências

- [FastAPI do Zero](https://fastapidozero.dunossauro.com/estavel/01/)

- [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/)

- [Documentação oficial do Pydantic](https://docs.pydantic.dev/)

- [Documentação oficial do SQLAlchemy](https://docs.sqlalchemy.org/)

- [Documentação oficial do Alembic](https://alembic.sqlalchemy.org/)

- [Documentação oficial do pytest](https://docs.pytest.org/)

- [Especificação OpenAPI](https://spec.openapis.org/oas/latest.html)

## Ferramentas utilizadas

| Ferramenta | Finalidade |
| --- | --- |
| Visual Studio Code | Edição do código-fonte. |
| Python | Implementação do backend. |
| FastAPI | Implementação da API REST. |
| Git e GitHub | Versionamento e hospedagem do projeto. |
| SQLite | Persistência local inicial. |
| Ruff | Análise estática e formatação. |
| pytest | Testes automatizados. |

Ferramentas de inteligência artificial poderão ser utilizadas como apoio ao aprendizado, à pesquisa, à revisão, à documentação e à identificação de erros. Todo código sugerido deverá ser compreendido, revisado, testado e validado pelos integrantes antes de ser incorporado ao projeto.

## Status

- **Projeto:** Grimório — API de Fichas de RPG

- **Status:** Em planejamento e desenvolvimento

- **Licença:** A definir

---

**Projeto acadêmico:** Atividade prática de Programação Web.