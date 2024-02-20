# Lab02

## Exercise 3

### Q1)

The server returns a 200 status code to the client.

![img](./lab02-q3-a.png)

### Q2)

----------------------------

When was the HTML file the browser retrieves last modified at the server? Does the response also contain a DATE header? How are these two fields different?
----------------------------

The HTML file was last modified on Tue, 23 Sep 2003 05:29:00 GMT.

The response also contains a date header.

The _'date'_ header represents the time when the message was sent. This is contrasted by _'last modified'_ which tells the user when the file lab2-1.html was last changed at the server.

### Q3)

Is the connection established between the browser and the server persistent or non-persistent? How can you infer this?

The connection between the browser and server is persistent. We can conclude this because the _'Connection'_ header is _'Keep Alive'_ and represents the persistency of a connection. Additionally, the HTTP version used is `HTTP/1.1` and this version assumes all connections are persistent unless specified.
