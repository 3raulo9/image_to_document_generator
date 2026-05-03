import os
from tkinter import Tk, filedialog
from PIL import Image

def pick_images():
    root = Tk()
    root.withdraw()  # hide main window

    file_paths = filedialog.askopenfilenames(
        title="Select images",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("All files", "*.*")
        ]
    )

    return list(file_paths)


def convert_to_pdf(image_paths, output_path):
    images = []

    for path in image_paths:
        img = Image.open(path)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        images.append(img)

    if not images:
        print("[!] No images selected")
        return

    images[0].save(output_path, save_all=True, append_images=images[1:])
    print(f"[+] PDF created: {output_path}")


if __name__ == "__main__":
    image_paths = pick_images()

    if not image_paths:
        print("No files selected.")
        exit()

    output_path = "output.pdf"
    convert_to_pdf(image_paths, output_path)