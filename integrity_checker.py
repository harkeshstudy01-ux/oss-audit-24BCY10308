import hashlib
import json

FILE = "hashes.json"

def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None

def store(path):
    data = load()
    h = get_hash(path)
    if h:
        data[path] = h
        save(data)
        return True
    return False

def verify(path):
    data = load()
    h = get_hash(path)

    if path in data:
        return "SAFE" if data[path] == h else "MODIFIED!"
    return "No record"