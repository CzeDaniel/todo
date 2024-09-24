# main.py

import tkinter as tk
from gui import ContentIdeenGeneratorApp

def main():
    root = tk.Tk()
    app = ContentIdeenGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()