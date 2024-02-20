# 1° Desafio Avançado

1. **Desenvolvimento de uma API RESTful para um Sistema de Blog:**

   - Crie uma API RESTful utilizando Flask-RestAPI.
   - A API deve permitir as seguintes operações:
     - Criar novas postagens.
     - Atualizar postagens existentes.
     - Visualizar postagens, incluindo a capacidade de filtrar por diferentes critérios, como data de publicação, autor, categoria, etc.
     - Excluir postagens.
   - Implemente autenticação e autorização para controlar o acesso às operações da API.
     - Faça login com autenticação de token JWT (JSON Web Token) ou outro método seguro.
     - Proteja as rotas sensíveis, como criar, atualizar e excluir postagens, exigindo tokens válidos.
     - Considere estratégias de hashing e segurança para armazenar senhas de usuário.
   - Utilize boas práticas de design de API, como usar os métodos HTTP apropriados (POST, GET, PUT, DELETE) e URLs significativas.
   - Persista os dados de forma segura em um banco de dados, como SQLite, PostgreSQL ou MongoDB, conforme preferência.

2. **Implementação de Rate Limiting:**

   - Implemente rate limiting em sua aplicação Flask-RestAPI para mitigar possíveis ataques de força bruta ou abuso de recursos.
   - Defina limites de taxa razoáveis para cada rota da API, considerando a capacidade do seu servidor e a expectativa de uso.
   - Utilize bibliotecas adequadas, como Flask-Limiter, para simplificar a implementação e gerenciamento dos limites de taxa.
   - Considere estratégias de fallback ou mensagens de erro claras para lidar com solicitações que excedam os limites de taxa.
   - Teste a funcionalidade de rate limiting para garantir que esteja eficaz e não impeça o uso legítimo da API.

3. **Persistência de Dados:**
   - Utilize um sistema de gerenciamento de banco de dados para persistir os dados do sistema de blog.
   - Escolha um banco de dados que atenda às necessidades da sua aplicação e ofereça segurança e desempenho adequados.
   - Modele o banco de dados de forma eficiente, considerando a estrutura das postagens, usuários, comentários, etc.
   - Implemente lógica de acesso aos dados na sua aplicação, garantindo a integridade e consistência dos dados.
   - Considere estratégias de backup e recuperação para proteger os dados contra perda ou corrupção.
