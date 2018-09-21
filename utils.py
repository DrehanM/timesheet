from hashlib import sha1, sha256

def hash_it(*args):
    hasher = sha1()
    for arg in args:
        hasher.update(arg)
    
    return int(hasher.hexdigest(), 16)

def hash_login(username, password):
    hasher = sha1()
    
    hasher.update(bytes(username, encoding="utf-8"))
    hasher.update(bytes(password, encoding="utf-8"))

    hash_id = int(float('%f' % (int(hasher.hexdigest(), 16) % 1e18)))

    return hash_id

def hash256_it(*args):
    hasher = sha256()
    for arg in args:
        hasher.update(arg)
    
    return hasher.hexdigest()

def hash256_login(username, password):
    hasher = sha256()
    
    hasher.update(bytes(username, encoding="utf-8"))
    hasher.update(bytes(password, encoding="utf-8"))

    hash_id = hasher.hexdigest()

    return str(hash_id)
