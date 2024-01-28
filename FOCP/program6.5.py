'''Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fifth character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye'''
import random
import string

def random_interval_encryption(message):
    interval = random.randint(2, 20)
    encrypted_chars = [c if c.isalpha() else random.choice(string.ascii_lowercase) for i, c in enumerate(message)]
    encrypted_message = ''.join([c + ' ' if (i + 1) % interval == 0 else c for i, c in enumerate(encrypted_chars)])
    return encrypted_message, interval


original_message = input("Enter a message: ")
encrypted_message, interval_used = random_interval_encryption(original_message)

print("\nOriginal Message:", original_message)
print("Encrypted Message:", encrypted_message)
print("Interval Used:", interval_used)
