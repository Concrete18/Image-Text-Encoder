# Image Text Encoder

A command-line and GUI tool that lets you hide secret messages inside PNG images using basic steganography, and later extract those messages. Supports encoding any UTF-8 text directly into the pixel data of an image without visibly altering it. Ideal for lightweight, offline message hiding.

## Setup

Run the follow command to install libraries

```bash
pip install -r requirements.txt
```

## Usage

## Run using a terminal interface

Run Python script

```bash
python main.py
```

### CLI

```bash
usage: secret_image_cli.py [-h] {encode,decode} ...

Encode or decode messages in PNG images.

positional arguments:
  {encode,decode}
    encode         Encode a message into an image.
    decode         Decode a message from an image.

options:
  -h, --help       show this help message and exit
```
