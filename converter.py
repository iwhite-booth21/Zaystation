# Get the ASCII value of a letter
# ascii value = ord (letter)

def make_me (secret_statement):
    ascii_phrase = []
    new_phrase = ""
    print("original: " + secret_statement)
    for letter in secret_statement:
        if letter.isalpha():
            new_letter = chr(ord(letter)+ 2)
            new_phrase += new_letter
            ascii_phrase.append(ord(new_letter))
        else:
            new_phrase += letter
    return new_phrase, ascii_phrase


secret_statement = input("Give me a secret phrase: ")
if len(secret_statement) > 0:
    new_ascii, new_phrase = make_me(secret_statement)
    print(new_ascii)
    print(new_phrase)



