## Summary

Server and client via Python `socket` library.  
Client generates its id and sends it to the server (port 8000). Server responds with the key. After that client
sends its id, key and random message to server (port 8001). If id: key pair is in clients database `db_clients`:
time, client id and random message will be logged in **serverlog.log** file. Else time,
client id and "ACCESS DENIED!" message will be logged in the same file.
