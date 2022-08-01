"""Task 1. There is string s = "Python Bootcamp". Write the code that hashes string."""
import hashlib


def string_to_hash(s="Python Bootcamp"):
    """function that hashes string"""
    sha = hashlib.sha256(s.encode('utf-8'))
    return sha.hexdigest()


print(string_to_hash())
