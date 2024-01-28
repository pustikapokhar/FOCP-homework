'''Write a program that decrypts messages encoded as above.'''
import random
import string

def random_interval_encryption(message):
    interval = random.randint(2, 20)
    encrypted_message = ''.join([c + ' ' if (i + 1) % interval == 0 and c.isalpha() else c for i, c in enumerate(message)])
    return encrypted_message, interval

def random_interval_decryption(encrypted_message, interval):
    decrypted_message = ''.join([c for c in encrypted_message if c.isalpha()])
    return decrypted_message

# Get user input for the original message
original_message = input("Enter a message: ")

# Encrypt and decrypt the message
encrypted_message, interval_used = random_interval_encryption(original_message)
decrypted_message = random_interval_decryption(encrypted_message, interval_used)

# Display the results
print("\nOriginal Message:", original_message)
print("Encrypted Message:", encrypted_message)
print("Interval Used:", interval_used)
print("Decrypted Message:", decrypted_message)

