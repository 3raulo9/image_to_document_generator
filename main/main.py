import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Import our custom components
from gui_components import ImagePreviewer, FileListManager
from pdf_engine import PDFEngine

class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modular Image to PDF Tool")
        self.root.geometry("850x600")
        self.root.configure(bg="#2e2e2e")

        self.file_paths = []

        # Header
        tk.Label(root, text="Image to PDF Converter", bg="#2e2e2e", fg="white", 
                 font=("Arial", 16, "bold")).pack(pady=15)

        # Layout Container
        self.main_container = tk.Frame(root, bg="#2e2e2e")
        self.main_container.pack(padx=20, fill="both", expand=True)

        # Initialize Components
        self.file_manager = FileListManager(self.main_container, self.handle_selection)
        self.file_manager.pack(side="left", fill="both", expand=True)
        self.file_manager.up_btn.config(command=self.move_up)
        self.file_manager.down_btn.config(command=self.move_down)

        self.previewer = ImagePreviewer(self.main_container, width=300, height=300)
        self.previewer.pack(side="right", padx=(20, 0))

        # Bottom Buttons
        self.create_controls()

    def create_controls(self):
        ctrl_frame = tk.Frame(self.root, bg="#2e2e2e")
        ctrl_frame.pack(pady=20)

        btns = [
            ("Add Images", self.add_images, "#5a5a5a"),
            ("Remove", self.remove_item, "#cc4444"),
            ("Clear All", self.clear_all, "#888"),
            ("Convert to PDF", self.convert, "#28a745")
        ]

        for text, cmd, color in btns:
            tk.Button(ctrl_frame, text=text, command=cmd, width=15, 
                      bg=color, fg="white", relief="flat").pack(side="left", padx=5)

    def handle_selection(self, event=None):
        selection = self.file_manager.listbox.curselection()
        if selection:
            path = self.file_paths[selection[0]]
            self.previewer.update_preview(path)

    def add_images(self):
        files = filedialog.askopenfilenames(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if files:
            self.file_paths.extend(list(files))
            self.refresh_list()

    def refresh_list(self, select_idx=None):
        self.file_manager.listbox.delete(0, tk.END)
        for i, path in enumerate(self.file_paths, 1):
            self.file_manager.listbox.insert(tk.END, f"{i}. {os.path.basename(path)}")
        
        if select_idx is not None:
            self.file_manager.listbox.select_set(select_idx)
            self.handle_selection()

    def move_up(self):
        idx = self.file_manager.listbox.curselection()
        if idx and idx[0] > 0:
            i = idx[0]
            self.file_paths[i], self.file_paths[i-1] = self.file_paths[i-1], self.file_paths[i]
            self.refresh_list(i-1)

    def move_down(self):
        idx = self.file_manager.listbox.curselection()
        if idx and idx[0] < len(self.file_paths) - 1:
            i = idx[0]
            self.file_paths[i], self.file_paths[i+1] = self.file_paths[i+1], self.file_paths[i]
            self.refresh_list(i+1)

    def remove_item(self):
        idx = self.file_manager.listbox.curselection()
        if idx:
            del self.file_paths[idx[0]]
            self.refresh_list()

    def clear_all(self):
        self.file_paths.clear()
        self.refresh_list()

    def convert(self):
        out = filedialog.asksaveasfilename(defaultextension=".pdf")
        if out:
            success, msg = PDFEngine.convert_images_to_pdf(self.file_paths, out)
            if success:
                messagebox.showinfo("Done", "PDF Created!")
            else:
                messagebox.showerror("Error", msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()