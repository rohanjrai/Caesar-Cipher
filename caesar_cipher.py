# String that stores all lowercase alphabet
letters = "abcdefghijklmnopqrstuvwxyz"
# Store the number of letters in the alphabet
num_letters = len(letters)

# Function that encrypts a message
def encrypt(plaintext, shift):
    # Store the encrypted text
    shifted_message = ""

    for letter in plaintext:
        letter = letter.lower()

        if letter == ' ':
            shifted_message += ' '
        else:
            index = letters.find(letter) # Get letter's position

            if index == -1:
                shifted_message += letter # If it's not a letter, keep it the same
            else:
                new_index = index + shift # Shift the letter by the shift value

                if new_index >= num_letters:
                    new_index -= num_letters # Wrap around if past 'z'

                shifted_message += letters[new_index] # Add the shifted letter

    # Return the encrypted result
    return shifted_message


# Function that decrypts a message
def decrypt(ciphertext, shift):
    # Store the decrypted text
    plaintext = ""

    for letter in ciphertext:
        letter = letter.lower()

        if letter == ' ':
            plaintext += ' '
        else:
            index = letters.find(letter) # Get letter's position

            if index == -1:
                plaintext += letter # If it's not a letter, keep it the same
            else:
                new_index = index - shift

                if new_index < 0:
                    new_index += num_letters # Wrap around if before 'a'

                plaintext += letters[new_index] # Add the shifted letter

    # Return the decrypted result
    return plaintext
