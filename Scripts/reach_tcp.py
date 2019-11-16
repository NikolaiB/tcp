import socket
import time


def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(1)
        return True
    except:
        return False


def check_host(ip, port):
    ipup = False
    for i in range(3):
        if check_port(ip, port):
            ipup = True
        break
    else:
        time.sleep(2)
    return ipup


def check_connection(ip, port):
    check_port(ip, port)
    check_host(ip, port)
    if check_host(ip, port):
        print(ip + " connection " + str(port) + u" is UP")
    else:
        raise ConnectionError(ip + " connection " + str(port) + u" is DOWN")
