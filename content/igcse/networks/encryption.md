---
title: "2.3 Encryption"
description: Explain how symmetric and asymmetric encryption protect data.
type: lesson
order: 6
draft: false
---

## Learning goals

- Explain why data may be encrypted.
- Distinguish plaintext from ciphertext.
- Describe symmetric encryption and its key-distribution problem.
- Describe how public and private keys are used in asymmetric encryption.
- Compare when symmetric and asymmetric encryption may be useful.

## Quick start

Imagine sending a private message across a network that other people can
access.

1. What could happen if someone intercepted the message?
2. How might the sender make the message difficult to understand without
   changing who it is intended for?

## Key terms

- **Plaintext** is the original, readable data.
- **Encryption** changes plaintext into an unreadable form using an
  encryption method and key.
- **Ciphertext** is the encrypted, unreadable data.
- **Decryption** changes ciphertext back into readable data using the
  appropriate key.

Encryption is used to help keep data confidential if it is intercepted.

## Symmetric encryption

In **symmetric encryption**, the same secret key is used to encrypt and
decrypt the data.

1. The sender and receiver share a secret key.
2. The sender encrypts the plaintext using that key.
3. The receiver uses the same key to decrypt the ciphertext.

The sender and receiver must keep the key secret. They need a secure way to
share it; if someone else obtains the key, that person may be able to decrypt
the data.

## Asymmetric encryption

In **asymmetric encryption**, each user has a related pair of keys:

- a **public key**, which can be shared with other people
- a **private key**, which is kept secret by its owner

To send confidential data to a receiver:

1. The sender obtains the receiver's public key.
2. The sender encrypts the message using that public key.
3. The receiver uses their own private key to decrypt the ciphertext.

The public key can be shared without giving away the private key. The
receiver must keep the private key secure.

## Compare the approaches

| Feature | Symmetric encryption | Asymmetric encryption |
| --- | --- | --- |
| Keys used | One shared secret key is used by both sender and receiver. | A related public and private key pair is used. |
| Main challenge | The secret key must be shared securely. | The private key must be protected; the public key can be shared. |
| Typical strength | Efficient for encrypting larger amounts of data. | Helps address the problem of sharing a secret key securely. |

The methods can be used together: asymmetric encryption can help establish
or share a secret key, and symmetric encryption can then be used for the
data. Follow the wording and scope of the question when describing a system.

## Worked example

Alex wants to send a confidential message to Sam using asymmetric
encryption.

1. Alex uses **Sam's public key** to encrypt the message.
2. Sam uses **Sam's private key** to decrypt it.

Alex does not use Alex's private key to decrypt this message; the private key
belongs to the intended receiver, Sam.

## Practice

### 1. Key vocabulary

Match each term to its meaning:

1. Plaintext
2. Ciphertext
3. Encryption
4. Decryption

Meanings:

- The original readable message.
- Changing encrypted data back into readable data.
- The unreadable result of encryption.
- Changing readable data into an unreadable form.

### 2. Trace the keys

Mina wants to send a confidential message to Ravi using asymmetric
encryption.

1. Which key should Mina use to encrypt the message?
2. Which key should Ravi use to decrypt it?
3. Which key must Ravi keep secret?

### 3. Compare encryption methods

Complete the comparison:

1. Which method uses the same key to encrypt and decrypt?
2. What is the key-distribution problem with this method?
3. Which keys are used when encrypting a confidential message for someone
   with asymmetric encryption?
4. Why can a public key be shared openly?

## Homework

Create a comparison table for symmetric and asymmetric encryption. Include
the keys used, one benefit, and one challenge for each method. Then explain
which key Mina should use to send a confidential message to Ravi and which
key Ravi uses to decrypt it.

## Exit check

1. What is the difference between plaintext and ciphertext?
2. Which key is shared in symmetric encryption?
3. Which key does a sender use to encrypt a confidential message for a
   receiver using asymmetric encryption?
4. Which key does the receiver use to decrypt it?
