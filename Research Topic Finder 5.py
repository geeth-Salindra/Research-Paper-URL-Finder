import tkinter as tk
from tkinter import messagebox
import requests
from urllib.parse import urlencode


def get_url():
    title = title_entry.get()
    authors = authors_entry.get()
    journal = journal_entry.get()

    query = f"{title} {authors} {journal}"
    params = {'query': query}
    url = f"https://api.crossref.org/works?{urlencode(params)}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["message"]["items"]:
            paper = data["message"]["items"][0]
            if "URL" in paper:
                pub_url = paper["URL"]
                url_text.delete(1.0, tk.END)
                url_text.insert(tk.END, pub_url)
            else:
                messagebox.showinfo("URL Not Found", "No URL found for the provided details.")
        else:
            messagebox.showinfo("No Results", "No results found for the provided details.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Research Paper URL Finder")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Title:")
title_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
title_entry = tk.Entry(root, width=40)
title_entry.grid(row=0, column=1, padx=10, pady=5)

# Authors
authors_label = tk.Label(root, text="Authors:")
authors_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
authors_entry = tk.Entry(root, width=40)
authors_entry.grid(row=1, column=1, padx=10, pady=5)

# Journal
journal_label = tk.Label(root, text="Journal:")
journal_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
journal_entry = tk.Entry(root, width=40)
journal_entry.grid(row=2, column=1, padx=10, pady=5)

# URL text box
url_text_label = tk.Label(root, text="URL:")
url_text_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
url_text = tk.Text(root, width=30, height=1)
url_text.grid(row=3, column=1, padx=10, pady=5)

search_button = tk.Button(root, text="Search", command=get_url)
search_button.grid(row=4, column=0, columnspan=2, padx=50, pady=10, sticky="e")
search_button.config(height=1, width=10)

root.grid_rowconfigure(4, weight=1)

root.mainloop()
