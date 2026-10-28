---
title: "02 - Chatbots and Selection"
description: Make a chatbot choose a response using an if and else statement.
order: 4
draft: false
---
## Today you will

Make your chatbot choose a different reply depending on an answer.

By the end, you should be able to:

- check an answer using `==`;
- use `if` and `else` to choose between actions; and
- add a choice to a chatbot.

<!-- Suggested pace for a 45-minute lesson: Remember (5 min), Watch and predict
(5 min), Run it together (10 min), Change the code (10 min), Make your
chatbot (10 min), Check and hand in (5 min). -->

## Get ready

Open Thonny. If you have your chatbot from the last lesson, open it. If not,
you can start with the example in Step 2.

## 1. Remember

Look at this line from the last lesson:

```python
hobby = input("What is a hobby you enjoy? ")
```

What does `input()` do? Where does the program keep the answer?

In this lesson, the chatbot will use an answer to choose what to say next.

## 2. Watch and predict

Read this code. Before running it, predict what will happen if the answer is
`yes`. What do you think will happen if the answer is `no`?

```python
answer = input("Do you like computer games? Type yes or no: ")

if answer == "yes":
    print("Great! What is your favourite game?")
else:
    print("That is okay. What do you like doing?")
```

`if` checks a condition. Here, `answer == "yes"` checks whether the answer
matches the word `yes`.

The two equals signs `==` mean **check whether these values are the same**.
One equals sign `=` saves a value in a variable.

## 3. Run it together

Run the code. First type `yes`, then run it again and type `no`.

Notice:

- if the answer is `yes`, the indented instruction under `if` runs;
- otherwise, the indented instruction under `else` runs.

The indented lines belong to the `if` or `else` above them. Keep the spaces
at the start of those lines.

## 4. Change the code

Change the question and both replies so the chatbot asks about a hobby you
like. Keep the answer choices as `yes` and `no`.

Run the program twice: once with `yes`, and once with `no`. Check that the
chatbot gives a different reply each time.

> [!NOTE]
>
> Type `yes` in lowercase, just like it appears in the code. Python treats
> `Yes` and `yes` as different answers.

## 5. Make your chatbot

Create a chatbot that asks for a made-up name and then asks whether the
person likes a chosen activity. Make it greet the person and choose a reply
based on their answer.

Use this starter if you need it. Replace the `_____` parts with the correct
code:

```python
name = input("What is your name? ")
answer = input("Do you like drawing? Type yes or no: ")

print("Hello", name)

if answer == "_____":
    print("That sounds fun!")
else:
    print("What activity do you enjoy?")
```

Run your chatbot twice, using `yes` and `no`. If you finish early, add a
second question and another `if` statement.

## Check your work

Before handing in, check:

- [ ] My chatbot asks a question and saves the answer.
- [ ] I used `if` and `else` to choose a reply.
- [ ] I used `==` to check the answer.
- [ ] I tested both `yes` and `no`.

## Hand in your work

Save your Python program as your teacher has shown you. Use the submission
link for your class at the bottom of this page and follow the instructions
there to send in your file.
