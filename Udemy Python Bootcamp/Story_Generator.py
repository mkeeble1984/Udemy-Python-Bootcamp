def structure(p_sentence, p_story):
    question = ['When', 'What', 'Where', 'Who',
                'Whom', 'Whose', 'Why', 'Which', 'How', 'Is', 'Are']

    if p_sentence[-1] == "?" or p_sentence[-1] == "." or p_sentence[-1] == "!":
        pass
    else:
        if sentence.split(" ", 1)[0] in question:
            p_sentence = p_sentence + "?"
        else:
            p_sentence = p_sentence + "."
    p_story += p_sentence + " "
    return p_story


repeat = True
story = ""
while repeat:
    sentence = input("What is on your mind? ").capitalize()
    if sentence != "\end":
        story = structure(sentence, story)
    else:
        break
print(story)
