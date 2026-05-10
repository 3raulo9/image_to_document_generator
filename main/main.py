import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Tool")
        self.root.geometry("550x450")
        self.root.configure(bg="#2e2e2e")

        self.file_paths = []

        # --- Title ---
        self.label = tk.Label(
            root,
            text="Selected Images:",
            bg="#2e2e2e",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.label.pack(pady=10)

        # --- Listbox ---
        self.file_listbox = tk.Listbox(
            root,
            width=70,
            height=15,
            bg="#1e1e1e",
            fg="#00ff99",
            borderwidth=0,
            highlightthickness=1,
            highlightcolor="#555",
            selectbackground="#444"
        )
        self.file_listbox.pack(padx=20, pady=5)

        # --- Buttons Frame ---
        btn_frame = tk.Frame(root, bg="#2e2e2e")
        btn_frame.pack(pady=20)

        # Add ONE image at a time
        self.add_single_btn = tk.Button(
            btn_frame,
            text="Add Image",
            command=self.add_single_image,
            width=15,
            bg="#4a4a4a",
            fg="white",
            relief="flat"
        )
        self.add_single_btn.grid(row=0, column=0, padx=5)

        # Add MULTIPLE images
        self.add_multiple_btn = tk.Button(
            btn_frame,
            text="Add Multiple",
            command=self.pick_images,
            width=15,
            bg="#5a5a5a",
            fg="white",
            relief="flat"
        )
        self.add_multiple_btn.grid(row=0, column=1, padx=5)

        # Remove selected image
        self.remove_btn = tk.Button(
            btn_frame,
            text="Remove Selected",
            command=self.remove_selected,
            width=15,
            bg="#cc4444",
            fg="white",
            relief="flat"
        )
        self.remove_btn.grid(row=0, column=2, padx=5)

        # Convert button
        self.convert_btn = tk.Button(
            root,
            text="Convert to PDF",
            command=self.convert_to_pdf,
            width=25,
            bg="#28a745",
            fg="white",
            relief="flat",
            font=("Arial", 11, "bold")
        )
        self.convert_btn.pack(pady=10)

    # Add ONE image at a time
    def add_single_image(self):
        file = filedialog.askopenfilename(
            title="Select image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )

        if file:
            self.file_paths.append(file)
            self.update_listbox()

    # Add MULTIPLE images
    def pick_images(self):
        files = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )

        if files:
            self.file_paths.extend(list(files))
            self.update_listbox()

    # Update listbox
    def update_listbox(self):
        self.file_listbox.delete(0, tk.END)

        for index, path in enumerate(self.file_paths, start=1):
            self.file_listbox.insert(
                tk.END,
                f"{index}. {os.path.basename(path)}"
            )

    # Remove selected image
    def remove_selected(self):
        selected = self.file_listbox.curselection()

        if not selected:
            return

        index = selected[0]
        del self.file_paths[index]
        self.update_listbox()

    # Convert images into PDF
    def convert_to_pdf(self):
        if not self.file_paths:
            messagebox.showwarning(
                "Warning",
                "Please add some images first!"
            )
            return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile="merged_document.pdf"
        )

        if not output_path:
            return

        try:
            images = []

            for path in self.file_paths:
                img = Image.open(path)

                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                images.append(img)

            images[0].save(
                output_path,
                save_all=True,
                append_images=images[1:]
            )

            messagebox.showinfo(
                "Success",
                f"PDF created successfully!\n\nSaved to:\n{output_path}"
            )

            # Clear list after conversion
            self.file_paths.clear()
            self.update_listbox()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred:\n{e}"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()