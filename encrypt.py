import binascii
import base64

def hexToBase64(s):
    decoded = binascii.unhexlify(s)
    return base64.b64encode(decoded).decode('ascii')

def encrypt(msg):
    return [ord(c) for c in msg]




print(encrypt(f'apply.joincoded.com/jadodjosdkncjsod'))