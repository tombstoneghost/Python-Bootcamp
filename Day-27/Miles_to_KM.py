# Imports
from tkinter import *

# Miles to Kilometer Convertor
def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    kilometer_result_label.config(text="{:.2f}".format(km))

# Tkinter Window
window = Tk()
window.title("Miles to Kilometer Convertor")
window.config(padx=20, pady=20)

# Widgets
miles_input = Entry(width=7)
miles_label = Label(text="Miles")
is_equal_label = Label(text="is equal to")
kilometer_result_label = Label(text="0")
kilometer_label = Label(text="Km")
calculate_button = Button(text="Calculate", command=miles_to_km)


# Layout the Widgets
miles_input.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
kilometer_result_label.grid(column=1, row=1)
kilometer_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)


window.mainloop()
