# Image Converter Script

## Overview
This Python script provides a graphical user interface (GUI) for converting both single images and in bulk in a specified input directory to JPEG format with the option to resize them. It utilizes the Tkinter library for the GUI, the PIL (Pillow) library for image processing, and allows you to select both input and output directories along with the desired output size.

## Requirements
- Python 3.x
- Tkinter library
- Pillow (PIL) library

## Usage

1. **Select Input Directory:** Click the "Select" button next to "Input Directory" to choose the folder containing the images you want to convert.

2. **Select Output Directory:** Click the "Select" button next to "Output Directory" to specify where the converted images should be saved.

3. **Set Output Size:** Enter the desired output size in the "Output Size (Width x Height)" field. The images will be resized proportionally to fit within these dimensions.

4. **Convert Images:** Click the "Convert Images" button to start the conversion process. The script will resize and convert all images in the input directory to JPEG format and save them in the output directory.

## Script Execution

The script uses a graphical interface to simplify the image conversion process:

- It creates a GUI window titled "Image Converter" where you can interact with the script.

- The input and output directories are selected using file dialogs, ensuring user-friendly input.

- You can specify the desired output image size in the format "Width x Height" (e.g., "800x600"). The images will be proportionally resized to fit within these dimensions.

- When you click the "Convert Images" button, the script processes the images in the input directory, resizes them, and saves the converted images in the specified output directory.

- Progress and error messages are displayed in the console.

## Troubleshooting

- If you encounter any errors during the conversion process, the script will display an error message in the console, providing information about the issue.

## Note

- Make sure to install the required Python libraries (`tkinter` and `Pillow`) before running the script.

- The script performs image resizing using the Lanczos resampling algorithm for high-quality results.

- The default JPEG quality is set to 90, which provides a good balance between image quality and file size. You can adjust this value in the `img.save` function if needed.

- The script does not modify the original image files in the input directory; it creates new JPEG copies in the output directory.

- Always make sure to have backups of your original images before running batch conversion processes.

## Author
[okiromosh](github.com/okiromosh)

## License
This script is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.
