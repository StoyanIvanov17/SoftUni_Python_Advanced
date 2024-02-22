def students_credits(*args):
    final_result = []
    subjects = {}
    credit_score = 0

    for arg in args:
        subject, course_credits, max_test_points, points_achieved = arg.split('-')
        credits_earned = (int(points_achieved) / int(max_test_points)) * int(course_credits)
        credit_score += credits_earned
        subjects[subject] = credits_earned

    if credit_score >= 240:
        final_result.append(f"Diyan gets a diploma with {credit_score:.1f} credits.")
    else:
        final_result.append(f"Diyan needs {240 - credit_score:.1f} credits more for a diploma.")

    sorted_subjects = sorted(subjects.items(), key=lambda x: -x[1])
    for c, p in sorted_subjects:
        final_result.append(f"{c} - {float(p):.1f}")

    return f"\n".join(final_result)
