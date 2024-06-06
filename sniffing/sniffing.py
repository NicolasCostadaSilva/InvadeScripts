from scapy.all import sniff, TCP, Raw
import requests

print('Sniff started, press CTRL + C to finish')

def freeze_login():
    requests.get('http://127.0.0.1:1234')

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load
        if b"POST /" in payload:
            print(payload.decode(errors='ignore'))
            freeze_login()

# Sniffar pacotes na interface 'lo' (loopback) na porta 1233
sniff(iface="lo", prn=packet_callback, filter="tcp port 1234", store=0)