import sys, socket, random, time

UPPER = 60_000;
LOWER = 50_000;
PING_TIMES = 20;
TIMEOUT = 600; # Timeout in ms
BUFFER_SIZE = 0xff;

def main():
    print(sys.argv);

    # Get and check arguments
    if (len(sys.argv) < 3):
        print("Required Arguments: [host IP] [port]")
        return 0
    hostIP = sys.argv[1];
    port = int(sys.argv[2]);
    address = (hostIP, port);

    #Choose random starting integer between LOWER and UPPER
    start = (UPPER - LOWER) * random.random() + LOWER;

    # Create a new socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    client.connect(address);
    # Begin to send packets
    tripTimeData = [];

    # for i in range(start, start + PING_TIMES, 1):
    message = Message(sequence=start, timeNow=time.time());
    client.sendto(message.toBytes(), address);



    client.close();

class Message:
    __sequence = 0;
    __timeStamp = 0;
    __keyword = "PING"

    def __init__(self ,sequence : int, timeNow : float):
        self.sequence = sequence;
        self.__timeStamp = int(timeNow);
    
    def toBytes(self):
        tmp = self.__keyword + ' ' + str(self.__sequence) + ' ' + str(self.__timeStamp)
        byte_array = bytearray(tmp, 'ascii')
        return byte_array


    def getTime(self):
        return self.__timeStamp;





if __name__ == "__main__":
    main();

