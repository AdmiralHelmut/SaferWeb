from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
import requests
from logEncrypter import LogEncrypter


logEncrypter1 = LogEncrypter()
logEncrypter1.encrypted_logging("TestLog")
