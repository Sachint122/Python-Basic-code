import tkinter as tk

def button_click():
    label.config(text="Button clicked!")

# Create the main window
root = tk.Tk()
root.title("My Application")

# Create a label
label = tk.Label(root, text="Hello, world!")
label.pack()

# Create a button
button = tk.Button(root, text="Click me", command=button_click)
button.pack()

# Run the main event loop
root.mainloop()
