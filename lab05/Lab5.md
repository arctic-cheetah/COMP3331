# Lab05

## Exercise 1

![TCP window size](./img/lab5-q1.png)

### 1.1a) In this case, what is the maximum size of the congestion window that the TCP flow reaches?

The maximum congestion window size that is reached is 100 at 2.08secs.

### 1.1b) What does the TCP flow do when the congestion window reaches this value? Why?

~~The TCP flow will continue to use _slow-start_ as it has not reached the slow start threshold (ssthresh)~~

The congestion window (cwind) will fall to 1, and the slow start threshold (ssthresh) will be half of 100 (This is from the congestion window and so ssthresh is 50) according to TCP tahoe.

This will occur because the sender has encountered a timeout or a triple ACK, which indicates that the receiver has a full queue because of the sender's increased window size

### 1.1c) What happens next?

The sender will be in the _slow-start_ stage to increase window size up to ssthresh. Since ssthresh is now 50, after cwind reaches ssthresh, it will begin to use _additive increase_ algorithm the increase the cwind size by 1 until it receives a timeout or triple-ack (because of a full queue from the receiver). Then cwind will drop back to 1 and the cycle continues

### 1.2)From the simulation script we used, we know that the packet's payload is 500 Bytes. Keep in mind that the size of the IP and TCP headers is 20 Bytes each. Neglect any other headers. What is the average throughput of TCP in this case? (both in number of packets per second and bps)

![TCP window size](./img/lab5-q1-2.png)

As seen in the graph above, the average throughput for TCP stabilises around 193 packets/second after 35s.
The total packet size is (500 + 20 + 20)

and so the bytes / second is: 540 *193 = 104,220 bytes / second

Thus the bits / second is = 8* 104,220 bytes / s = 833,760 bits/s = 833.76kbps

## Exercise 2

![Q2](./img/lab5-q2.png)
TODO:

### 2.1) Why is the throughput achieved by flow tcp2 higher than tcp1 between 6 sec to 8 sec?

The reason is because tcp1 and tcp2 compete over bandwith the link and that tcp1 has a higher RTT (200ms) than tcp2(120ms).
Specifically, tcp1 and tcp2 will compete over bandwith on link n2-n4.
and tcp1 will also compete with tcp4 for link bandiwth over n1-n2.
Since tcp2 has a lower RTT than tcp1, this means tcp2 will eventually have a greater flow than tcp1

### 2.2) Why does the throughput for flow tcp1 fluctuate between a time span of 0.5 sec to 2 sec?

The throughput fluctuates because tcp1 is in the slow start stage.
