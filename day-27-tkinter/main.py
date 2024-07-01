import tkinter


def button_clicked():
    # my_label["text"] = "Button clicked"
    my_label.config(text=my_input.get())


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

new_button = tkinter.Button(text="New button", command=button_clicked)
new_button.grid(column=2, row=0)

my_input = tkinter.Entry(width=10)
my_input.grid(column=3, row=2)

window.mainloop()
