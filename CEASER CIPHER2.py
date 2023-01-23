def caesar_cipher(text, shift):
    """Decrypts the given text using a Caesar cipher.

    Args:
        text (str): The text to be decrypted.
        shift (int): The number of positions to shift the letters of the alphabet.

    Returns:
        str: The decrypted text.
    """
    # Create a list of all the lowercase and uppercase letters of the Turkish alphabet
    lowercase_letters = list('abcçdefgğhıijklmnoöprsştuüvyz')
    uppercase_letters = list('ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ')

    # Create an empty list to store the decrypted text
    decrypted_text = []

    # Iterate over each character in the text
    for char in text:
        # If the character is a lowercase letter, shift it by the given number of positions
        if char in lowercase_letters:
            index = lowercase_letters.index(char)
            decrypted_text.append(lowercase_letters[(index - shift) % 29])
        # If the character is an uppercase letter, shift it by the given number of positions
        elif char in uppercase_letters:
            index = uppercase_letters.index(char)
            decrypted_text.append(uppercase_letters[(index - shift) % 29])
        # If the character is not a letter, just append it to the decrypted text
        else:
            decrypted_text.append(char)

    # Return the decrypted text as a single string
    return ''.join(decrypted_text)

decrypted_text = caesar_cipher("Rbyp açnvl", 3)
print(decrypted_text)  
