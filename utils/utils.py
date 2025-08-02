import tkinter as tk
from tkinter import filedialog


def open_file_dialog() -> str:
    """
    ph
    """
    root = tk.Tk()
    root.withdraw()

    try:
        file_path = filedialog.askopenfilename(
            title="Select a file",
            initialdir="/",
            filetypes=(
                ("Image files", "*.jpg *.jpeg *.png *.bmp"),
                ("All files", "*.*"),
            ),
        )
        return file_path
    except PermissionError:
        print("No image was picked for encoding.")
        return ""


def save_file_as() -> str:
    """
    ph
    """
    root = tk.Tk()
    root.withdraw()

    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save secret as PNG",
            initialdir="/",
            initialfile="fun_image.png",
        )
        return file_path
    except PermissionError:
        print("No name was picked for saving the image.")
        return ""


if __name__ == "__main__":
    open_file_dialog()
