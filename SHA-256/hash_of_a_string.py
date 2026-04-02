import hashlib

a = input("Enter a string : ")
hash = hashlib.sha256(a.encode())
l = hash.hexdigest()
print(l)
