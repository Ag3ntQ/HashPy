import hashlib as h
import base64
import os
import time
from shutil import which

G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    #Red

pr= which("figlet")
print(pr)
if pr== None:
	print(f'{R} [~] figlet is not Installed!{W}')
	time.sleep(2)
	os.system("pkg install figlet")
	os.system("clear")
else:
	pass



def hash():
 os.system("figlet Hash.py")
 print(30*"=")
 t=input("[+] Type   : ")
 s=input("[+] String : ")
 st=input("[+] Salt   : ")
 print(30*"=")
 if t=="md5":
  v=h.md5((st+s).encode()).hexdigest()
  print(f"[~] MD5 : {v}")
 elif t=="md4":
   v=h.new('md4',(s+st).encode("utf-8")).hexdigest()
   print(f"[~] md4 : {v}")
 elif t=="sha1":
  v=h.sha1((st+s).encode()).hexdigest()
  print(f"[~] SHA1 : {v}")
 elif t=="sha224":
  v=h.sha224((st+s).encode()).hexdigest()
  print(f"[~] SHA224 : {v}")
 elif t=="sha256":
  v=h.sha256((st+s).encode()).hexdigest()
  print(f"[~] Sha256 : {v}")
 elif t=="sha384":
  v=h.sha384((st+s).encode()).hexdigest()
  print(f"[~] Sha384 : {v}")
 elif t=="sha512":
  v=h.sha512((st+s).encode()).hexdigest()
  print(f"[~] Sha512 : {v}")
 elif t=="base64":
  msg_byte=s.encode("ascii")
  base_byte=base64.b64encode(msg_byte)
  base_str=base_byte.decode("ascii")
  print(f"[~] Base64 : {base_str}")
 else:
  print("[ !! ] Invalid Type")
  print('[md4] [md5] [sha1] [sha224] [sha256] [sha384] [sha512] [base64]')
 

hash()