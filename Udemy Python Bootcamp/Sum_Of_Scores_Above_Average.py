student_scores = [80, 60, 50, 65, 75, 55]


def sum_score_above_average(p_student_scores):
    total = 0
    count = 0
    sum_score = 0
    for item in student_scores:
        total += item
        count += 1

    average = total / count

    for item in student_scores:
        if item > average:
            sum_score += item

    return sum_score


print(sum_score_above_average(student_scores))
