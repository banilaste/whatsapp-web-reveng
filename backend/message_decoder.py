from Crypto.Cipher import AES
import base64
from whatsapp_binary_reader import whatsappReadBinary
import hmac
import hashlib

key = base64.b64decode(input("private key [JSON.parse(window.localStorage.WASecretBundle).encKey] :"))
#macKey = base64.b64decode(input("private key [JSON.parse(window.localStorage.WASecretBundle).macKey] :")

def HmacSha256(key, sign):
    return hmac.new(key, sign, hashlib.sha256).digest()

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def AESDecrypt(key, ciphertext):						# from https://stackoverflow.com/a/20868265
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

while True:
	message = base64.b64decode(input("message : "))
	message = message[message.index(b',')+1:]
    
	#hmacValidation = HmacSha256(macKey, message[32:])
	#if hmacValidation != message[:32]:
	#	raise ValueError("Hmac mismatch")

	decryptedMessage = AESDecrypt(key, pad(message[32:])) #self.loginInfo["key"]["encKey"]
	try:
		processedData = whatsappReadBinary(decryptedMessage, True)
		with open("../result.txt", "a") as file:
			file.write(str(processedData))
			file.write("\n\n")

		print(processedData)
	except Exception as e:
		print(e)
		
