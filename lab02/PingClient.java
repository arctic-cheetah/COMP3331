import java.io.IOException;
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
            return;
        }

        // Check valid arguments.
        // TODO : Perform error Checking
        InetAddress serverIP = InetAddress.getByName(args[0]);
        int serverPort = Integer.parseInt(args[1]);

        // Create random number between UPPER AND LOWER
        Random random = new Random();

        // Starting number
        Integer diff = (int) (random.nextDouble() * (UPPER - LOWER));
        Integer start = diff + LOWER;

        // Setup socket to rx and tx UDP packets via serverIP and packet.
        // DatagramSocket socket = new DatagramSocket(port, serverIP);
        DatagramSocket socket = sendPackets(serverIP, serverPort, start);
        socket.close();
    }

    private static DatagramSocket sendPackets(InetAddress serverIP, int serverPort, Integer start)
            throws SocketException, IOException {
        DatagramSocket socket = new DatagramSocket();
        ArrayList<Long> tripTimeData = new ArrayList<>();

        socket.setSoTimeout(TIMEOUT);

        // Wrap the socket around the thread to enable timeout
        synchronized (socket) {
            // Send 20 UDP packets
            for (int i = 0; i < PING_TIMES; i += 1) {
                // Send a UDP packet
                Message message = new Message(start, new Date());
                DatagramPacket txPacket = new DatagramPacket(message.toBytes(), BUFFER_SIZE, serverIP, serverPort);
                socket.send(txPacket);

                // Wait for reply. Timeout is 600ms
                DatagramPacket rxPacket = new DatagramPacket(new byte[BUFFER_SIZE], BUFFER_SIZE);
                try {
                    socket.receive(rxPacket);
                    long rtt = calculateRTT(tripTimeData, message);

                    // print as shown: ping to 127.0.0.1, seq = 50215, rtt = 120 ms
                    System.out.println("ping to " + txPacket.getAddress().getHostAddress() + ", seq = "
                            + message.getSequence() + ", rtt = " + rtt);
                } catch (Exception e) {
                    // System.out.println(e);
                    System.out.println("ping to " + txPacket.getAddress().getHostAddress() + ", seq = "
                            + message.getSequence() + ", rtt = timeout");
                    continue;
                } finally {
                    start += 1;
                }
            }
        }
        // Calculate Packet RTT min, max, avg
        RTTStats(tripTimeData);
        return socket;
    }

    private static long calculateRTT(ArrayList<Long> tripTimeData, Message message) {
        long rxTime = (new Date()).getTime();
        long rtt = rxTime - message.getSendTime();
        tripTimeData.add(rtt);
        return rtt;
    }

    private static void RTTStats(ArrayList<Long> tripTimeData) {
        Integer tripTimeSum = tripTimeData.stream().map(e -> e.intValue()).reduce(Integer::sum).orElse(-1);
        Double averageTime = (double) tripTimeSum / tripTimeData.size();
        // int tmpMin = tripTimeData.stream().mapToInt(Long::intValue).min().orElse(-1);

        Integer minTime = tripTimeData.stream().map(e -> e.intValue()).min(Integer::compare).orElse(0);
        Integer maxTime = tripTimeData.stream().map(e -> e.intValue()).max(Integer::compare).orElse(0);
        System.out.print("minimum = " + minTime + " , ");
        System.out.print("maximum = " + maxTime + " , ");
        System.out.println("average = " + averageTime);
    }
}
