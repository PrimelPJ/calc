import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get().replace("÷", "/").replace("×", "*")
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "AC":
        entry.delete(0, tk.END)
    elif text == "+/-":
        try:
            current = entry.get()
            if current.startswith("-"):
                entry.delete(0)
                entry.insert(0, current[1:])
            elif current != "":
                entry.delete(0, tk.END)
                entry.insert(0, "-" + current)
        except Exception:
            pass
    elif text == "%":
        try:
            current = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(current / 100))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="white")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify="right", bg="white", fg="black", insertbackground="black")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

button_frame = tk.Frame(root, bg="white")
button_frame.pack(expand=True, fill="both")

buttons = [
    ['AC', '+/-', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]

for r, row in enumerate(buttons):
    c = 0
    while c < len(row):
        btn_text = row[c]
        if btn_text == '':
            c += 1
            continue

        bg_color = "white"
        if btn_text in ['0','1','2','3','4','5','6','7','8','9','.']:
            fg_color = "black"
        else:
            fg_color = "white"

        btn = tk.Button(button_frame, text=btn_text, font="Arial 18", relief=tk.GROOVE,
                        border=0, bg=bg_color, fg=fg_color)

        if btn_text == '0':
            btn.grid(row=r, column=c, columnspan=2, sticky="nsew")
            button_frame.grid_columnconfigure(c, weight=1)
            button_frame.grid_columnconfigure(c+1, weight=1)
            c += 2
        else:
            btn.grid(row=r, column=c, sticky="nsew")
            button_frame.grid_columnconfigure(c, weight=1)
            c += 1

        button_frame.grid_rowconfigure(r, weight=1)
        btn.bind("<Button-1>", click)

root.mainloop()