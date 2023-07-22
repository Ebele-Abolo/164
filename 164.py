from tkinter import filedialog
root.configure(background = "black")
label_image = Label(root, bg="white", highlightthickness=5)
img_path = filedialog.askopenfiledialog.askopenfilename(title = " Open Text File", filetypes= ["Image Files", "*.jpg;*.gif;*.jpg;;*.png;*txt"])