# standard library
from typing import cast

# third-party imports
from PIL import Image

from utils.utils import *


class ImageSecret:

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

    def run(self):
        print("\nSecret Message Encode/Decode")

        response = input("What do you want to do?\n1.Encode\n2.Decode\n")

        # -------- Encoding --------
        if response == "1":
            print("What image do you want to encode a secret into?")
            starter_image_path = open_file_dialog()

            print("Where do you want to save the image?")
            image_output_path = save_file_as()

            secret = input("\nWhat message do you want to encode into the image?\n")
            self.encode_image(starter_image_path, secret, image_output_path)
            print("Encoding was completed.")

        # -------- Decoding --------
        elif response == "2":
            image_path = open_file_dialog()
            secret = self.decode_image(image_path)
            print(f"Decoded Secret: {secret}")


if __name__ == "__main__":
    app = ImageSecret()
    app.run()
