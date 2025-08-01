from main import *


class TestEncodeDecode:

    app = ImageSecret()

    def test_success(self):
        image_path = "tests/test_image_1.jpg"
        secret_message = "This is a secret test message."
        self.app.encode_image(image_path, secret_message)

        secret = self.app.decode_image("output/image.png")
        assert secret_message == secret
