import tkinter as tk
from PIL import Image, ImageTk
import os

class ImagePreviewer(tk.Frame):
    """A dedicated frame for displaying image thumbnails."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#1e1e1e", highlightthickness=1, highlightbackground="#555")
        self.pack_propagate(False)

        self.label = tk.Label(self, text="No Image Selected", bg="#1e1e1e", fg="#888")
        self.label.pack(expand=True, fill="both")
        self.current_img = None

    def update_preview(self, image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((280, 280))
            photo = ImageTk.PhotoImage(img)
            self.label.config(image=photo, text="")
            self.current_img = photo  # Keep reference
        except:
            self.label.config(image='', text="Preview Error")

class FileListManager(tk.Frame):
    """A frame containing the listbox and the Up/Down buttons."""
    def __init__(self, master, on_select_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#2e2e2e")
        
        # Listbox
        self.listbox = tk.Listbox(
            self, width=45, height=15, bg="#1e1e1e", fg="#00ff99",
            borderwidth=0, selectbackground="#444"
        )
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind('<<ListboxSelect>>', on_select_callback)

        # Reorder Buttons
        btn_frame = tk.Frame(self, bg="#2e2e2e")
        btn_frame.pack(side="right", padx=5)
        
        self.up_btn = tk.Button(btn_frame, text="▲", width=3, bg="#4a4a4a", fg="white")
        self.up_btn.pack(pady=2)
        
        self.down_btn = tk.Button(btn_frame, text="▼", width=3, bg="#4a4a4a", fg="white")
        self.down_btn.pack(pady=2)