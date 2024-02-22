import java.nio.ByteBuffer;
import java.util.Date;

// Message payload

public class Message {
    private String keyword = "PING";
    private Integer sequence = -1;

    private Long timeStamp = null; // Sending time

    public Message(Integer sequence, Date date) {
        this.sequence = sequence;
        this.timeStamp = date.getTime();
    }

    // Convert message to byte array
    public byte[] toBytes() {
        // Format the message as required by the lab
        // <PING> <sequence_number> <time> <CRLF>
        ByteBuffer b = ByteBuffer.allocate(PingClient.BUFFER_SIZE);
        b.put(keyword.getBytes());
        b.put(" ".getBytes());
        b.put(this.sequence.toString().getBytes());
        b.put(" ".getBytes());
        b.put(timeStamp.toString().getBytes());
        b.put("\r\n".getBytes());
        return b.array();
    }

    public Long getSendTime() {
        return timeStamp;
    }

    public Integer getSequence() {
        return sequence;
    }

}