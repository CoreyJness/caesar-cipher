# add your code here
#alphabet soup
alphabet = "abcdefghijklmnopqrstuvwxyz"

#ceasar cipher function
def caesar_cipher(message, character_shift):
        global alphabet
        encrypted_message = ""
        if character_shift > 25:
            print("Please enter a number between 1 and 25")
            return
        
        if message == "":
            print("Please enter a message")
            return
        
        for char in message:
            if char in alphabet:
                char_index = alphabet.find(char)
                encrypted_char = alphabet[(char_index + character_shift) % 26]
                encrypted_message += encrypted_char
                if char_index + character_shift > 25:
                    encrypted_char = alphabet[(char_index + character_shift) % 26]

        print("The original message : ", message, " has been encrypted to : ", encrypted_message) 

character_shift = int(input("How many characters would you like to shift the letters between 1 and 25?"))
message = input("Please enter your message:").lower()
caesar_cipher(message, character_shift)