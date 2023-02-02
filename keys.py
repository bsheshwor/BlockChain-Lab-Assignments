import rsa
import base64

def generateKeys(whom=None):
    public_key, private_key = rsa.newkeys(1024)

    with open(whom+"_public_keys/"+whom+"_public.pem","wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open(whom+"_private_keys/"+whom+"_private.pem","wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

generateKeys(whom="server")
generateKeys(whom="client")