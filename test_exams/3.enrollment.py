def gather_credits(credits_needed, *courses):
    courses_enrolled = []
    my_credits = 0

    for course, amount in courses:
        if my_credits >= credits_needed:
            break
        if course in courses_enrolled:
            continue
        courses_enrolled.append(course)
        my_credits += amount

    result = ''

    if my_credits < credits_needed:
        result += f"You need to enroll in more courses! You have to gather {credits_needed - my_credits} credits more."
    else:
        result += f"Enrollment finished! Maximum credits: {my_credits}.\nCourses: "
        result += f"{', '.join(sorted(courses_enrolled))}"

    return result


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
