import hashlib

md5 = hashlib.md5()
md5.update('python'.encode('utf-8'))
print(md5.hexdigest())  