# helpers/security_helpers.py
"""
Security helpers
"""
import hashlib

def hash_password(password: str):
    """Return SHA256 hex digest of password"""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()
