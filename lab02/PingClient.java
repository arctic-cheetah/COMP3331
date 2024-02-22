import java.net.*;
import java.util.*;

public class PingClient {
    private static final int LOWER = 50_000;
    private static final int UPPER = 60_000;
    private static final int PING_TIMES = 20;
    private static final int TIMEOUT = 600; // Timeout in ms

    public static final int BUFFER_SIZE = 0xff;

    public static void main(String[] args) throws Exception {
        // Get arguments
        if (args.length < 2) {
            System.out.println("Required Arguments: [host IP] [port]");
        }

        // Check valid arguments.
        // TODO : Perform error Checking
        InetAddress hostIP = InetAddress.getByName(args[0]);
        int port = Integer.parseInt(args[1]);

        // Create random number between UPPER AND LOWER
        Random random = new Random();

        // Starting number
        Integer diff = (int) (random.nextDouble() * (UPPER - LOWER));
        Integer start = diff + LOWER;

        // Setup socket to rx and tx UDP packets via hostIP and packet.
        DatagramSocket socket = new DatagramSocket(port, hostIP);
        socket.setSoTimeout(TIMEOUT);

        // Send 20 UDP packets
        for (int i = 0; i < 1; i += 1) {
            Message message = new Message(start, new Date());
            DatagramPacket txPacket = new DatagramPacket(message.toBytes(), BUFFER_SIZE, hostIP, port);
            socket.send(txPacket);

            // Wait for reply. Timeout is 600ms
            socket.wait();
            DatagramPacket rxPacket = new DatagramPacket(new byte[BUFFER_SIZE], BUFFER_SIZE);
            socket.receive(rxPacket);

        }
        socket.close();
    }
}
