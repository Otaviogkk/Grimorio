## Identificação do Projeto

**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Piauí (IFPI)

**Disciplina:** Programação Web

**Projeto:** Grimório — Organizador de Fichas de RPG

### Integrantes do grupo

- José Otavio Luciano Sousa Chagas
- Ronalty Hauan Gomes Galvão dos Santos

### Professor responsável

**Anthony Irlan Marques Luz**

### Finalidade acadêmica

Projeto desenvolvido como atividade prática da disciplina de Programação Web, com o objetivo de aplicar conhecimentos de desenvolvimento web, construção de APIs REST, integração com banco de dados, autenticação, testes e documentação de software.

### Grimório — Organizador de Fichas de RPG

#### 1. Sobre o projeto

O **Grimório** é uma aplicação web desenvolvida como atividade prática da disciplina de **Programação Web**. Seu objetivo é permitir que jogadores organizem, personalizem e gerenciem as fichas de seus personagens de RPG em um único lugar.

A aplicação permitirá cadastrar personagens, registrar atributos e perícias, administrar habilidades, controlar inventários, acompanhar a evolução dos personagens e organizar suas campanhas.

O projeto será desenvolvido utilizando Python e FastAPI no backend, com uma API REST para comunicação com a interface web e um banco de dados relacional para armazenar as informações.

A proposta é desenvolver a aplicação progressivamente, aplicando os conceitos estudados durante a disciplina e utilizando como referência a metodologia prática do curso [FastAPI do Zero](https://fastapidozero.dunossauro.com/estavel/01/).

## 2. Objetivos

- Aplicar os conhecimentos de desenvolvimento web na construção de uma aplicação funcional.
- Desenvolver uma API REST utilizando FastAPI.
- Implementar operações CRUD para o gerenciamento dos dados.
- Modelar e integrar um banco de dados relacional.
- Implementar autenticação e autorização de usuários.
- Construir uma interface web responsiva e intuitiva.
- Desenvolver testes automatizados para validar o funcionamento da aplicação.
- Utilizar Git e GitHub para versionamento e documentação do projeto.
- Aplicar boas práticas de organização, segurança e manutenção de código.

## 3. Tecnologias utilizadas

O projeto utilizará tecnologias do ecossistema Python, seguindo a abordagem de desenvolvimento apresentada no FastAPI do Zero.

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal do backend. |
| FastAPI | Criação da API REST e gerenciamento das rotas. |
| Pydantic | Validação dos dados recebidos e enviados pela API. |
| SQLAlchemy | Mapeamento objeto-relacional (ORM) e comunicação com o banco de dados. |
| SQLite | Banco de dados inicial para desenvolvimento local. |
| PostgreSQL | Banco de dados previsto para implantação em produção. |
| Alembic | Controle e execução de migrações do banco de dados. |
| HTML5 | Estrutura das páginas web. |
| CSS3 | Estilização e responsividade da interface. |
| JavaScript | Interatividade e integração da interface com a API. |
| JWT | Autenticação por tokens, quando aplicável à estratégia de sessão escolhida. |
| pytest | Testes automatizados da aplicação. |
| Ruff | Análise estática e formatação do código Python. |
| Git e GitHub | Versionamento e colaboração. |
| Docker | Containerização da aplicação, prevista para uma etapa posterior. |

As dependências e suas versões serão definidas no arquivo `pyproject.toml`. O ambiente será configurado de acordo com as versões compatíveis das bibliotecas escolhidas.

## 4. Funcionalidades do sistema

### 4.1. Cadastro e autenticação de usuários

Cada usuário deverá possuir uma conta própria para organizar seus personagens.

- [ ] Cadastro de usuários.
- [ ] Login com e-mail e senha.
- [ ] Logout.
- [ ] Validação dos campos de cadastro.
- [ ] Armazenamento seguro das senhas por meio de hash.
- [ ] Autenticação das requisições protegidas.
- [ ] Recuperação de senha, em uma etapa posterior.
- [ ] Edição dos dados básicos do perfil.
- [ ] Exclusão da conta.
- [ ] Proteção dos dados para impedir que um usuário acesse personagens de outra conta.
- [ ] Tratamento de sessões expiradas e tokens inválidos.

### 4.2. Painel principal

Após entrar no sistema, o usuário terá acesso a um painel com um resumo de seus personagens e campanhas.

- [ ] Exibir a quantidade total de personagens cadastrados.
- [ ] Listar os personagens recentemente acessados.
- [ ] Exibir personagens favoritos.
- [ ] Mostrar o nome, a imagem, o sistema de RPG e o nível de cada personagem.
- [ ] Criar um personagem diretamente pelo painel.
- [ ] Pesquisar personagens pelo nome.
- [ ] Filtrar personagens por sistema, classe, nível ou campanha.
- [ ] Ordenar personagens por nome, nível ou data de atualização.
- [ ] Acessar rapidamente a ficha completa de um personagem.
- [ ] Exibir mensagens de sucesso, erro e confirmação das operações.

### 4.3. Criação e gerenciamento de personagens

O sistema deverá permitir o gerenciamento completo das fichas dos personagens.

- [ ] Criar personagens.
- [ ] Consultar fichas cadastradas.
- [ ] Editar os dados de um personagem.
- [ ] Excluir personagens mediante confirmação.
- [ ] Duplicar uma ficha para criar um personagem semelhante.
- [ ] Marcar personagens como favoritos.
- [ ] Definir nome, apelido, idade, gênero ou outras informações opcionais.
- [ ] Adicionar uma imagem ou retrato.
- [ ] Registrar raça, espécie ou ancestralidade.
- [ ] Registrar classe, profissão ou arquétipo.
- [ ] Definir nível, experiência e alinhamento, quando aplicável.
- [ ] Registrar origem, história, personalidade e objetivos.
- [ ] Adicionar aparência física, características e anotações.
- [ ] Registrar o sistema de RPG utilizado.
- [ ] Informar a campanha à qual o personagem pertence.
- [ ] Registrar o criador e as datas de criação e atualização da ficha.

Os campos deverão ser adaptáveis ao sistema de RPG selecionado, evitando exigir informações que não existam em determinadas regras.

### 4.4. Atributos e características

Cada personagem poderá possuir atributos numéricos e características próprias.

- [ ] Cadastrar atributos básicos, como força, destreza, constituição, inteligência, sabedoria e carisma.
- [ ] Permitir atributos personalizados conforme o sistema de RPG.
- [ ] Registrar os valores dos atributos.
- [ ] Calcular modificadores automaticamente quando as regras cadastradas permitirem.
- [ ] Registrar bônus e penalidades.
- [ ] Exibir os atributos de maneira organizada na ficha.
- [ ] Validar valores permitidos.
- [ ] Atualizar os cálculos após a alteração dos atributos.

**Observação:** os atributos e suas fórmulas não serão fixos para todos os sistemas. As regras específicas deverão ser configuráveis ou implementadas separadamente para cada sistema de RPG suportado.

### 4.5. Perícias e proficiências

- [ ] Cadastrar perícias.
- [ ] Definir o valor de cada perícia.
- [ ] Registrar proficiências, especializações e conhecimentos.
- [ ] Associar perícias aos atributos correspondentes.
- [ ] Calcular bônus de perícia quando as regras estiverem implementadas.
- [ ] Adicionar perícias personalizadas.
- [ ] Exibir os valores na ficha do personagem.

### 4.6. Combate e sobrevivência

A ficha deverá possuir uma área dedicada às informações utilizadas durante o combate.

- [ ] Registrar pontos de vida máximos e atuais.
- [ ] Registrar pontos de mana, energia ou recurso equivalente.
- [ ] Registrar classe de armadura ou defesa.
- [ ] Registrar iniciativa, deslocamento e velocidade.
- [ ] Registrar resistências, imunidades e vulnerabilidades.
- [ ] Controlar condições e estados temporários.
- [ ] Registrar dados de morte, inconsciência ou recuperação, quando aplicável.
- [ ] Registrar ataques e respectivos bônus.
- [ ] Registrar dano, alcance, tipo de dano e propriedades dos ataques.
- [ ] Permitir atualizar recursos durante uma sessão de jogo.
- [ ] Validar limites configurados para cada recurso.
- [ ] Exibir barras visuais para pontos de vida e outros recursos.

### 4.7. Habilidades, talentos e poderes

- [ ] Cadastrar habilidades, talentos, poderes, magias e características especiais.
- [ ] Registrar nome e descrição.
- [ ] Definir categoria e nível da habilidade.
- [ ] Registrar custo de utilização.
- [ ] Registrar alcance, duração e tempo de execução.
- [ ] Informar pré-requisitos.
- [ ] Registrar efeitos e limitações.
- [ ] Organizar habilidades por categoria.
- [ ] Pesquisar habilidades cadastradas.
- [ ] Associar habilidades a um personagem.
- [ ] Editar e remover habilidades.
- [ ] Identificar habilidades passivas e ativas.
- [ ] Registrar usos disponíveis e limites de utilização, quando aplicável.

### 4.8. Inventário e equipamentos

O inventário permitirá controlar os itens carregados pelo personagem.

- [ ] Adicionar itens ao inventário.
- [ ] Editar e remover itens.
- [ ] Registrar nome, descrição e categoria do item.
- [ ] Definir quantidade e peso.
- [ ] Registrar valor monetário.
- [ ] Controlar moedas e outros recursos financeiros.
- [ ] Marcar equipamentos como equipados ou guardados.
- [ ] Registrar armas, armaduras, acessórios, consumíveis e itens mágicos.
- [ ] Associar propriedades e bônus aos equipamentos.
- [ ] Calcular o peso total carregado.
- [ ] Definir limites de carga quando suportados pelo sistema de RPG.
- [ ] Registrar itens consumidos, perdidos ou transferidos.
- [ ] Exibir o inventário organizado por categoria.

### 4.9. Magias e recursos especiais

Para sistemas que utilizam magia ou recursos semelhantes:

- [ ] Cadastrar magias e habilidades sobrenaturais.
- [ ] Registrar círculos, níveis ou categorias.
- [ ] Definir custo e requisitos de utilização.
- [ ] Registrar componentes, alcance e duração.
- [ ] Controlar espaços de magia ou cargas disponíveis.
- [ ] Associar magias conhecidas ao personagem.
- [ ] Separar magias preparadas e conhecidas, quando aplicável.
- [ ] Restaurar recursos conforme as regras configuradas.
- [ ] Permitir sistemas alternativos de energia e recursos.

### 4.10. Evolução do personagem

- [ ] Registrar experiência atual e necessária para o próximo nível.
- [ ] Atualizar o nível do personagem.
- [ ] Registrar histórico de evolução.
- [ ] Registrar mudanças de atributos.
- [ ] Registrar habilidades e talentos adquiridos.
- [ ] Registrar mudanças de classe, profissão ou especialização.
- [ ] Manter anotações sobre eventos importantes.
- [ ] Consultar evoluções anteriores.
- [ ] Aplicar cálculos automáticos de progressão quando as regras do sistema estiverem implementadas.

### 4.11. Campanhas e sessões de jogo

O sistema poderá organizar personagens em campanhas e registrar acontecimentos das aventuras.

- [ ] Criar campanhas.
- [ ] Definir nome, descrição e sistema de RPG da campanha.
- [ ] Registrar mestre e participantes.
- [ ] Associar personagens à campanha.
- [ ] Registrar sessões de jogo.
- [ ] Definir data e título de cada sessão.
- [ ] Registrar resumos das aventuras.
- [ ] Manter diário de acontecimentos.
- [ ] Registrar missões, objetivos e recompensas.
- [ ] Marcar missões como pendentes, concluídas ou falhas.
- [ ] Registrar NPCs e organizações importantes.
- [ ] Consultar o histórico de sessões.
- [ ] Permitir que o usuário mantenha notas privadas.

### 4.12. Exportação e importação de fichas

- [ ] Exportar fichas para JSON.
- [ ] Importar fichas de arquivos JSON compatíveis.
- [ ] Validar os dados importados antes de salvá-los.
- [ ] Permitir imprimir fichas em um formato adequado.
- [ ] Gerar uma versão de ficha em PDF em uma etapa posterior.
- [ ] Exportar inventário e histórico de evolução.
- [ ] Tratar arquivos inválidos e versões incompatíveis.
- [ ] Evitar sobrescrever personagens existentes sem confirmação.

### 4.13. Personalização da interface

- [ ] Interface adaptável para computadores, tablets e celulares.
- [ ] Tema claro e tema escuro.
- [ ] Personalização do retrato e da aparência da ficha.
- [ ] Organização das informações em abas ou seções.
- [ ] Formulários com validação e mensagens de erro.
- [ ] Confirmação antes de operações destrutivas.
- [ ] Navegação acessível por teclado.
- [ ] Contraste e legibilidade adequados.
- [ ] Estados visuais para carregamento, ausência de dados e falhas.
- [ ] Interface consistente em todas as páginas.

### 4.14. Administração e segurança dos dados

- [ ] Garantir que cada usuário acesse somente os dados autorizados.
- [ ] Validar os dados no backend, independentemente das validações do frontend.
- [ ] Utilizar consultas parametrizadas e os recursos seguros do ORM.
- [ ] Configurar variáveis de ambiente para informações sensíveis.
- [ ] Tratar erros sem expor detalhes internos da aplicação.
- [ ] Implementar exclusão controlada de personagens e campanhas.
- [ ] Definir regras para exclusão de dados relacionados.
- [ ] Criar registros de auditoria para operações importantes, se necessário.
- [ ] Implementar cópias de segurança conforme o ambiente de implantação.

## 5. Requisitos funcionais

Os requisitos funcionais descrevem as ações que o sistema deverá executar.

| Código | Requisito |
|---|---|
| RF01 | O sistema deve permitir cadastrar usuários. |
| RF02 | O sistema deve autenticar usuários. |
| RF03 | O sistema deve permitir criar, consultar, editar e excluir personagens. |
| RF04 | O sistema deve associar cada personagem ao seu proprietário. |
| RF05 | O sistema deve permitir cadastrar e editar atributos e perícias. |
| RF06 | O sistema deve permitir gerenciar habilidades e poderes. |
| RF07 | O sistema deve permitir gerenciar inventário e equipamentos. |
| RF08 | O sistema deve controlar os recursos do personagem. |
| RF09 | O sistema deve permitir registrar a evolução dos personagens. |
| RF10 | O sistema deve permitir organizar personagens em campanhas. |
| RF11 | O sistema deve permitir pesquisar, filtrar e ordenar personagens. |
| RF12 | O sistema deve validar dados enviados pela interface e pela API. |
| RF13 | O sistema deve permitir exportar e importar fichas em formato JSON. |
| RF14 | O sistema deve apresentar mensagens apropriadas para operações realizadas e erros. |
| RF15 | O sistema deve proteger informações privadas e impedir acessos não autorizados. |

## 6. Requisitos não funcionais

| Código | Requisito |
|---|---|
| RNF01 | A aplicação deve possuir interface responsiva. |
| RNF02 | O backend deve ser desenvolvido em Python utilizando FastAPI. |
| RNF03 | A API deve seguir uma estrutura REST e utilizar códigos HTTP apropriados. |
| RNF04 | Os dados persistentes devem ser armazenados em banco de dados relacional. |
| RNF05 | O código deve ser organizado em módulos e apresentar responsabilidades bem definidas. |
| RNF06 | As operações principais devem possuir testes automatizados. |
| RNF07 | As senhas nunca devem ser armazenadas em texto puro. |
| RNF08 | As credenciais e chaves secretas devem ficar fora do código-fonte. |
| RNF09 | A documentação da API deve estar disponível por meio do OpenAPI e da interface de documentação do FastAPI. |
| RNF10 | A aplicação deve apresentar mensagens de erro compreensíveis. |
| RNF11 | As migrações do banco de dados devem ser versionadas. |
| RNF12 | O projeto deve utilizar Git para controle de versão. |
| RNF13 | A aplicação deve permitir manutenção e inclusão de novas funcionalidades sem reescrever toda a estrutura. |
| RNF14 | A interface deve observar princípios básicos de acessibilidade e usabilidade. |

## 7. Arquitetura da aplicação

A aplicação será dividida em três partes principais:

1. **Frontend:** interface desenvolvida com HTML, CSS e JavaScript, responsável pela interação com o usuário.
2. **Backend:** API desenvolvida com FastAPI, responsável pelas regras de negócio, validação, autenticação e processamento das requisições.
3. **Banco de dados:** responsável por armazenar usuários, personagens, atributos, habilidades, inventários e campanhas.

Fluxo básico de funcionamento:

```text
Usuário
   |
   v
Interface Web
HTML + CSS + JavaScript
   |
   | Requisições HTTP / JSON
   v
API REST
FastAPI + Pydantic
   |
   v
Regras de negócio
   |
   v
SQLAlchemy
   |
   v
Banco de dados
SQLite / PostgreSQL
```

## 8. Organização inicial do projeto

A estrutura será organizada para separar a configuração, as rotas, os modelos, as regras de negócio e os testes.

```text
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
│   ├── services/
│   │   ├── personagens.py
│   │   └── campanhas.py
│   └── templates/
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
├── tests/
│   ├── test_usuarios.py
│   ├── test_autenticacao.py
│   └── test_personagens.py
├── alembic/
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── Dockerfile
```

A estrutura poderá ser ajustada durante o desenvolvimento. Os diretórios e módulos serão adicionados conforme a aplicação crescer, evitando criar complexidade desnecessária nas primeiras etapas.

## 9. API REST

As rotas abaixo representam uma proposta inicial para a API.

### Usuários e autenticação

| Método | Rota | Descrição |
|---|---|---|
| POST | `/usuarios/` | Cadastrar usuário. |
| POST | `/auth/login` | Autenticar usuário. |
| GET | `/usuarios/me` | Consultar o usuário autenticado. |
| PATCH | `/usuarios/me` | Atualizar os dados do perfil. |
| DELETE | `/usuarios/me` | Excluir a própria conta. |

### Personagens

| Método | Rota | Descrição |
|---|---|---|
| POST | `/personagens/` | Criar personagem. |
| GET | `/personagens/` | Listar personagens do usuário. |
| GET | `/personagens/{personagem_id}` | Consultar ficha completa. |
| PATCH | `/personagens/{personagem_id}` | Atualizar personagem. |
| DELETE | `/personagens/{personagem_id}` | Excluir personagem. |
| POST | `/personagens/{personagem_id}/duplicar` | Duplicar personagem. |

### Atributos e habilidades

| Método | Rota | Descrição |
|---|---|---|
| GET | `/personagens/{personagem_id}/atributos` | Listar atributos. |
| PUT | `/personagens/{personagem_id}/atributos` | Atualizar atributos. |
| GET | `/personagens/{personagem_id}/habilidades` | Listar habilidades. |
| POST | `/personagens/{personagem_id}/habilidades` | Adicionar habilidade. |
| PATCH | `/habilidades/{habilidade_id}` | Editar habilidade. |
| DELETE | `/habilidades/{habilidade_id}` | Remover habilidade. |

### Inventário e campanhas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/personagens/{personagem_id}/inventario` | Consultar inventário. |
| POST | `/personagens/{personagem_id}/inventario` | Adicionar item. |
| PATCH | `/itens/{item_id}` | Atualizar item. |
| DELETE | `/itens/{item_id}` | Remover item. |
| POST | `/campanhas/` | Criar campanha. |
| GET | `/campanhas/` | Listar campanhas. |
| GET | `/campanhas/{campanha_id}` | Consultar campanha. |
| PATCH | `/campanhas/{campanha_id}` | Atualizar campanha. |
| DELETE | `/campanhas/{campanha_id}` | Excluir campanha. |

As rotas são uma proposta inicial. Seus contratos, parâmetros, respostas e regras de autorização serão definidos durante a implementação. As operações que modificam dados deverão exigir autenticação e verificar a propriedade ou a permissão de acesso ao recurso.

## 10. Modelagem inicial do banco de dados

As principais entidades previstas são:

- **Usuario:** identificação, e-mail, hash da senha e dados de perfil.
- **Personagem:** proprietário, nome, descrição, imagem, sistema de RPG, nível e informações básicas.
- **Atributo:** nome, valor e personagem associado.
- **Pericia:** nome, valor, proficiência e personagem associado.
- **Habilidade:** nome, descrição, categoria, custo e requisitos.
- **PersonagemHabilidade:** associação entre personagens e habilidades, incluindo informações específicas da aquisição.
- **Item:** nome, descrição, categoria, peso e valor.
- **InventarioItem:** personagem, item, quantidade e estado de equipamento.
- **Campanha:** proprietário, nome, descrição e sistema de RPG.
- **CampanhaPersonagem:** associação entre personagens e campanhas.
- **Sessao:** campanha, data, título e resumo.
- **Missao:** campanha, descrição, objetivo e estado.
- **HistoricoEvolucao:** personagem, data, nível e descrição das mudanças.

Relacionamentos, restrições de integridade e regras de exclusão serão definidos com SQLAlchemy e controlados por migrações do Alembic.

## 11. Etapas de desenvolvimento

O projeto será desenvolvido por etapas, permitindo entregar uma versão funcional antes de implementar recursos mais avançados.

### Etapa 1 — Configuração do ambiente

- [ ] Criar o repositório Git.
- [ ] Configurar o Python e o ambiente virtual.
- [ ] Configurar o projeto com `pyproject.toml`.
- [ ] Instalar FastAPI e suas dependências.
- [ ] Configurar Ruff.
- [ ] Criar a aplicação inicial.
- [ ] Executar o servidor localmente.
- [ ] Documentar como iniciar o projeto.

### Etapa 2 — Primeira API e operações CRUD

- [ ] Criar as primeiras rotas.
- [ ] Definir schemas com Pydantic.
- [ ] Implementar cadastro e consulta de personagens.
- [ ] Implementar atualização e exclusão.
- [ ] Validar entradas e respostas.
- [ ] Utilizar corretamente os códigos de status HTTP.
- [ ] Testar as rotas pela documentação automática do FastAPI.

### Etapa 3 — Banco de dados

- [ ] Configurar SQLAlchemy.
- [ ] Criar os modelos de dados.
- [ ] Integrar a API ao SQLite.
- [ ] Configurar Alembic.
- [ ] Criar e executar migrações.
- [ ] Persistir os personagens entre reinicializações.
- [ ] Implementar os relacionamentos necessários.

### Etapa 4 — Usuários e segurança

- [ ] Implementar cadastro e autenticação.
- [ ] Configurar hash seguro de senhas.
- [ ] Proteger as rotas privadas.
- [ ] Associar os personagens aos seus proprietários.
- [ ] Validar permissões de acesso.
- [ ] Implementar tratamento de erros de autenticação.

### Etapa 5 — Interface web

- [ ] Criar a página inicial.
- [ ] Criar as páginas de cadastro e login.
- [ ] Criar o painel principal.
- [ ] Desenvolver os formulários de personagens.
- [ ] Integrar a interface à API.
- [ ] Exibir mensagens de sucesso e erro.
- [ ] Implementar pesquisa, filtros e responsividade.

### Etapa 6 — Funcionalidades da ficha

- [ ] Implementar atributos e perícias.
- [ ] Implementar habilidades e poderes.
- [ ] Implementar combate e recursos.
- [ ] Implementar inventário.
- [ ] Implementar evolução.
- [ ] Implementar campanhas e sessões.
- [ ] Adicionar regras específicas para os sistemas de RPG escolhidos.

### Etapa 7 — Testes e qualidade

- [ ] Criar testes unitários.
- [ ] Criar testes das rotas da API.
- [ ] Testar os fluxos de autenticação.
- [ ] Testar permissões e isolamento de dados.
- [ ] Testar entradas inválidas e erros.
- [ ] Verificar os relacionamentos do banco de dados.
- [ ] Corrigir problemas encontrados.

### Etapa 8 — Finalização e implantação

- [ ] Revisar a estrutura do projeto.
- [ ] Atualizar o README.
- [ ] Configurar as variáveis de ambiente.
- [ ] Preparar o PostgreSQL para produção.
- [ ] Configurar Docker, se previsto na atividade.
- [ ] Automatizar os testes com integração contínua.
- [ ] Implantar a aplicação em um serviço compatível.
- [ ] Validar o funcionamento da versão implantada.

## 12. Escopo da primeira versão (MVP)

Para manter a atividade viável e garantir uma entrega funcional, a primeira versão deverá priorizar as seguintes funcionalidades:

- [ ] Cadastro e login de usuários.
- [ ] Painel principal.
- [ ] Criação, consulta, edição e exclusão de personagens.
- [ ] Cadastro e edição de atributos.
- [ ] Cadastro de habilidades.
- [ ] Gerenciamento básico do inventário.
- [ ] Persistência dos dados em SQLite.
- [ ] Interface web integrada à API.
- [ ] Validação dos dados.
- [ ] Controle de acesso por usuário.
- [ ] Testes das operações principais.
- [ ] Documentação da instalação e execução.

Recursos como campanhas completas, PDF, importação avançada, múltiplos sistemas de regras, compartilhamento de fichas e Docker em produção poderão ser desenvolvidos após a conclusão do MVP, conforme o tempo disponível.

## 13. Como executar o projeto

Os comandos definitivos serão atualizados conforme as dependências e a estrutura forem implementadas.

### Pré-requisitos

- Python em uma versão compatível com as dependências do projeto.
- Git.
- Editor de código, como Visual Studio Code.
- Terminal compatível com o sistema operacional.

### Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd grimorio
```

### Criar o ambiente virtual

No Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Instalar as dependências

Após configurar o `pyproject.toml`:

```bash
pip install -e ".[dev]"
```

Esse comando pressupõe que o projeto declare um grupo ou extra de dependências de desenvolvimento chamado `dev`. A configuração deverá ser incluída no arquivo antes de utilizar o comando.

### Executar a aplicação

Quando o módulo principal estiver configurado:

```bash
fastapi dev app/main.py
```

A documentação interativa da API estará disponível, por padrão, em:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 14. Testes

Os testes automatizados serão desenvolvidos utilizando pytest e as ferramentas de teste compatíveis com FastAPI.

Para executar a suíte de testes:

```bash
pytest
```

Os testes deverão verificar:

- Cadastro e consulta de personagens.
- Atualização e exclusão de registros.
- Validação de campos obrigatórios.
- Comportamento diante de dados inválidos.
- Autenticação e autorização.
- Proteção dos dados de diferentes usuários.
- Persistência e relacionamentos do banco de dados.
- Respostas HTTP esperadas.

## 15. Segurança e boas práticas

Durante o desenvolvimento, serão observados os seguintes princípios:

- Senhas armazenadas somente por meio de hash seguro.
- Segredos e credenciais mantidos em variáveis de ambiente.
- Arquivo `.env` incluído no `.gitignore`.
- Validação de dados no backend.
- Verificação de permissões em todas as operações protegidas.
- Tratamento apropriado de erros e exceções.
- Controle de integridade do banco de dados.
- Separação entre modelos de persistência e schemas de entrada e saída.
- Versionamento das alterações do banco de dados.
- Testes automatizados para regras de negócio importantes.
- Revisão das configurações de segurança antes da implantação.

## 16. Resultados esperados

Ao final da atividade, espera-se obter uma aplicação web funcional para gerenciamento de fichas de RPG, com interface própria, API REST, banco de dados integrado, autenticação e operações CRUD.

O projeto também deverá demonstrar a aplicação prática dos conceitos de programação web, arquitetura cliente-servidor, persistência de dados, validação, segurança, testes e versionamento de código.

Além do produto final, o desenvolvimento servirá como exercício de organização de um projeto real, desde a configuração do ambiente até a documentação e a preparação para implantação.

## 17. Referências

- [FastAPI do Zero — Aula 01: Configurando o ambiente de desenvolvimento](https://fastapidozero.dunossauro.com/estavel/01/)
- [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/)
- [Documentação oficial do Pydantic](https://docs.pydantic.dev/)
- [Documentação oficial do SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentação oficial do Alembic](https://alembic.sqlalchemy.org/)
- [Documentação oficial do pytest](https://docs.pytest.org/)

---

**Projeto acadêmico:** Atividade prática de Programação Web.

**Nome do projeto:** Grimório — Organizador de Fichas de RPG.

**Status:** Em planejamento e desenvolvimento.

**Licença:** A definir.

## 18. Ferramentas e recursos utilizados

Esta seção apresenta as tecnologias, ferramentas de desenvolvimento e recursos de inteligência artificial utilizados como apoio à implementação, documentação, testes e manutenção do projeto.

### 18.1. Ambiente de desenvolvimento

| Ferramenta | Finalidade |
|---|---|
| Visual Studio Code | Editor de código-fonte utilizado no desenvolvimento. |
| Python | Linguagem de programação utilizada no backend. |
| FastAPI | Desenvolvimento da API REST. |
| Git | Controle de versão do código-fonte. |
| GitHub | Hospedagem do repositório e acompanhamento do desenvolvimento. |
| SQLite | Armazenamento de dados durante o desenvolvimento inicial. |
| Ruff | Análise estática e formatação do código Python. |
| pytest | Execução de testes automatizados. |

### 18.2. Inteligência artificial como apoio ao desenvolvimento

As ferramentas de inteligência artificial poderão ser utilizadas como recursos auxiliares durante o desenvolvimento, com o objetivo de facilitar o aprendizado, a resolução de problemas e a elaboração de código.

| Ferramenta | Finalidade |
|---|---|
| ChatGPT — OpenAI | Apoio à compreensão de conceitos, elaboração de exemplos de código, identificação de erros, revisão de implementações e produção de documentação técnica. |
| Microsoft Copilot | Apoio à escrita de código, sugestões de implementação, explicação de trechos de código e auxílio na identificação de possíveis problemas, conforme a ferramenta e os recursos disponíveis. |

### 18.3. Forma de utilização das ferramentas de IA

As ferramentas de inteligência artificial serão utilizadas como apoio, e não como substitutas do processo de aprendizagem e desenvolvimento.

Sua utilização poderá incluir:

- Consultar explicações sobre Python, FastAPI, APIs REST e bancos de dados.
- Obter exemplos de implementação para estudo e adaptação.
- Auxiliar na identificação e correção de erros.
- Revisar a organização e a legibilidade do código.
- Elaborar documentação técnica e instruções de instalação.
- Sugerir casos de teste e cenários de validação.
- Investigar possíveis soluções para problemas encontrados durante o desenvolvimento.

Todo código sugerido por ferramentas de IA deverá ser analisado, testado e validado antes de ser incorporado ao projeto. A responsabilidade pela implementação final, pelas decisões técnicas e pela compreensão do código permanece com o desenvolvedor.

### 18.4. Referências das ferramentas

- [Visual Studio Code](https://code.visualstudio.com/)
- [Microsoft Copilot](https://copilot.microsoft.com/)
- [ChatGPT](https://chatgpt.com/)
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [SQLite](https://www.sqlite.org/)
- [Ruff](https://docs.astral.sh/ruff/)
- [pytest](https://docs.pytest.org/)

**Observação:** esta relação deve refletir as ferramentas efetivamente utilizadas durante a atividade. Caso alguma ferramenta não tenha sido utilizada, ela deverá ser removida da lista ou identificada apenas como recurso previsto.
