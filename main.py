# standard library
from typing import cast
import sys

# third-party imports
from PIL import Image

# local imports
from utils.utils import *


class ImageSecret:
    def __init__(self) -> None:
        pass

    @staticmethod
    def encode_image(image_path, secret_message, output_path="output/image.png"):
        """
        ph
        """
        # append delimiter to mark end
        secret_message += "####"
        binary_message = "".join(f"{ord(c):08b}" for c in secret_message)

        img = Image.open(image_path).convert("RGB")
        pixels = img.load()

        if not pixels:
            return None

        width, height = img.size
        total_pixels = width * height

        if len(binary_message) > total_pixels:
            raise ValueError("Message is too long to encode in this image.")

        index = 0
        for y in range(height):
            for x in range(width):
                if index >= len(binary_message):
                    break

                r, g, b = cast(tuple[int, int, int], pixels[x, y])
                bit = binary_message[index]
                r = (r & ~1) | int(bit)  # replaces LSB of red channel
                pixels[x, y] = (r, g, b)
                index += 1

        img.save(output_path)

    @staticmethod
    def decode_image(image_path):
        """
        ph
        """
        img = Image.open(image_path).convert("RGB")
        pixels = img.load()

        if not pixels:
            return None

        width, height = img.size

        bits = []
        for y in range(height):
            for x in range(width):
                r, _, _ = cast(tuple[int, int, int], pixels[x, y])
                bits.append(str(r & 1))

        chars = [chr(int("".join(bits[i : i + 8]), 2)) for i in range(0, len(bits), 8)]
        message = "".join(chars)

        end_index = message.find("####")
        if end_index == -1:
            raise ValueError("Delimiter not found. Image may not contain a message.")
        return message[:end_index]

    def encode_prompt(self):
        """
        ph
        """
        print("\nWhat image do you want to encode a secret into?")
        starter_image_path = open_file_dialog()
        print(f"Selected: {starter_image_path}")

        print("\nWhere do you want to save the image?")
        image_output_path = save_file_as()
        print(f"Save location: {starter_image_path}")

        secret = input("\nWhat message do you want to encode into the image?\n")
        self.encode_image(starter_image_path, secret, image_output_path)
        print("Encoding was completed.")

    def decode_prompt(self):
        """
        ph
        """
        image_path = open_file_dialog()
        print(f"\nDecoding: {image_path}\n")

        secret = self.decode_image(image_path)
        print(f"Decoded Secret: {secret}")

    def run(self):
        print("\nSecret Message Encoder/Decoder")

        try:
            response = input("\nWhat do you want to do?\n1.Encode\n2.Decode\n")

            # -------- Encoding --------
            if response == "1":
                self.encode_prompt()

            # -------- Decoding --------
            elif response == "2":
                self.decode_prompt()

            print("Press enter to restart")
            self.run()

        except KeyboardInterrupt:
            input("Process Cancelled\n Press Enter to Exit")
            sys.exit()


if __name__ == "__main__":
    app = ImageSecret()
    app.run()
