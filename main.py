import json
import tkinter as tk

with open('dict.json') as d:
    dictionary: dict = json.load(d)

root = tk.Tk()


w = input('Search for a word: ').lower()

print(f"{w}")

for i, v in enumerate(dictionary[w], 1):
    print(f"\t{i}. {v}")
