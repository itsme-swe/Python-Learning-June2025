def result(mrk1, mrk2, mrk3):
    total = mrk1 + mrk2 + mrk3
    avg = round(total / 3, 2)

    if avg >= 45:
        grade = "Pass"
    else:
        grade = "Fail"

    return total, avg, grade


s1 = result(30, 50, 30)

print(s1)  # (110, 36.67, 'Fail')
