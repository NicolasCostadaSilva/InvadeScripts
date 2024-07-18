# Importação de bibliotecas necessárias
import requests  # Para fazer requisições HTTP
import multiprocessing  # Para criar processos separados
import threading  # Para criar threads dentro dos processos

# Definição da função para enviar requisições de login
def send_login_requests(target_url, count):
    session = requests.Session()  # Cria uma sessão HTTP para manter cookies e cabeçalhos
    for _ in range(count):
        try:
            # Envia uma requisição POST para o target_url com dados de login fixos
            response = session.post(target_url, data={'username': 'testuser', 'password': 'testpassword'})
            print(f"Status Code: {response.status_code}")  # Imprime o código de status da resposta
        except requests.exceptions.RequestException as e:
            print(f"Erro: {e}")  # Em caso de exceção, imprime o erro

# Definição da função para executar requisições em threads
def threaded_requests(target_url, count, num_threads):
    threads = []
    # Cria num_threads threads, cada uma chamando send_login_requests
    for _ in range(num_threads):
        thread = threading.Thread(target=send_login_requests, args=(target_url, count))
        threads.append(thread)
        thread.start()  # Inicia a thread

    for thread in threads:
        thread.join()  # Espera todas as threads terminarem antes de continuar

# Ponto de entrada principal do programa
if __name__ == "__main__":
    target_url = "http://127.0.0.1:1234/login"  # URL alvo para enviar requisições POST de login
    count = 100000  # Número de requisições POST a serem enviadas por cada thread
    num_threads = 100  # Número de threads a serem criadas por processo
    num_processes = multiprocessing.cpu_count()  # Obtém o número de CPUs disponíveis

    processes = []
    # Cria num_processes processos, cada um executando threaded_requests
    for _ in range(num_processes):
        p = multiprocessing.Process(target=threaded_requests, args=(target_url, count, num_threads))
        processes.append(p)
        p.start()  # Inicia o processo

    for p in processes:
        p.join()  # Espera todos os processos terminarem antes de finalizar o programa
