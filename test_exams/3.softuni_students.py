def softuni_students(*args, **kwargs):
    valid_students = {}
    invalid_students = []

    for arg in args:
        student_id, username = arg

        if student_id not in kwargs:
            invalid_students.append(username)
        else:
            valid_students[username] = kwargs[student_id]

    result = []
    for nickname, course in sorted(valid_students.items()):
        result.append(f"*** A student with the username {nickname} has successfully finished the course {course}!")

    if invalid_students:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid_students))}")

    return "\n".join(result)