import pyperclip
import pyshorteners
import tkinter as tk

root = tk.Tk()
root.geometry("450x250")
root.title("URL Shortener")
root.configure(bg="#2c3e50")

url = tk.StringVar()
url_address = tk.StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

tk.Label(root, text="Project URL Shortener", font="Times_New_Roman").pack(pady=10)
tk.Entry(root, textvariable=url).pack(pady=5)
tk.Button(root, text="Generate Short URL", command=urlshortener).pack(pady=7)
tk.Entry(root, textvariable=url_address).pack(pady=5)
tk.Button(root, text="Copy URL", command=copyurl).pack(pady=5)

root.mainloop()
