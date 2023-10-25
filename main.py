import tkinter as tk

def show_selection():
    # Get the selected sex
    selected_sex = var.get()
    print(f'Selected sex: {selected_sex}')

# Create the main window
root = tk.Tk()
root.title("Sex Selection")

# Create a StringVar to hold the selected sex
var = tk.StringVar()

# Create the label for the sex selection
sex_label = tk.Label(root, text="Select your sex:")
sex_label.pack()

# Create Male and Female radio buttons
male_radio = tk.Radiobutton(root, text="Male", variable=var, value="Male")
female_radio = tk.Radiobutton(root, text="Female", variable=var, value="Female")

male_radio.pack()
female_radio.pack()

# Create a button to display the selected sex
show_button = tk.Button(root, text="Show Selection", command=show_selection)
show_button.pack()

root.mainloop()
