import os
import socket


def get(request, addr):
    sock.sendto(request, addr)
    return sock.recv(1024)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    UDP_IP = os.getenv("UDP_IP", default="0.0.0.0")
    UDP_PORT = os.getenv("UDP_PORT", default=2000)
    sock.bind((UDP_IP, UDP_PORT))

    MCAST_GRP = os.getenv("MCAST_GRP", default="224.1.1.1")
    MULTICAST_TTL = 2
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

    SERDES_UDP_PORT = os.getenv("SERDES_UDP_PORT", default=2000)
    FORMAT_CNT = 7

    while True:
        try:
            data, addr = sock.recvfrom(64 * 1024 - 1)
            request, format = data.split()
            if format == b"all":
                sock.sendto(request, (MCAST_GRP, SERDES_UDP_PORT))
                results = [sock.recv(64 * 1024 - 1) for i in range(FORMAT_CNT)]
                sock.sendto(b'\n'.join(results), addr)
            else:
                sock.sendto(get(request, (format, SERDES_UDP_PORT)), addr)
        except Exception as e:
            print(e)
