from hashlib import sha1

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