import unittest
from encrypt import *

server_publicKey = load_public_keys(whom="server")
server_privateKey = load_private_keys(whom="server") 
client_publicKey = load_public_keys(whom="client")
client_privateKey = load_private_keys(whom="client")

client_message = "Hi Server. I am a client"
server_message = "Hi Client. I am a Server"


class TestEncryptDecrypt(unittest.TestCase):

    def test_server2client_send(self):
        message = server_message
        server_ciphertext = encrypt(message, client_publicKey)
        server_ciphertextB64 = base64.b64encode(server_ciphertext)
        server_decrypted = decrypt(base64.b64decode(server_ciphertextB64), client_privateKey)
        self.assertEqual(server_decrypted, server_message, "Decryption in Client Successful")
    
    def test_client2server_send(self):
        message = client_message
        client_ciphertext = encrypt(message, server_publicKey)
        client_ciphertextB64 = base64.b64encode(client_ciphertext)
        client_decrypted = decrypt(base64.b64decode(client_ciphertextB64), server_privateKey)
        self.assertEqual(client_decrypted, client_message, "Decryption in Server Successful")

if __name__ == "__main__":
    unittest.main()