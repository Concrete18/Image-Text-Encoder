# standard library
import argparse

# local imports
from main import ImageSecret


def main():
    app = ImageSecret()
    parser = argparse.ArgumentParser(
        description="Encode or decode messages in PNG images."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # encode subcommand
    encode_parser = subparsers.add_parser(
        "encode", help="Encode a message into an image."
    )
    encode_parser.add_argument("image", help="Path to the input PNG image.")
    encode_parser.add_argument("message", help="Message to encode.")
    encode_parser.add_argument("output", help="Path to save the encoded PNG.")

    # decode subcommand
    decode_parser = subparsers.add_parser(
        "decode", help="Decode a message from an image."
    )
    decode_parser.add_argument("image", help="Path to the encoded PNG image.")

    args = parser.parse_args()

    if args.command == "encode":
        app.encode_image(args.image, args.message, args.output)
    elif args.command == "decode":
        app.decode_image(args.image)


if __name__ == "__main__":
    main()
