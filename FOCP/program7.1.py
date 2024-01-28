'''Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].'''
def unique_letters(string):
    return sorted(set(char.lower() for char in string if char.isalpha()))

# Test the function
test_string = "cheese"
result = unique_letters(test_string)
print("Original String:", test_string)
print("Unique Letters:", result)
