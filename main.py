import json
import tkinter as tk

dict_fn = 'dict'

with open(f'{dict_fn}.json') as d:
    dictionary: dict = json.load(d)

with open(f'{dict_fn}.jdinf') as dinf:
    name = dinf.read().split('\n')[0]

dictionary = dict(sorted([(i, v) for i, v in dictionary.items()], key=lambda x: x[0]))

root = tk.Tk()
ico = tk.PhotoImage(file='logo.png')
root.wm_iconphoto(False, ico)
ety_info = tk.Label(root, text='', anchor=tk.W, justify=tk.LEFT, relief=tk.SUNKEN)
ety_info.grid(column=2, row=1)

scroll = tk.Scrollbar(root)
scroll.grid(row=0, column=0, rowspan=2)

search_results = tk.Listbox(root, justify=tk.LEFT, relief=tk.SUNKEN)
search_results.grid(row=1, column=1)

search_results.config(yscrollcommand=scroll.set)
scroll.config(command=search_results.yview)

search = tk.StringVar()
search_box = tk.Entry(root, textvariable=search)


def sel_word(e):
    search.set(e.widget.get(0, tk.END)[e.widget.curselection()[0]])
    search_dict()


def search_dict():
    s = search.get().lower()
    if s in dictionary.keys():
        text = f'From {name}\n{search.get()}'

        for i, v in enumerate(dictionary[s], 1):
            text += f'\n\t{i}. {v}'

    else:
        text = 'Entry not found'

    ety_info['text'] = text


def update_search_results():
    global search_results
    sr = [w for w in dictionary if w.startswith(search.get().lower()) and search.get() != '']

    for idx, res in enumerate(sr):
        if res not in search_results.get(0, tk.END):
            search_results.insert(idx, res)

    for i, li in enumerate(search_results.get(0, tk.END)):
        if li not in sr:
            search_results.delete(i, i)

    root.after(1, update_search_results)


search_results.bind('<<ListboxSelect>>', sel_word)
search_box.grid(row=0, column=1)
search_button = tk.Button(root, text='Search', command=search_dict)
search_button.grid(row=0, column=2)
root.after(1, update_search_results)
root.mainloop()
