# DS_Tic_Tac_Toe
Client-Server Tic_Tac_Toe

This is a simple Tic tac toe game develped using Python. Through the server is first start to enable the clients to coonnect. once two players are connected the server send a copy of the game object to the connected clients.

Client - Server architecture is used for this project using TCP , and I used port 7228. messages were sent back and forth between the server and the clients, pickle module was used to convert the game object into a byte stream to be sent to the clients.
