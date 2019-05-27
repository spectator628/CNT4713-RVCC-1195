#This code has segment used from https://www.geeksforgeeks.org/simple-chat-room-using-python/
# Python program to implement client side of chat room. 

"""This program allows mutliple clients to connect to a server and send messages to each other using client-side scipt
using the concept of sockets and threading """

"""Sockets can be seen as the end points in a communication channel, and established a communication between a server and one 
or more clients"""

"""A thread is a subprocess that runs a set of commands. Everytime a user connects to the server, a seperate thread is created.
The communication of the client and the server occur along individual threads based on socket objects created."""

"""We will require two scripts for this chatroom"""

""""This server can be setup on a local area netwrok by choosing any computer to be a server node, and using that computer’s 
private IP address as the server IP address."""

import socket 
import select 
import sys 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print "Correct usage: script, IP address, port number"
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 
  
while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server] 
  
    """We have two potential options
    1. The user wants to send a message to another user
    2. The server wants to send a message to the participating clients to be siplayed on screen

    Select returns from the sockets_list which reads the input stream."""

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    for socks in read_sockets: 
        if socks == server: 
            message = socks.recv(2048) 
            print message 
        else: 
            message = sys.stdin.readline() 
            server.send(message) 
            sys.stdout.write("<You>") 
            sys.stdout.write(message) 
            sys.stdout.flush() 
server.close() 