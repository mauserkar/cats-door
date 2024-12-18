import socket

import cats_door.logger as logger
from cats_door.config import env
from cats_door.web import index_html
from cats_door.utils import parse_request_to_dict


def start_server():
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    logger.info(f'server http://{env["network_ip"]}:80')

    while True:
        cl, addr = s.accept()
        request = cl.recv(1024).decode("utf-8")
        request_dict = parse_request_to_dict(request)

        # print("client ip:", addr[0])
        logger.debug(request_dict)

        if "/?led=on" in request:
            # led.value(1)
            # print(led.value())
            print("debug: led on")

        elif "/?led=off" in request:
            # led.value(0)
            # print(led.value())
            print("debug: led off")
        else:
            response = index_html()

        # HTTP response
        cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        cl.send("<html><body><h1>{}</h1></body></html>".format(response))
        cl.close()
