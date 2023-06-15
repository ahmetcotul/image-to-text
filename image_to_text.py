import pytesseract
from PIL import Image
import sys

# take argument
image_path = sys.argv[1] if len(sys.argv) > 1 else None 

# check argument
if image_path is None:
    print("File not specified. Please provide the image file path as an argument.If you don't know anything, write \"help\" as parameter")
    sys.exit()

# check if help is requested
if image_path.lower() == "help":
    print("Usage: python3 script.py [image_path]")
    print("image_path: The path to the image file you want to extract text from.")
    sys.exit()

# open image
try:
    image = Image.open(image_path)
except IOError:
    print("Invalid file path or file format")
    sys.exit()

# Convert image to text with OCR
text = pytesseract.image_to_string(image)

# save text to file
def write_to_file(file_path, data):
    # open file and keep in write mode
    with open(file_path, 'w') as file:
        # write data to file
        file.write(data)
    # Automatically saved after closing the file

# the path to save the file
file_path = "/path/to/file.txt"

# write data to file function
write_to_file(file_path, text)

# print text
print(text)
