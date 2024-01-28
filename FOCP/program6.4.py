'''Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.'''
def simple_encryption(message):
    return message.replace(" ", "")[::-1]

# Test the function
original_message = input("Enter a message: ")
encrypted_message = simple_encryption(original_message)
print("\nOriginal Message:", original_message)
print("Encrypted Message:", encrypted_message)

