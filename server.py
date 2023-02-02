import socket
from encrypt import *

server_publicKey = load_public_keys(whom="server")
server_privateKey = load_private_keys(whom="server") 
client_publicKey = load_public_keys(whom="client")
client_privateKey = load_private_keys(whom="client")

def server_program():
    host = socket.gethostname()
    port = 3000 
    server_socket = socket.socket() 
    server_socket.bind((host, port)) 
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        ciphertextB64Input = conn.recv(1024)
        print(ciphertextB64Input)
        decrypted = decrypt(base64.b64decode(ciphertextB64Input), server_privateKey)
        if not decrypted:
            break
        print("from connected user: " + str(decrypted))
        message = input(' -> ')
        ciphertext = encrypt(message, client_publicKey)
        ciphertextB64 = base64.b64encode(ciphertext)
        conn.send(ciphertextB64)
    conn.close()

if __name__ == '__main__':
    server_program()