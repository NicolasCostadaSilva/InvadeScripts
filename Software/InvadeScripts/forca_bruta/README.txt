Olá, aqui explicarei as funcionalidades implementadas, como tudo foi construído e o que aprendi nesse caminho.

Primeiramente, o arquivo app.py foi criado, junto com os arquivos HTML dentro da pasta template. O app.py utiliza Flask, um framework
para desenvolvimento web. Nele, podemos emular um site e, como o foco do estudo era um ataque de força bruta, foi feito um site de login básico.
Dentro do app.py, estão comentadas as funções de cada parte. Basicamente, ele recebe as informações do usuário, registrando ou tentando
fazer login, e os códigos HTML dentro da pasta template são a nossa visualização desse site.

Após o site estar funcionando, foi criado o forcaBruta.py. Nele, a proposta é procurar a senha do usuário, que neste caso será sempre numérica. Para isso,
foram utilizadas as bibliotecas "requests" e "time". A segunda é utilizada apenas para contar o tempo de execução do programa, enquanto a "requests" é
responsável por interagir com nosso servidor web, permitindo que o programa insira o usuário e procure pela senha. Para encontrar a senha, o programa
faz um loop incrementando a senha até encontrar a correta. Dependendo do tamanho da senha, o tempo para encontrar pode ser muito longo. Ao encontrar a 
senha, ele retorna o usuário e sua senha, juntamente com o tempo de execução do programa. Vale lembrar que você deve alterar os lugares indicados nos
comentarios para que seu caso funcione adequadamente.

Para utilizar, você deve executar o app.py, inserir as informações básicas no forçaBruta.py nos campos indicados e, com uma conta criada no banco de dados, realizar os testes executando o forçaBruta.py.

Ao realizar esse trabalho, aprendi sobre o Flask, todas as suas funcionalidades e utilidades, e também entendi melhor o banco de dados que
usamos para o servidor. Criar um script que funcione nesse caso foi ótimo e agregou bastante conhecimento.
