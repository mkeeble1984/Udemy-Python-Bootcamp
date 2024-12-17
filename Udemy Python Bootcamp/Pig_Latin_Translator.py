"""Program to convert a user entered string into Pig Latin"""

vowels = ['A', 'E', 'I', 'O', 'U']
new_sentence = []
start_of_word = ""
message = input(
    "Please enter a messaage in English to be translated into Pig Latin: ")

message_words = message.split()

for word in message_words:
    if word[0].upper() in vowels:
        new_word = word + "yay"
        new_sentence.append(new_word)
    else:
        if word[0].isupper():
            new_word = word[1:] + word[0] + "ay"
            new_word = new_word.capitalize()
        else:
            new_word = word[1:] + word[0] + "ay"
        new_sentence.append(new_word)

NEW_SENTENCE = " ".join(new_sentence)
print(NEW_SENTENCE)
