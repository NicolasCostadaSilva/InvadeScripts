from scapy.all import IP, ICMP, send
import time

def send_icmp_packets(target_ip, count):
    ip = IP(dst=target_ip)
    icmp = ICMP()
    
    try:
        for i in range(count):
            send(ip/icmp, verbose=False)
            if i % 100 == 0:
                print(f"Enviados {i} pacotes ICMP até agora...")
    except KeyboardInterrupt:
        print("Envio de pacotes interrompido pelo usuário.")

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Alvo é a própria máquina
    count = 100000            # Número de pacotes a serem enviados          # Atraso entre pacotes (em segundos)
    
    send_icmp_packets(target_ip, count)
