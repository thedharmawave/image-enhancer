import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance

# Function to load an image
def load_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp")]
    )
    if file_path:
        try:
            img = Image.open(file_path)
            enhance_image(img)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")

# Function to enhance the image
def enhance_image(img):
    # Enhance sharpness as an example
    enhancer = ImageEnhance.Sharpness(img)
    enhanced_img = enhancer.enhance(2.0)  # Increase sharpness

    # Save the enhanced image
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        try:
            enhanced_img.save(save_path)
            messagebox.showinfo("Success", "Image enhanced and saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {e}")

# Set up the tkinter UI
def setup_ui():
    root = tk.Tk()
    root.title("Image Enhancer")

    load_button = tk.Button(root, text="Load Image", command=load_image)
    load_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    setup_ui()
