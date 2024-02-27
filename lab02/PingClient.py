import sys, socket, random, time, functools;

UPPER = 60_000;
LOWER = 50_000;
PING_TIMES = 20;
TIMEOUT = 600 / 1E3; # Timeout in ms
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
    start = int((UPPER - LOWER) * random.random() + LOWER);

    # Create a new socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    client.connect(address);
    client.settimeout(TIMEOUT);

    # Set Timeout

    # Begin to send packets
    tripTimeData = [];

    for i in range(start, start + PING_TIMES, 1):
        message = Message(sequence=i, timeNow=time.time());
        client.sendto(message.toBytes(), address);
        try:
            data = client.recv(BUFFER_SIZE);
            data = data.decode("utf8");
            # Need to remove padding here with replace because python 
            # is retarded and doesn't replace for you when converting to float unlike other languages
            timeSent = float(data.split(' ')[2].replace("\x00", ""));
            rtt = float(time.time() - timeSent);
            tripTimeData.append(rtt);
            print(f"ping to {hostIP}, seq = {i}, rtt(ms) = {rtt * 1E3}");
        except Exception as error:
            print(error)
            print(f"Waited for 600ms, too long! packet #{i} lost!");
            continue;
        
    # calculate RTT stats
    avgLambda = lambda a,b: a+b; 
    avg = functools.reduce(avgLambda, tripTimeData) / len(tripTimeData) * 1E3;
    maxVal = max(tripTimeData) * 1E3;
    minVal = min(tripTimeData) * 1E3;

    print(f"minimum = {minVal} \nmaximmum = {maxVal} \naverage = {avg}");

    client.close();

class Message:
    __keyword = "PING"
    __sequence = 0;
    __timeStamp = 0;

    def __init__(self ,sequence : int, timeNow : float):
        self.__sequence = sequence;
        self.__timeStamp = float(timeNow);
    
    def toBytes(self):
        tmp = self.__keyword + ' ' + str(self.__sequence) + ' ' + str(self.__timeStamp)
        byte_array = bytearray(tmp, 'ascii')
        return byte_array


    def getTime(self):
        return self.__timeStamp;





if __name__ == "__main__":
    main();

