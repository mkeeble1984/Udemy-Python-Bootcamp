"""Program to convert a user entered string into Pig Latin"""

vowels = ['A', 'E', 'I', 'O', 'U']
new_sentence = []
start_of_word = ""
MAIN_WORD = ""
message = input(
    "Please enter a messaage in English to be translated into Pig Latin: ")

message_words = message.split()

for word in message_words:
    char_word = list(word)
    print(char_word)
    for char in char_word:
        if char.isnumeric():
            start_of_word = start_of_word + char
        else:
            MAIN_WORD = MAIN_WORD + char

print(start_of_word)
print(MAIN_WORD)
