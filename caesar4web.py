def alphabet_position(letter):
    the_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # This line and the one below are the letter the loop will traverse.
    the_alphabet2 = 'abcdefghijklmnopqrstuvwxyz'

    if letter.islower():  # Here we check to see if the letter is lowercase, if it is, the next line executes.
        return the_alphabet2.index(letter)

    elif letter.isupper():  # This line will check if it is uppercase, then will execute the line below if it is uppercase.
        return the_alphabet.index(
            letter)  # Here, I implemented the .index() method to check what number position the letter is in


def rotate_character(char, rot):
    symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+ "
    if char.isdigit() == True:
        return char

    for i in char:
        if i in symbol:
            return i

        if char.isupper() == True:
            b = alphabet_position(char)
            nr = (b + rot) % 26 + 97
            return chr(nr).capitalize()
        elif char.isupper() == False:
            c = alphabet_position(char)
            nr2 = (c + rot) % 26 + 97
            return chr(nr2)
        elif char.isdigit() == True:
            return char

def encrypt(text,rot): #This is my caesar function
    the_new_txt = ''
    
    for c in text:
        the_new_txt += rotate_character(c,rot)
        
    return the_new_txt


print(encrypt('hello world!!',13))
    


    









