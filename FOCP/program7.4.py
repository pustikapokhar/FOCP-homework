'''One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes.'''
def frequency_analysis(message):
    # Initialize an empty dictionary to store letter frequencies
    letter_counts = {}

    # Process the message and count letter frequencies
    for char in message.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    # Sort the letter frequencies by count in descending order
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    # Display the six most common letters and their counts
    print("Six most common letters and their counts:")
    for letter, count in sorted_letter_counts[:6]:
        print(f"{letter}: {count}")

# Test the function
encrypted_message = "Helloworld! This is an example of an encrypted message."
frequency_analysis(encrypted_message)
