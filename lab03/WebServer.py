import sys, socket, threading

# HOST_NAME =
hostName = "127.0.0.1"
CHUNK_SIZE = 0xFFF
decoder = "ascii"
HTTP_OK = "200 OK"
HTTP_NO_CONTENT = "204 No Content"
HTTP_NOT_FOUND = "404 Not Found"
HTTP_RESPONSE_TOP = "HTTP/1.1"
PNG = "image/png"
TXT = "text/html"
TIMEOUT = 2


def main():

    if len(sys.argv) < 2:
        print("Required Arguments: [port]")
        return 0
    print("Server starting!!")
    port = int(sys.argv[1])
    # hostName = socket.gethostbyname(socket.gethostname()) # TEST!
    address = (hostName, port)
    # i) Create a connection socket when contacted by a client (browser).
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen()

    # (ii) Receive HTTP requests from this connection. Your server should only process GET requests. You may assume that only GET requests will be received.
    while True:
        (sock, addr) = server.accept()
        thread = threading.Thread(target=handle_client, args=(sock, addr, port))
        try:
            # sock.settimeout(TIMEOUT)
            thread.start()
            print(f"[Active Connections] {threading.active_count() - 1}")
        except Exception as err:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            print(err)
            continue


def HTTP_response(code: str, content: str, length: int):
    return (
        HTTP_RESPONSE_TOP
        + " "
        + code
        + "\n\r"
        + f"""Connection: Keep-Alive\n\rContent-Type: {content}\n\rContent-Length: {length}\n\rKeep-Alive: timeout={TIMEOUT}, max=10\r\n\r\n"""
    )


def handle_client(sock: socket, addr, serverPort: int):
    # (iii) Parse the request to determine the specific file being requested.

    connected = True
    while connected:
        msg: bytes = sock.recv(CHUNK_SIZE)
        HTTP_data = msg.decode(decoder).split("\r\n")
        HTTP_req = HTTP_data[0]
        # (iv) Get the requested file from the server's file system.
        request = HTTP_req.split(" ")[0]
        print(HTTP_req)
        if len(msg) == 0:
            connected = False
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            return

        if request == "GET":
            try:
                fileName = HTTP_req.split(" ")[1].strip("/")
                (name, extension) = fileName.split(".")
                sendFileData(sock, fileName, extension)
                # (v) Create an HTTP response message consisting of the requested file preceded by header lines.
                # (vi) Send the response over the TCP connection to the requesting browser.
            except Exception as err:
                res: bytes
                if str(err) == "ico":
                    res = HTTP_response(HTTP_NO_CONTENT, TXT, 0).encode()
                else:
                    res = HTTP_response(HTTP_NOT_FOUND, TXT, 0).encode()
                print(res)
                sock.sendall(res)
            connected = False
        # (vii) If the requested file is not present on the server, the server should send an HTTP “404 Not Found” message back to the client.
        # (viii) The server should listen in a loop, waiting for the next request from the browser.
        # (ix) The server should be able to handle HTTP 1.1 persistent connections. This means It should be able to handle multiple requests from the same connection. This will carry 1 mark if you manage to implement this
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()


def sendFileData(sock, fileName, extension):

    if extension == "html":
        f = open(fileName, "r", encoding="utf-8")
        res = f.read()
        http = HTTP_response(HTTP_OK, TXT, f.tell()) + res
        f.close()
        sock.send(http.encode())
        print(http)
    elif extension == "png":
        f = open(fileName, "rb")
        res = f.read()
        http = HTTP_response(
            HTTP_OK, PNG, f.tell()
        )  # + f"<img src={hostName}:{serverPort}/{fileName}>"
        sock.send(http.encode())
        sock.send(res)
        f.close()
        print(http)
    elif extension == "ico":
        raise Exception("ico")
    else:
        raise Exception("Incompatible file type")


if __name__ == "__main__":
    main()
