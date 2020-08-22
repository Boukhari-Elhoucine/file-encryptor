from Crypto.Cipher import AES
import os

target_ext = ["encrypted"]
def read_key():
    with open("key.pem","rb") as reader:
        key = reader.read()
    return key

def decryption(key,target):
    with open(target,"rb") as dec:
        IV = dec.read(16)
        D = AES.new(key,AES.MODE_OFB,IV)
        if target.endswith(".encrypted"):
            new_file = target[:-10]
        with open(new_file,"wb") as writer:
            writer.write(D.decrypt(dec.read()))

def main():
    key = read_key()
    for root, _, files in os.walk("."):
        for f in files:
            file_path = os.path.join(root,f)
            if file_path.split(".")[-1] in target_ext:
                decryption(key,file_path)

main()

