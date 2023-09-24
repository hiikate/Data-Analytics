import random

# Function to generate a random encryption string
def generate_random_encryption_string():
    encryption_string = "abcdefghijklmnopqrstuvwxyz"
    encryption_list = list(encryption_string)
    random.shuffle(encryption_list)
    return ''.join(encryption_list)

# Function to encrypt the input text
def encrypt_text(input_text):
    encryption_string = generate_random_encryption_string()
    encrypted_text = ""
    
    for char in input_text:
        if char.islower():
            index = ord(char) - ord('a')
            if 0 <= index < 26:
                encrypted_char = encryption_string[index]
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        else:
            encrypted_text += char

    return input_text, encrypted_text, encryption_string

# Main program
if __name__ == "__main__":
    input_text = input("Enter the text to encrypt: ").lower()  # Convert input to lowercase
    original_text, encrypted_text, encryption_string = encrypt_text(input_text)
    
    print(f"Original Text: {original_text}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Encryption String: {encryption_string}")
