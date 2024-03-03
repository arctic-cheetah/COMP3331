
import java.io.*;
import java.net.*;
import java.util.*;

public class WebServer {
    // Change host ip address here
    private static String hostName = "127.0.0.1";

    public static void main(String[] args) throws Exception {

        if (args.length < 1) {
            System.out.println("Required arguments: [port]");
            return;
        }
        int port = Integer.parseInt(args[0]);

        ServerSocket server = new ServerSocket(port);
        // Create a connection socket when contacted by a client (browser).
        while (true) {
            Socket client = server.accept();
            InputStream i = client.getInputStream();
            BufferedReader input = new BufferedReader(new InputStreamReader(i));
            String s = input.readLine();
            // Get the HTTP codes.
            // Only process GET requests
            // (iii) Parse the request to determine the specific file being requested.
            String[] req = s.split(" ");

            if (req[0].equals("GET")) {
                // (iv) Get the requested file from the server's file system.
                String filePath = "." + req[1];
                System.out.println(filePath);

                FileOutputStream inputStream = new FileOutputStream(filePath);
                inputStream.close();
            }

            // (v) Create an HTTP response message consisting of the requested file preceded
            // by header lines.
            // (vi) Send the response over the TCP connection to the requesting browser.
            // (vii) If the requested file is not present on the server, the server should
            // send an HTTP “404 Not Found” message back to the client.
            // (viii) The server should listen in a loop, waiting for the next request from
            // the browser.

        }

    }
}