---
title: "Lesson 3: Input & Output Mechanics"
description: "Use user prompts, formatted outputs, and string concatenation."
order: 3
draft: false
---

> [!NOTE]
>
> Complete the reading and tasks below. Record your work in **Lesson 3** of your **Teams Portfolio Document**.

## Learning Objectives

- Differentiate between input prompts and output statements.
- Use string concatenation to format outputs clearly.
- Construct algorithms that interact with users and follow specific formatting rules.

---

## 1. Explanation: Input & Output

Programs receive data from users (**input**) and display information or results (**output**).

In pseudocode, use `INPUT` to receive a value and `OUTPUT` to display a message or value:

```pseudocode
OUTPUT "Please enter your name:"
INPUT UserName
OUTPUT "Welcome back, ", UserName
```

The equivalent Python program uses `input()` and `print()`:

```python
user_name = input("Please enter your name: ")
print("Welcome back, " + user_name)
```

The `+` operator joins strings together. This is called **string concatenation**.

## 2. Practical Coding Activity

Create an interactive receipt generator in Python. Run the program and test it with different item names, prices, and quantities.

```python
item_name = input("Enter item name: ")
price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
tax = subtotal * 0.20
total = subtotal + tax

print("----- RECEIPT -----")
print("Item:", item_name)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (20%): ${tax:.2f}")
print(f"TOTAL DUE: ${total:.2f}")
```

## 3. Portfolio Tasks (Submit to Teams)

> [!WARNING]
>
> Copy your answers into **Lesson 3** of your **Algorithm Design Portfolio** in Teams.

1. **Code Correction:** The pseudocode below contains syntax and logic errors. Identify the errors and rewrite the algorithm correctly so it inputs a length and width, calculates the area, and displays the result.

    ```pseudocode
    INPUT "Enter length:" Length
    Width <- INPUT
    Area = Length * Width
    PRINT "Area is" + Area
    ```

2. **Algorithm Design (Average Calculator):** Write pseudocode that prompts the user for three test scores, calculates their average, and displays it in this format: `"The candidate average is: [Value]"`.

3. **Formatting Output:** Write Python or pseudocode that asks for a person's first name and surname separately, then outputs them in this format: `"Formatting: [Surname], [FirstName]"`.

> [!CHALLENGE]
>
> Extend your average calculator in Python so the average is displayed to two decimal places. For example, use an f-string with a format specifier such as `{average:.2f}`.
