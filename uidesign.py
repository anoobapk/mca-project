import tkinter as tk

class VirtualTryOnUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Try On Clothes")

        # Set the background image
        self.background_image = tk.PhotoImage(file="UID.png")
        background_label = tk.Label(self.root, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Create a label for the title
        title_label = tk.Label(self.root, text="Virtual Try On Clothes", font=("Arial", 18))
        title_label.pack(pady=10)
        
        # Create a label for the image
        image_label = tk.Label(self.root, text="Pic Your Image", font=("Arial", 12))
        image_label.pack(pady=10)
        
        # Create a button for uploading an image
        upload_button = tk.Button(self.root, text="Upload Image")
        upload_button.pack(pady=10)

        # Create a label for displaying the uploaded image
        self.uploaded_image = None
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)
        
        # Create a label for the clothes
        clothes_label = tk.Label(self.root, text="Clothes", font=("Arial", 12))
        clothes_label.pack(pady=10)
        
        # Create a listbox for selecting clothes
        clothes_listbox = tk.Listbox(self.root)
        clothes_listbox.insert(1, "T-Shirt")
        clothes_listbox.insert(2, "Pants")
        clothes_listbox.insert(3, "Dress")
        clothes_listbox.pack(pady=10)
        
        # Create a button for trying on clothes
        tryon_button = tk.Button(self.root, text="Try On Clothes")
        tryon_button.pack(pady=30)
        
        # Run the main loop
        self.root.mainloop()

        def upload_image(self):
        # Open a file dialog to select an image file
         file_path = tk.filedialog.askopenfilename()
        
        # If a file was selected, load the image and display it
        if file_path:
            self.uploaded_image = tk.PhotoImage(file=file_path)
            self.image_label.configure(image=self.uploaded_image)

# Create an instance of the VirtualTryOnUI class
virtual_try_on_ui = VirtualTryOnUI()
