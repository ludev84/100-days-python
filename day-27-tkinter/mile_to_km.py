import tkinter


def miles_to_km():
    miles = float(miles_input.get())
    result = round(miles * 1.609344, 2)
    result_label.config(text=f"{result}")


window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=7)
miles_input.insert(tkinter.END, string="0")
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=20, pady=10)

result_label = tkinter.Label(text="0")
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
