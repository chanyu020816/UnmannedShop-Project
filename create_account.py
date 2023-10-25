import tkinter as tk
from tkinter import messagebox

def submit():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    birth = birth_entry.get()
    sex = sex_var.get()

    if password == confirm_password:
        # You can save the user's information here
        messagebox.showinfo("Success", "Account created successfully!")
    else:
        messagebox.showerror("Error", "Password and Confirm Password do not match.")

# Create the main window
root = tk.Tk()
root.title("Account Creation")

# Create labels and entry fields for user input
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Use show="*" to hide the password
password_entry.pack()

confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack()

birth_label = tk.Label(root, text="Birth:")
birth_label.pack()
birth_entry = tk.Entry(root)
birth_entry.pack()

sex_label = tk.Label(root, text="Sex:")
sex_label.pack()
sex_var = tk.StringVar()
sex_var.set("Male")  # Default value
male_radio = tk.Radiobutton(root, text="Male", variable=sex_var, value="Male")
female_radio = tk.Radiobutton(root, text="Female", variable=sex_var, value="Female")
male_radio.pack()
female_radio.pack()

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Start the main loop
root.mainloop()

