---
title: "01 - Chatbots, Variables and Input"
description: Ask a question, save the answer, and use it in a Python chatbot.
order: 3
draft: false
---
## Today you will

Make a small chatbot that asks a question and replies using the answer.

By the end, you should be able to:

- ask a question with `input()`;
- save the answer in a variable; and
- use the saved answer in a message.

## Get ready

Open Thonny and get ready to type and run a Python program. Use made-up
answers only. Do not enter real passwords, addresses, phone numbers, or other
private information.

## 1. Watch and predict

Look at the code. Before it runs, think: **What will appear on the screen?**
What do you think `name` will contain?

```python
name = "Alex"
print("Hello", name)
```

`name` is a **variable**: a named place where the program keeps information.
The `=` sign puts `"Alex"` into the variable `name`.

## 2. Run it together

Run the code and compare what happened with your prediction.

Now look at this new instruction:

```python
name = input("What is your name? ")
```

`input()` asks a question and waits for someone to type an answer and press
Enter. The program saves that answer in `name`.

Run this complete program. Type a made-up name when it asks:

```python
name = input("What is your name? ")
print("Hello", name)
```

## 3. Investigate

Follow what happens in order:

1. `input()` asks the question.
2. The program waits while you type and press Enter.
3. Your answer is saved in `name`.
4. `print()` displays the greeting and the saved answer.

The program runs from top to bottom. The answer must be saved before the
program can use it.

## 4. Change the code

Add a second question and reply. Use the same pattern as the first question:

```python
name = input("What is your name? ")
favourite_game = input("What is your favourite game? ")

print("Hello", name)
print(favourite_game, "sounds fun.")
```

Run the program. Try different made-up answers. Notice how the replies change.

## 5. Make your chatbot

Write a chatbot that:

1. asks for a made-up name;
2. asks for a hobby; and
3. replies using both answers.

Use this starter if you need it. Replace each `_____` with the correct
variable name:

```python
name = input("What is your name? ")
hobby = input("What is a hobby you enjoy? ")

print("Hello", _____)
print(_____, "sounds like fun.")
```

**Finished early?** Add another question, save its answer in a new variable,
and use that answer in another reply.

## Check your work

Before handing in, check:

- [ ] My program asks for a name and a hobby.
- [ ] I saved each answer in a variable.
- [ ] My replies use both answers.
- [ ] I ran my program and fixed any errors.

## Hand in your work

Save your Python program as your teacher has shown you. Use the submission
link for your class at the bottom of this page and follow the instructions
there to send in your file.
