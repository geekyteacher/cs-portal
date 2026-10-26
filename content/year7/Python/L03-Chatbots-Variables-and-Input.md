---
title: Year 7 Python: Chatbots, Variables and Input
description: Use input, variables, and print to build a simple interactive Python chatbot.
order: 3
draft: false
---
## Learning Objectives

By the end of this lesson you should be able to:

- Explain what a variable is and how it stores information.
- Use `input()` to ask the user a question.
- Store an answer in a variable and use it in a response.
- Build a simple interactive chatbot.

## Prior Knowledge

Before starting this lesson, you should be able to:

- Open Python in Thonny and run a program.
- Use `print()` to display text.
- Recognise that Python runs instructions from top to bottom.

## Quick Knowledge Check

Try these before running the examples:

1. What does `print()` do?
2. What do you think this code displays?

   ```python
   name = "Alex"
   print("Hello", name)
   ```

3. What do you think `input()` lets a program do?

## Learn

### What is a variable?

A variable is a named place for storing a value. You can use that name later
to work with the stored value.

```python
name = "Alex"
print("Hello", name)
```

The `=` sign assigns the value `"Alex"` to the variable `name`. It does not
mean “is equal to” in the way it is used in a maths equation.

### Asking for input

The `input()` function displays a prompt, waits for the user to type, and
returns what they typed as text. Assign the result to a variable to keep it:

```python
name = input("What is your name? ")
print("Hello", name)
```

The program pauses at `input()` until the user types an answer and presses
Enter. That answer is stored in `name`, so the program can use it in the
greeting.

### Building a chatbot

A chatbot can ask questions, remember answers in variables, and respond to
them:

```python
name = input("What is your name? ")
favourite_game = input("What is your favourite game? ")

print(f"Hello, {name}!")
print(f"{favourite_game} sounds fun.")
```

The `f` before a string lets Python insert the value of a variable inside
curly brackets, such as `{name}`.

> [!WARNING]
>
> Use fictional answers while practising. Do not type real passwords,
> addresses, phone numbers, or other private information into a class activity.

## Teacher Demonstration

Project Thonny or the class Python environment and type the example as you
teach. Ask students to predict what will happen before each run.

1. Start with `print("Hello!")` and run it to recap output.
2. Add `name = input("What is your name? ")`. Run the program, type a
   fictional name, and point out that the program pauses until Enter is
   pressed.
3. Add `print("Hello", name)`. Run it again and trace how the typed answer is
   stored and then displayed.
4. Add a second question and response using `favourite_game`. Demonstrate that
   the variable names in the f-strings must match the names used when storing
   the answers.
5. Ask students to predict what would happen if `print()` used `favourite_game`
   before the program had asked for it.

## Guided Practice

Copy this starter into Thonny and fill in the gaps. Use made-up answers.

```python
name = input("What is your name? ")
favourite_food = input("What food do you like? ")

print(f"Hello, {_____}!")
print(f"I like hearing about {_____}.")
```

Check that the program asks both questions and uses each answer in a response.

## Practice

### Task 1: Friendly Greeting

Write a program that:

1. Asks the user for a name.
2. Stores the answer in a variable.
3. Prints a greeting that includes the answer.

### Task 2: Mini Chatbot

Make a chatbot that asks for the user's name and favourite hobby. It should
then respond using both answers.

Use this scaffold if you need help:

```python
name = input("What is your name? ")
hobby = input("What is a hobby you enjoy? ")

print(f"Hello, {_____}!")
print(f"{_____} sounds like fun.")
```

### Challenge: Chatbot Plus

Add one more question, such as a favourite animal or fictional superpower.
Store the answer in a new variable and include it in another response.

Can you make the chatbot display a three-line conversation using all of its
answers?

## Summary

You should now be able to:

- Use `input()` to collect text typed by the user.
- Store input in a variable using `=`.
- Use variables in `print()` and f-strings.
- Create a simple interactive chatbot.
