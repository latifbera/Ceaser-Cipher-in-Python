def caesar_cipher(text, shift):
    """Encrypts the given text using a Caesar cipher.

    Args:
        text (str): The text to be encrypted.
        shift (int): The number of positions to shift the letters of the alphabet.

    Returns:
        str: The encrypted text.
    """
    # Create a list of all the lowercase and uppercase letters of the Turkish alphabet
    lowercase_letters = list('abcçdefgğhıijklmnoöprsştuüvyz')
    uppercase_letters = list('ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ')

    # Create an empty list to store the encrypted text
    encrypted_text = []

    # Iterate over each character in the text
    for char in text:
        # If the character is a lowercase letter, shift it by the given number of positions
        if char in lowercase_letters:
            index = lowercase_letters.index(char)
            encrypted_text.append(lowercase_letters[(index + shift) % 29])
        # If the character is an uppercase letter, shift it by the given number of positions
        elif char in uppercase_letters:
            index = uppercase_letters.index(char)
            encrypted_text.append(uppercase_letters[(index + shift) % 29])
        # If the character is not a letter, just append it to the encrypted text
        else:
            encrypted_text.append(char)

    # Return the encrypted text as a single string
    return ''.join(encrypted_text)

encrypted_text = caesar_cipher("öckğ alı öctğulosj zvkgj vkkczğeğj", 3)
print(encrypted_text)  


