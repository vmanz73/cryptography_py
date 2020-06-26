import hashlib 

tes = "GeeksforGeeks"
tes = bytes(tes, 'utf-8')
result = hashlib.md5(tes) 

# printing the equivalent byte value. 
print("The byte equivalent of hash is : ", end ="") 
print(str(result.hexdigest()))