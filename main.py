import re
from caesar_cipher import encrypt, decrypt

def main():
    print("Welcome to the Caesar Cipher!")

    while True:
        print("\nSelect Operation:\na) Encrypt message\nb) Decrypt message\nc) Exit\n")

        # Loop runs until user exits
        while True:
            choice = input("Enter choice: ").strip().lower()
            if choice == 'a':
                print("\nENCRYPTION ACTIVATED.")
                operation(choice) # Run program in encrypt mode
                break
            elif choice == 'b':
                print("\nDECRYPTION ACTIVATED.")
                operation(choice) # Run program in decrypt mode
                break
            elif choice == 'c': 
                break # Exit the loop and end the program
            else: 
                print("Enter a valid choice.")

        if choice == 'c':
            print("\n\nYou have successfully exited the program!")
            break # Exit the main loop
        else:
            continue # Restart main loop


def operation(mode):
    # Loop until user enters valid message
    while True:
        message = str(input("Enter message: "))
        if re.match("^[A-Za-z ]*$", message): # Check if the input contains only letters and spaces
            break
        else:
            print("Enter letters and spaces only.")

    # Loop until user enters valid integer shift value
    while True:
        try:
            shift =  int(input("Enter the number to shift the message by: "))
            break
        except ValueError:
            print("Enter a valid number.")

    # Perform the operation based on the mode
    if mode == 'a':
        print(f"\nEncrypted message: {encrypt(message, shift)}") 
    elif mode == 'b':
        print(f"\nDecrypted message: {decrypt(message, shift)}")
    else:
        print("Error: Invalid operation selected.")


# Entry point of the program
if __name__ == "__main__":
    main()
