student_scores = [80, 60, 50, 65, 75, 55]
current_highest = student_scores[0]

for highest in student_scores:
    if highest > current_highest:
        current_highest = highest

print(current_highest)
