"""
Validation examples for IGCSE and A level students.

Validation checks whether data is sensible and follows rules. It cannot prove
that data is correct. Verification checks that data matches its source, for
example by visual checking or entering it twice; those are processes rather
than checks performed by the functions below.
"""


def range_check(value: int, lower: int, upper: int) -> bool:
    """Return True when value is between lower and upper, inclusive."""
    return lower <= value <= upper


def len_check(text: str, min_len: int, max_len: int) -> bool:
    """Return True when text contains between min_len and max_len characters."""
    return min_len <= len(text) <= max_len


def is_integer(value: str) -> bool:
    """Return True if the text can be converted to an integer.

    input() always returns a string, so check by attempting the conversion.
    This does not check whether the resulting number is sensible or in range.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value: str) -> bool:
    """Return True if the text can be converted to a floating-point number."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def presence_check(value: str) -> bool:
    """Return True when at least one character has been entered."""
    return value != ""


def email_check(value: str) -> bool:
    """A simple format-check example, not a complete email-address validator."""
    return "@" in value and ".com" in value


def date_format_check(value: str) -> bool:
    """Check that a date is written as DD/MM/YYYY.

    This checks the format only; it does not check that the date exists
    (for example, 31/02/2026 has the right format but is not a real date).
    """
    return (
        len(value) == 10
        and value[2] == "/"
        and value[5] == "/"
        and value[:2].isdigit()
        and value[3:5].isdigit()
        and value[6:].isdigit()
    )


def check_digit(value: str) -> bool:
    """Check a number using an alternating 3, 1 weighted-modulo-10 method.

    The final character is the check digit. Starting at the left, multiply
    the other digits alternately by 3 and 1. The check digit is the amount
    needed to make the weighted total a multiple of 10.

    This is one example algorithm; check-digit schemes can use different
    weights and rules.
    """
    if len(value) < 2 or not value.isdigit():
        return False

    weighted_total = 0
    for index, digit in enumerate(value[:-1]):
        weight = 3 if index % 2 == 0 else 1
        weighted_total += int(digit) * weight

    expected_check_digit = (10 - weighted_total % 10) % 10
    return int(value[-1]) == expected_check_digit


if __name__ == "__main__":
    # Each example prints True or False so students can try changing the data.
    print("Range:", range_check(15, 1, 20))
    print("Length:", len_check("Python", 1, 10))
    print("Integer:", is_integer("42"))
    print("Float:", is_float("3.14"))
    print("Presence:", presence_check("Hello"))
    print("Email format:", email_check("student@example.com"))
    print("Date format:", date_format_check("01/01/2026"))
    print("Check digit:", check_digit("1236"))
