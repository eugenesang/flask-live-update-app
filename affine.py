import random

def generate_coprimes(n):
    """Generate a list of coprimes of n."""
    coprimes = []
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def affine_encrypt(message):
    """Encrypt message using the Affine cipher."""
    n = 52  # number of letters in the alphabet (both capital and small)
    coprimes = generate_coprimes(n)
    a = random.choice(coprimes)
    b = random.randint(1, n - 1)

    encrypted_numbers = []
    for char in message:
        if char.isalpha():
            if char.isupper():
                x = ord(char) - ord('A')
            else:
                x = ord(char) - ord('a') + 26
            y = (a * x + b) % n
            encrypted_numbers.append(y)
        else:
            encrypted_numbers.append(char)

    return encrypted_numbers, (a, b)

def mod_inverse(a, n):
    """Compute the modular multiplicative inverse of a modulo n."""
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return 1

def affine_decrypt(encrypted_numbers, coprime_pair):
    """Decrypt the encrypted numbers using the Affine cipher."""
    a, b = coprime_pair
    n = 52  # number of letters in the alphabet (both capital and small)
    a_inv = mod_inverse(a, n)

    decrypted_message = ''
    for y in encrypted_numbers:
        if isinstance(y, int):
            x = (a_inv * (y - b)) % n
            if x < 26:
                decrypted_message += chr(x + ord('A'))
            else:
                decrypted_message += chr(x - 26 + ord('a'))
        else:
            decrypted_message += y

    return decrypted_message

# Example usage:
message = "Hello, World!"
encrypted_numbers, coprime_pair = affine_encrypt(message)
print("Encrypted numbers:", encrypted_numbers)
print("Co-prime pair:", coprime_pair)

decrypted_message = affine_decrypt(encrypted_numbers, coprime_pair)
print("Decrypted message:", decrypted_message)