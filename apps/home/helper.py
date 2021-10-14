from base64 import b64encode, b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from core.settings import SECRET_KEY

def encrypt(data, iv):
    key = SECRET_KEY.encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return b64encode(ct_bytes)

def decrypt(ciphertext, iv):
    ciphertext = b64decode(ciphertext)
    iv = b64decode(iv)
    key = SECRET_KEY.encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt.decode()