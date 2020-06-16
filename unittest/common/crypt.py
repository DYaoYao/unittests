from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from rsa import transform
from rsa import core
from rsa import PublicKey
import base64
import hashlib

aes_key_length = 16


def md5(md5_str):
    return hashlib.md5(md5_str.encode()).hexdigest()


class AESCrypt:
    @staticmethod
    def encrypt(aes_key, aes_str):
        aes = AES.new(aes_key.encode(), AES.MODE_ECB)
        aes_pad = pad(aes_str.encode(), AES.block_size)
        encrypt_aes = aes.encrypt(aes_pad)
        encrypted_byte = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
        encrypted_str = encrypted_byte.replace('\n', '')
        return encrypted_str

    @staticmethod
    def decrypt(aes_key, aes_str):
        aes_base64 = base64.decodebytes(aes_str.encode())
        aes = AES.new(aes_key, AES.MODE_ECB)
        decrypt_base64 = aes.decrypt(aes_base64)
        return unpad(decrypt_base64, AES.block_size).decode()


class RSACrypt:
    @staticmethod
    def load_pubkey_from_str(str_key):
        """
        str likes below, prefix and suffix are needed.
        -----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEYkKp8k9wTzGMMBUrPfeMiS9R
        VBso8N8aC5hb0mJzm648kQLLJRA/wyiDu4AKSSIMsOOgtJD90ucvb5nDrQDI6+S3
        KDqkb9C1+36twe/kUcFtrTiiRPIL0ngWAOX5uXhJRZ4fvtzyOL03oOMXroxrUmR0
        +/nIst9tUud7+tbZ6QIDAQAB
        -----END PUBLIC KEY-----
        """
        return PublicKey.load_pkcs1_openssl_pem(str_key.encode())

    @staticmethod
    def encrypt(rsa_key, rsa_str):
        rsa_bytes = rsa_str.encode()
        key_str = RSA.importKey(rsa_key)
        cipher = PKCS1_v1_5.new(key_str)
        cipher_text = base64.b64encode(cipher.encrypt(rsa_bytes))
        return cipher_text.decode()

    @staticmethod
    def decrypt(rsa_key, rsa_str):
        rsa_bytes = base64.decodebytes(rsa_str.encode())
        rsa_key = PublicKey.load_pkcs1_openssl_pem(rsa_key.encode())
        num = transform.bytes2int(rsa_bytes)
        decry = core.decrypt_int(num, rsa_key.e, rsa_key.n)
        out = transform.int2bytes(decry)
        sep_idx = out.index(b"\x00", 2)
        out = out[sep_idx + 1:]
        return out
