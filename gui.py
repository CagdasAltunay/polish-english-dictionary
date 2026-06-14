import tkinter as tk
from tkinter import messagebox


class Word:
    def __init__(self, polish, english):
        self.polish = polish
        self.english = english

dictionary = []


def add_word():
    polish = entry_polish.get()
    english = entry_english.get()

    if not polish or not english:
        messagebox.showerror("Error", "Empty value cannot be entered")
        return


    existing = list(filter(lambda w: w.polish.lower() == polish.lower(), dictionary))

    if existing:
        existing[0].english = english
        messagebox.showinfo("Updated", "Word updated")
    else:
        dictionary.append(Word(polish, english))
        messagebox.showinfo("Success", "Word added")


def list_words():
    listbox.delete(0, tk.END)

    # Functional: map + lambda
    words = list(map(lambda w: f"{w.polish} - {w.english}", dictionary))

    for w in words:
        listbox.insert(tk.END, w)


def search_word():
    search = entry_polish.get()

    # Functional: filter + lambda
    result = list(filter(lambda w: w.polish.lower() == search.lower(), dictionary))

    if result:
        messagebox.showinfo("Result", result[0].english)
    else:
        messagebox.showerror("Not Found", "Word not found")



root = tk.Tk()
root.title("Dictionary App")
root.geometry("400x400")

tk.Label(root, text="Polish").pack()
entry_polish = tk.Entry(root)
entry_polish.pack()

tk.Label(root, text="English").pack()
entry_english = tk.Entry(root)
entry_english.pack()

tk.Button(root, text="Add / Update", command=add_word).pack()
tk.Button(root, text="Search", command=search_word).pack()
tk.Button(root, text="List Words", command=list_words).pack()

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()


# This program demonstrates:
# - Object-Oriented Programming (Word class)
# - Functional Programming (lambda, filter, map)
# - Event-Driven Programming (Tkinter GUI)