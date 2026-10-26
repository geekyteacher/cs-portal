"""Ready-to-run examples for the Year 8 compound conditions lesson."""


def show_score_example(score):
    print(f"\nScore: {score}")
    print(f"score >= 80: {score >= 80}")
    print(f"score >= 60: {score >= 60}")

    if score >= 80:
        print("Output: High score")
    elif score >= 60:
        print("Output: Good score")
    else:
        print("Output: Keep practising")


def show_and_example(age, height):
    print(f"\nAge: {age}; height: {height} cm")
    print(f"age >= 12: {age >= 12}")
    print(f"height >= 140: {height >= 140}")

    if age >= 12 and height >= 140:
        print("Output: Access Granted")
    else:
        print("Output: Access Denied")


def show_or_example(age, with_adult):
    print(f"\nAge: {age}; with adult: {with_adult}")
    print(f"age >= 12: {age >= 12}")
    print(f'with_adult == "yes": {with_adult == "yes"}')

    if age >= 12 or with_adult == "yes":
        print("Output: You may enter")
    else:
        print("Output: Entry denied")


def show_combined_example(username_correct, password_correct, is_admin, is_vip):
    print(
        "\nUsername correct: "
        f"{username_correct}; password correct: {password_correct}; "
        f"admin: {is_admin}; VIP: {is_vip}"
    )
    print(f"Admin or VIP: {is_admin or is_vip}")

    if username_correct and password_correct and (is_admin or is_vip):
        print("Output: Access granted")
    else:
        print("Output: Access denied")


def main():
    print("YEAR 8: COMPOUND CONDITIONS TEACHER DEMO")
    print("Each example shows the values, condition results, and output.")

    print("\n--- Quick check: if, elif, and else ---")
    show_score_example(72)
    show_score_example(45)

    print("\n--- AND: both conditions must be true ---")
    show_and_example(age=14, height=150)
    show_and_example(age=14, height=130)
    show_and_example(age=10, height=150)

    print("\n--- OR: at least one condition must be true ---")
    show_or_example(age=10, with_adult="yes")
    show_or_example(age=10, with_adult="no")
    show_or_example(age=12, with_adult="no")

    print("\n--- AND combined with OR ---")
    show_combined_example(
        username_correct=True,
        password_correct=True,
        is_admin=False,
        is_vip=True,
    )


if __name__ == "__main__":
    main()
