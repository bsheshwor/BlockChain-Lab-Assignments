import unittest
from encrypt import *

server_publicKey = load_public_keys(whom="server")
server_privateKey = load_private_keys(whom="server") 
client_publicKey = load_public_keys(whom="client")
client_privateKey = load_private_keys(whom="client")

client_message = "Hi Server. I am a client"
server_message = "Hi Client. I am a Server"


class TestEncryptDecrypt(unittest.TestCase):

    def test_server_send(self):
        message = server_message
        server_ciphertext = encrypt(message, client_publicKey)
        server_ciphertextB64 = base64.b64encode(server_ciphertext)
        with open("server_encrypt1.txt", "wb") as f:
            f.write(server_ciphertextB64)
        test_server_encrypt = open("server_encrypt.txt", "rb").read()
        self.assertEqual(test_server_encrypt, server_ciphertextB64, "Encryption in Server Successful")

    def test_client_receive(self):
        server_ciphertextB64 = open("server_encrypt1.txt","rb").read()
        server_decrypted = decrypt(base64.b64decode(server_ciphertextB64), client_privateKey)
        self.assertEqual(server_decrypted, server_message, "Decryption in Client Successful")

    def test_client_send(self):
        message = client_message
        client_ciphertext = encrypt(message, server_publicKey)
        client_ciphertextB64 = base64.b64encode(client_ciphertext)
        with open("client_encrypt1.txt", "wb") as f:
            f.write(client_ciphertextB64)
        test_client_encrypt = open("client_encrypt.txt", "rb").read()
        self.assertEqual(test_client_encrypt, client_ciphertextB64, "Encryption in Client Successful")
    
    def test_server_receive(self):
        client_ciphertextB64 = open("client_encrypt1.txt","rb").read()
        client_decrypted = decrypt(base64.b64decode(client_ciphertextB64), server_privateKey)
        self.assertEqual(client_decrypted, client_message, "Decryption in Server Successful")

if __name__ == "__main__":
    unittest.main()