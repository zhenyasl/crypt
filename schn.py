import hashlib
import random

# Generate a random private key (usually a large prime number)
private_key = random.randint(2, 2**256)

# Generate a public key based on the private key
def generate_public_key(private_key):
    return pow(2, private_key, p)

# Define the prime number p and generator g (p should be a safe prime)
p = 2**256 - 2**32 - 977
g = 2

# Generate a random nonce (k)
def generate_nonce():
    return random.randint(1, p - 1)

# Generate the Schnorr signature
def generate_signature(message, private_key):
    k = generate_nonce()
    R = pow(g, k, p)

    e = hashlib.sha256(message.encode()).hexdigest()
    e = int(e, 16)

    s = (k - private_key * e) % (p - 1)

    return (R, s)

# Verify
def verify_signature(message, signature, public_key):
    R, s = signature

    e = hashlib.sha256(message.encode()).hexdigest()
    e = int(e, 16)

    v1 = pow(g, s, p)
    v2 = pow(public_key, e, p)
    v = (v1 * v2) % p

    return v == R

# Test
message = "Hello, world!"
public_key = generate_public_key(private_key)
signature = generate_signature(message, private_key)
valid = verify_signature(message, signature, public_key)

print("Message:", message)
print("Public key:", public_key)
print("Signature:", signature)
print("Signature valid?", valid)