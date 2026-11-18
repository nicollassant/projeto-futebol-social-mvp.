# Auto-revisão técnica do MVP

## Escopo revisado

Foi realizada uma leitura crítica da aplicação Flask, das rotas de cadastro, dos templates e dos testes automatizados existentes. Esta revisão considera o estágio atual do MVP, que ainda implementa a validação inicial do formulário e não realiza persistência em banco de dados.

## Pontos positivos identificados

- **Separação inicial de responsabilidades:** a criação da aplicação está concentrada em `create_app()`, facilitando a configuração e a criação de instâncias para testes.
- **Legibilidade:** nomes de rotas e variáveis estão em português e descrevem sua finalidade; as validações estão organizadas em etapas compreensíveis.
- **Validação no servidor:** campos obrigatórios, data de nascimento, telefone e formato básico de e-mail são verificados no backend, sem depender exclusivamente do navegador.
- **Testabilidade:** há testes para carregamento da página inicial, exibição do formulário, rejeição de dados inválidos e resposta após envio válido.

## Achados e melhorias necessárias

### 1. Segurança — chave de sessão

A aplicação utiliza uma chave padrão quando a variável de ambiente `SECRET_KEY` não está definida. Esse fallback é útil apenas no desenvolvimento local e não deve ser utilizado em produção, pois pode comprometer a segurança das sessões.

**Ação recomendada:** exigir uma chave forte por variável de ambiente em ambientes de produção e manter segredos fora do repositório.

### 2. Segurança — autenticação e autorização

A rota de cadastro ainda não exige autenticação. Como o sistema será utilizado para administrar dados de crianças e responsáveis, permitir acesso público à inclusão de registros não é adequado.

**Ação recomendada:** implementar autenticação administrativa com Flask-Login e proteger as rotas de gestão antes de armazenar dados reais.

### 3. Segurança — proteção CSRF e privacidade

O formulário ainda não possui proteção explícita contra CSRF. Além disso, dados de menores e responsáveis exigem controles de acesso, coleta mínima e armazenamento protegido.

**Ação recomendada:** integrar proteção CSRF, restringir o acesso aos dados e utilizar somente informações fictícias durante o desenvolvimento e os testes.

### 4. Arquitetura — persistência de dados

Atualmente, o formulário valida os dados e apresenta uma mensagem de sucesso, mas não grava as informações. Portanto, a funcionalidade ainda não representa um cadastro persistente.

**Ação recomendada:** integrar SQLAlchemy e MySQL, modelando alunos e responsáveis com relacionamento por chave estrangeira e operações transacionais.

### 5. Refatoração e legibilidade — validações

As regras de validação estão concentradas diretamente na função da rota. Com o crescimento do sistema, isso pode dificultar manutenção e reutilização.

**Ação recomendada:** mover as regras para uma camada de serviço ou módulo de validação, mantendo a rota responsável por receber a requisição e retornar a resposta.

### 6. Testes — cobertura

Os testes atuais verificam os principais caminhos do formulário, mas não cobrem todos os limites das validações, falhas de persistência, autenticação ou proteção CSRF. Também não foi realizada, nesta revisão, uma execução automatizada da suíte.

**Ação recomendada:** ampliar os casos de teste para datas futuras, telefones fora do intervalo, e-mails inválidos, acesso sem autenticação e operações com banco de dados de teste.

## Conclusão da revisão

A estrutura inicial é simples e adequada para a construção incremental do MVP, e já apresenta validação no servidor e testes básicos. Entretanto, a implementação ainda é um protótipo: não persiste dados, não possui autenticação administrativa nem proteção CSRF. Esses pontos devem ser tratados antes de qualquer uso com informações reais. Esta revisão registra os achados e recomendações para orientar as próximas etapas, sem afirmar que as melhorias já foram implementadas.
