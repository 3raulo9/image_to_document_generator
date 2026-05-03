import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Tool")
        self.root.geometry("500x400")
        self.root.configure(bg="#2e2e2e")  # Dark background

        self.file_paths = []

        # --- UI Elements ---
        self.label = tk.Label(
            root, text="Selected Files:", bg="#2e2e2e", fg="white", font=("Arial", 12, "bold")
        )
        self.label.pack(pady=10)

        # Listbox to show files
        self.file_listbox = tk.Listbox(
            root, width=60, height=12, bg="#1e1e1e", fg="#00ff00", 
            borderwidth=0, highlightthickness=1, highlightcolor="#444"
        )
        self.file_listbox.pack(pady=5, padx=20)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#2e2e2e")
        btn_frame.pack(pady=20)

        self.add_btn = tk.Button(
            btn_frame, text="Add Images", command=self.pick_images,
            width=15, bg="#4a4a4a", fg="white", relief="flat"
        )
        self.add_btn.grid(row=0, column=0, padx=5)

        self.convert_btn = tk.Button(
            btn_frame, text="Convert to PDF", command=self.convert_to_pdf,
            width=15, bg="#28a745", fg="white", relief="flat"
        )
        self.convert_btn.grid(row=0, column=1, padx=5)

    def pick_images(self):
        files = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if files:
            self.file_paths.extend(list(files))
            self.update_listbox()

    def update_listbox(self):
        self.file_listbox.delete(0, tk.END)
        for path in self.file_paths:
            # Show just the filename for a cleaner look
            self.file_listbox.insert(tk.END, f" 📄 {os.path.basename(path)}")

    def convert_to_pdf(self):
        if not self.file_paths:
            messagebox.showwarning("Warning", "Please add some images first!")
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

            # Save the PDF
            images[0].save(
                output_path, 
                save_all=True, 
                append_images=images[1:]
            )
            
            messagebox.showinfo("Success", f"PDF created successfully!\nSaved to: {output_path}")
            # Clear list after success
            self.file_paths = []
            self.update_listbox()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()