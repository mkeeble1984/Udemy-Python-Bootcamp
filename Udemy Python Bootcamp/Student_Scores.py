student_scores = {
    "John": 90,
    "Edy": 68,
    "Marry": 88,
    "Ewan": 79,
    "Park": 62,
}


def convert_grade(p_student_scores):
    for key in p_student_scores:
        if p_student_scores[key] >= 85:
            p_student_scores[key] = "Outstanding"
        elif p_student_scores[key] >= 65:
            p_student_scores[key] = "Good"
        elif p_student_scores[key] >= 50:
            p_student_scores[key] = "Acceptable"
        else:
            p_student_scores[key] = "Fail"

    return p_student_scores


print(convert_grade(student_scores))
