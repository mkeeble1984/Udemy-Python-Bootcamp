alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number:\n"))


def encrypt(p_message, p_shift_num):
    new_message = ""
    for i in p_message:
        if i in alphabet:
            new_char_pos = (alphabet.index(i) + p_shift_num) % len(alphabet)
            new_message += alphabet[new_char_pos]
        else:
            new_message = new_message + i
    return new_message


new_message = encrypt(message, shift_number)
print(f"The encoded message is: {new_message}")
