def find_first_repeating_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            print(f"First repeating character: '{char}' at memory address: {id(char)}")
            return char, id(char)
        else:
            char_count[char] = 1
    return None

# Example usage:
result = find_first_repeating_character("hello world")
if result:
    character, address = result
    print(f"The character '{character}' repeats first and is located at memory address {address}.")
else:
    print("No repeating characters found.")

