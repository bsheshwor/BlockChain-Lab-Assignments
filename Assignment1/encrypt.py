import rsa
import base64

def load_public_keys(whom=None):
    with open(whom+"_public_keys/"+whom+"_public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    return public_key

def load_private_keys(whom=None):
    with open(whom+"_private_keys/"+whom+"_private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key

def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False
    
def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False