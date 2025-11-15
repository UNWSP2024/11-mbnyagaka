#favorite_saying.py
#Mark_Nyagaka
#11-14-25

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Favorite Saying")
    root.geometry("420x160")

    saying = "“No human is limited.”"

    lbl = tk.Label(
        root,
        text=saying,
        font=("Helvetica", 16, "italic"),
        wraplength=380,
        justify="center"
    )
    lbl.pack(expand=True, padx=16, pady=16)

    root.mainloop()

if __name__ == "__main__":
    main()