#show_info_with_quit.py
#Mark_Nyagaka
#11-14-25

import tkinter as tk
from tkinter import messagebox

def show_info():
    name = "Mark Nyagaka"
    address_lines = [
        "3601 Phillips Pkwy",
        "St Louis Park, MN 55426",
        "markbarakan3@gmail.com"
    ]
    messagebox.showinfo("My Info", f"{name}\n" + "\n".join(address_lines))

def quit_app(root):
    root.destroy()

def main():
    root = tk.Tk()
    root.title("Contact Card")
    root.geometry("300x160")

    heading = tk.Label(root, text="Click to view my info:", font=("Helvetica", 12))
    heading.pack(pady=(20, 10))

    btn_show = tk.Button(root, text="Show Info", width=14, command=show_info)
    btn_show.pack(pady=4)

    btn_quit = tk.Button(root, text="Quit", width=14, command=lambda: quit_app(root))
    btn_quit.pack(pady=4)

    root.mainloop()

if __name__ == "__main__":
    main()