import java.nio.ByteBuffer;
import java.util.Date;

// Message payload

public class Message {
    public String keyword = "PING";
    public Integer sequence = -1;
    public Long timeStamp = null;

    public Message(Integer sequence, Date date) {
        this.sequence = sequence;
        this.timeStamp = date.getTime();
    }

    // Convert message to byte array
    public byte[] toBytes() {
        ByteBuffer b = ByteBuffer.allocate(PingClient.BUFFER_SIZE);
        b.put(keyword.getBytes());
        b.putInt(this.sequence);
        b.putLong(timeStamp);
        return b.array();
    }
}