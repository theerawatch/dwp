import hashlib
import os
hash_algorithm = hashlib.sha256
salt = os.getenv('HASH_SALT')

def ComparePassword(password: str, store_password: str) -> bool:
    hashed_password = hash_algorithm((password+salt).encode('utf-8')).hexdigest()
    if hashed_password == store_password:
        return True
    return False 
    
def GeneratePassword(password: str) -> str:
    return hash_algorithm((password + salt).encode('utf-8')).hexdigest()