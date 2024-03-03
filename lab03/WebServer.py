import sys, socket, random, time, functools, os, threading

# HOST_NAME = 
hostName = "127.0.0.1"
CHUNK_SIZE = 0xfff
decoder = "ascii"
HTTP_OK = "200 OK"
HTTP_NO_CONTENT = "204 No Content"
HTTP_RESPONSE_TOP = "HTTP/1.1"
PNG = "image/png"
TXT = "text/html"
debug = ""
CWD = os.getcwd()

def main():
    
    if (CWD == "/home/k-730/Code/COMP3331"):
        debug = "lab03/"
    print(CWD)
    
    if (len(sys.argv) < 2):
        print("Required Arguments: [port]")
        return 0
    port = int(sys.argv[1])
    # hostName = socket.gethostbyname(socket.gethostname()) # TEST!
    address = (hostName, port)
    #i) Create a connection socket when contacted by a client (browser).
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen()

    #(ii) Receive HTTP requests from this connection. Your server should only process GET requests. You may assume that only GET requests will be received.
    while True:
        (sock, addr) = server.accept()
        thread = threading.Thread(target=handle_client, args=(sock, addr, port))
        thread.start()
        print(f"[Active Connections] {threading.active_count() - 1}")
        



def HTTP_response(code : str, content: str):
    return HTTP_RESPONSE_TOP + " " + code + "\n\r" + f"""Content-Type: {content}\n\rKeep-Alive: timeout=2, max=2\r\n\r\n"""

def handle_client(sock : socket, addr, serverPort :int):
    #(iii) Parse the request to determine the specific file being requested.
    
    connected = True
    while connected:
        msg : bytes = sock.recv(CHUNK_SIZE)
        HTTP_data = msg.decode(decoder).split("\r\n")
        HTTP_req = HTTP_data[0]
        #(iv) Get the requested file from the server's file system.
        request = HTTP_req.split(' ')[0]
        print(HTTP_req)
        if (len(msg) == 0):
            connected = False
            sock.close()
            return
        
        if (request == "GET"):
            try:
                fileName = HTTP_req.split(' ')[1].strip("/")
                (name, extension) = fileName.split(".")
                sendFileData(sock, fileName, extension)   
                #(v) Create an HTTP response message consisting of the requested file preceded by header lines.
                #(vi) Send the response over the TCP connection to the requesting browser.
            except Exception as err:
                print(err)
                res = HTTP_response(HTTP_NO_CONTENT, TXT).encode()
                sock.send(res)
                sock.close()
                connected = False
                return
                            
        #(vii) If the requested file is not present on the server, the server should send an HTTP “404 Not Found” message back to the client.
        #(viii) The server should listen in a loop, waiting for the next request from the browser.
        #(ix) The server should be able to handle HTTP 1.1 persistent connections. This means It should be able to handle multiple requests from the same connection. This will carry 1 mark if you manage to implement this
    sock.close()

def sendFileData(sock, fileName, extension):
    if (extension == "html"):
        f = open(debug + fileName, "r")
        raw_data = HTTP_response(HTTP_OK, TXT) + f.read()
        f.close()
        sock.send(raw_data.encode())
    elif (extension == "png"):
        f = open(debug + fileName, "rb")
        raw_data = HTTP_response(HTTP_OK, PNG) # + f"<img src={hostName}:{serverPort}/{fileName}>"
        sock.send(raw_data.encode())
        sock.send(f.read())
        f.close()
    print(raw_data)
    

if __name__ == "__main__":
    main()