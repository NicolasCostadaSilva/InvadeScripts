from struct import unpack
import socket
import sys

# Função para converter endereço MAC de binário para formato legível
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr

# Função para converter endereço IP de binário para formato legível
def get_ip(addr):
    return '.'.join(map(str, addr))

# Função para parse do cabeçalho Ethernet
def ethernet_head(raw_data):
    dest, src, prototype = unpack('! 6s 6s H', raw_data[:14])
    dest_mac = get_mac_addr(dest)
    src_mac = get_mac_addr(src)
    proto = socket.htons(prototype)
    data = raw_data[14:]
    return dest_mac, src_mac, proto, data

# Função para parse do cabeçalho IPv4
def ipv4_head(raw_data):
    version_header_length = raw_data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = unpack('! 8x B B 2x 4s 4s', raw_data[:20])
    src = get_ip(src)
    target = get_ip(target)
    data = raw_data[header_length:]
    return version, header_length, ttl, proto, src, target, data

# Função para parse do cabeçalho TCP
def tcp_head(raw_data):
    (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags) = unpack('! H H L L H', raw_data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    data = raw_data[offset:]
    return src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data

# Função para parse do cabeçalho UDP
def udp_head(raw_data):
    src_port, dest_port, size = unpack('! H H 2x H', raw_data[:8])
    data = raw_data[8:]
    return src_port, dest_port, size, data

# Função para parse do cabeçalho ICMP
def icmp_head(raw_data):
    icmp_type, code, checksum = unpack('! B B H', raw_data[:4])
    data = raw_data[4:]
    return icmp_type, code, checksum, data

# Função principal
def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = s.recvfrom(65535)
        eth = ethernet_head(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(eth[0], eth[1], eth[2]))
        
        if eth[2] == 8:  # IPv4
            ipv4 = ipv4_head(eth[3])
            print('\t - IPv4 Packet:')
            print('\t\t - Version: {}, Header Length: {}, TTL: {}'.format(ipv4[0], ipv4[1], ipv4[2]))
            print('\t\t - Protocol: {}, Source: {}, Target: {}'.format(ipv4[3], ipv4[4], ipv4[5]))
            
            if ipv4[3] == 6:  # TCP
                tcp = tcp_head(ipv4[6])
                print('\t - TCP Segment:')
                print('\t\t - Source Port: {}, Destination Port: {}'.format(tcp[0], tcp[1]))
                print('\t\t - Sequence: {}, Acknowledgment: {}'.format(tcp[2], tcp[3]))
                print('\t\t - Flags:')
                print('\t\t\t - URG: {}, ACK: {}, PSH:{}'.format(tcp[4], tcp[5], tcp[6]))
                print('\t\t\t - RST: {}, SYN: {}, FIN:{}'.format(tcp[7], tcp[8], tcp[9]))
                if len(tcp[10]) > 0:
                    print('\t\t - TCP Data:')
                    print(tcp[10])

            elif ipv4[3] == 1:  # ICMP
                icmp = icmp_head(ipv4[6])
                print('\t - ICMP Packet:')
                print('\t\t - Type: {}, Code: {}, Checksum:{}'.format(icmp[0], icmp[1], icmp[2]))
                print('\t\t - ICMP Data:')
                print(icmp[3])

            elif ipv4[3] == 17:  # UDP
                udp = udp_head(ipv4[6])
                print('\t - UDP Segment:')
                print('\t\t - Source Port: {}, Destination Port: {}, Length: {}'.format(udp[0], udp[1], udp[2]))

if __name__ == "__main__":
    main()
