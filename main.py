import json
import tkinter as tk

with open("dict.json") as d:
    dictionary: dict = json.load(d)

root = tk.Tk()
ety_info = tk.Label(root, text="", anchor=tk.W, justify=tk.LEFT)
ety_info.grid(column=0, row=1, columnspan=2)

search = tk.StringVar()
search_box = tk.Entry(root, textvariable=search)


def search_dict():
    s = search.get().lower()
    if s in dictionary.keys():
        text = search.get()

        for i, v in enumerate(dictionary[s], 1):
            text += f"\n\t{i}. {v}"

    else:
        text = "Entry not found"

    ety_info["text"] = text


search_box.grid(row=0, column=0)
search_button = tk.Button(root, text="Search", command=search_dict)
search_button.grid(row=0, column=1)
root.mainloop()
