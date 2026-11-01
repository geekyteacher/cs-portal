---
title: Images
description: Explain how bitmap images are represented and stored digitally.
order: 3
draft: false
---

# Images

## Learning goals

- [ ] Explain how a computer represents an image using pixels and binary.
- [ ] Define image resolution and colour depth.
- [ ] Calculate the file size of an uncompressed image.
- [ ] Describe how resolution and colour depth affect image quality and file size.

## Key ideas

### Pixels and binary

A digital image is made up of tiny picture elements called **pixels**. The computer stores a binary value for each pixel to represent its colour. When the pixels are displayed together in a grid, they form the complete image.

### Resolution

**Resolution** is the number of pixels in an image. It is often given as the image width multiplied by its height, for example, 640 pixels wide by 480 pixels high:

```text
Total pixels = width × height
```

An image of 640 × 480 pixels contains 307,200 pixels. A higher resolution means more pixels are used to represent the image. This can show more detail, especially when the image is enlarged, but it also increases the amount of data that must be stored.

### Colour depth

**Colour depth** is the number of bits used to represent the colour of each pixel. With *n* bits per pixel, the computer can represent up to `2^n` different colours.

For example, a colour depth of 8 bits can represent `2^8 = 256` colours. A colour depth of 24 bits can represent `2^24 = 16,777,216` colours. A greater colour depth allows a wider range of colours to be represented, but requires more storage for every pixel.

### Image file size

For an uncompressed image, calculate the pixel data size using:

```text
Image size in bits = width × height × colour depth
```

Divide by 8 to convert bits to bytes. If converting bytes to kilobytes using 1 KB = 1024 bytes, divide by 1024.

This calculation gives the size of the image's pixel data. A saved file may be larger because it can also contain metadata, or smaller if a compression method is used.

## Worked example

An uncompressed image is 640 pixels wide and 480 pixels high, with a colour depth of 24 bits.

1. Calculate the number of pixels: `640 × 480 = 307,200 pixels`.
2. Calculate the size in bits: `307,200 × 24 = 7,372,800 bits`.
3. Convert bits to bytes: `7,372,800 ÷ 8 = 921,600 bytes`.
4. Convert bytes to kilobytes: `921,600 ÷ 1024 = 900 KB`.

The image's pixel data requires **900 KB** of storage, using 1 KB = 1024 bytes.

## Practice

1. An image is 320 pixels wide and 200 pixels high. How many pixels does it contain?
2. How many different colours can be represented using a colour depth of 4 bits?
3. An uncompressed image is 800 pixels wide, 600 pixels high, and has a colour depth of 8 bits. Calculate its size in bits and bytes.
4. Explain how increasing the resolution affects the detail and file size of an image.
5. Explain how increasing the colour depth affects the range of colours and file size of an image.

## Answers

1. `320 × 200 = 64,000 pixels`.
2. `2^4 = 16 colours`.
3. `800 × 600 × 8 = 3,840,000 bits`; `3,840,000 ÷ 8 = 480,000 bytes`.
4. More pixels can represent more detail, but more pixel data must be stored, so the file size increases.
5. More bits per pixel can represent a wider range of colours, but each pixel requires more storage, so the file size increases.