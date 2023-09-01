import tkinter as tk
from tkinter import filedialog
from main import run
import sys
python_path = sys.executable

import os
if not os.path.exists(python_path):
    raise FileNotFoundError(f"Python executable not found at {python_path}")

class AnkifySongGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window title and size
        self.title("AnkifySong - Turn Songs into Anki Flashcards")

        # YouTube Link Field
        self.youtube_label = tk.Label(self, text="YouTube Link:")
        self.youtube_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.youtube_entry = tk.Entry(self, width=40)
        self.youtube_entry.grid(row=0, column=1, padx=10, pady=10)
        
        default_youtube_link = "https://www.youtube.com/watch?v=r6cIKA1SWI8"
        self.youtube_entry.insert(0, default_youtube_link)

        # Deck Name Field
        self.deck_label = tk.Label(self, text="Deck Name:")
        self.deck_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.deck_entry = tk.Entry(self, width=40)
        self.deck_entry.grid(row=1, column=1, padx=10, pady=10)
        
        default_deck_name = "Spinning Sky Rabbit"
        self.deck_entry.insert(0, default_deck_name)

        # SRT File Field
        self.srt_label = tk.Label(self, text="SRT File:")
        self.srt_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.srt_entry = tk.Entry(self, width=30)
        self.srt_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        
        default_srt_path = r".\lyrics.srt"
        self.srt_entry.insert(0, default_srt_path)

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_srt)
        self.browse_button.grid(row=2, column=2, padx=10, pady=10)
        
        # Output Path Field
        self.output_label = tk.Label(self, text="Output Path:")
        self.output_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.output_entry = tk.Entry(self, width=30)
        self.output_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
        
        default_output_path = r".\anki_deck.apkg"
        self.output_entry.insert(0, default_output_path)

        self.output_browse_button = tk.Button(self, text="Browse", command=self.browse_output)
        self.output_browse_button.grid(row=3, column=2, padx=10, pady=10)
        
        # Start Button
        self.start_button = tk.Button(self, text="Start", command=self.start_process)
        # Autosize the window to fit content
        self.autosize_window()
    def autosize_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        self.geometry(f"{width}x{height}")

    def browse_srt(self):
        srt_path = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])
        self.srt_entry.delete(0, tk.END)
        self.srt_entry.insert(0, srt_path)
        
    def start_process(self):
        link = self.youtube_entry.get()
        name = self.deck_entry.get()
        srt_path = self.srt_entry.get()
        run(link, name, srt_path)

if __name__ == "__main__":
    app = AnkifySongGUI()
    app.mainloop()
