import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image


def select_input_directory():
    input_directory = filedialog.askdirectory()
    input_directory_entry.delete(0, tk.END)
    input_directory_entry.insert(0, input_directory)


def select_output_directory():
    output_directory = filedialog.askdirectory()
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, output_directory)


def convert_images(input_dir, output_dir, output_size):
    try:
        for filename in os.listdir(input_dir):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image.open(input_path) as img:
                img.thumbnail(output_size, Image.LANCZOS)
                img.save(output_path, "JPEG", quality=90, optimize=True)
                print(f"Processed: {input_path}")
        print("Conversion completed.")
    except Exception as e:
        print(f"Error: {str(e)}")


window = tk.Tk()
window.title("Image Converter")

# Create and organize frames for better layout
input_frame = tk.Frame(window)
input_frame.pack(pady=10)
output_frame = tk.Frame(window)
output_frame.pack(pady=10)
size_frame = tk.Frame(window)
size_frame.pack(pady=10)
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Input Directory Section
input_label = tk.Label(input_frame, text="Input Directory:")
input_label.pack(side=tk.LEFT)
input_directory_entry = tk.Entry(input_frame)
input_directory_entry.pack(side=tk.LEFT, padx=10)
input_button = tk.Button(input_frame, text="Select", command=select_input_directory)
input_button.pack(side=tk.LEFT)

# Output Directory Section
output_label = tk.Label(output_frame, text="Output Directory:")
output_label.pack(side=tk.LEFT)
output_directory_entry = tk.Entry(output_frame)
output_directory_entry.pack(side=tk.LEFT, padx=10)
output_button = tk.Button(output_frame, text="Select", command=select_output_directory)
output_button.pack(side=tk.LEFT)

# Output Size Section
size_label = tk.Label(size_frame, text="Output Size (Width x Height):")
size_label.pack(side=tk.LEFT)
size_entry = tk.Entry(size_frame)
size_entry.pack(side=tk.LEFT, padx=10)
size_entry.insert(0, "800x600")

# Convert Button
convert_button = tk.Button(button_frame, text="Convert Images", command=lambda: convert_images(
    input_directory_entry.get(), output_directory_entry.get(), tuple(map(int, size_entry.get().split("x")))
))
convert_button.pack()

window.mainloop()
