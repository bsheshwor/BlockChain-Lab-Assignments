import socket
from encrypt import *

server_publicKey = load_public_keys(whom="server")
server_privateKey = load_private_keys(whom="server")
client_privateKey = load_private_keys(whom="client") 
client_publicKey = load_public_keys(whom="client")

def client_program():
    host = socket.gethostname()
    port = 3000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ") 
    
    while True:
        ciphertext = encrypt(message, server_publicKey)
        ciphertextB64 = base64.b64encode(ciphertext)
        client_socket.send(ciphertextB64)
        ciphertextB64Input = client_socket.recv(1024)
        decrypted = decrypt(base64.b64decode(ciphertextB64Input), client_privateKey)
        print('Received from server: ' + str(decrypted))
        message = ""
        message = input(" -> ")
    client_socket.close()


if __name__ == '__main__':
    client_program()