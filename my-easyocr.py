import easyocr
import os

# Initialize the reader
reader = easyocr.Reader(['de'])

# Path to the directory containing images
image_dir = 'project sources/Bookeye/images/boulevard'

# Iterate over all files in the directory
for image_file in os.listdir(image_dir):
    # Construct the full path to the image file
    image_path = os.path.join(image_dir, image_file)
    
    # Perform OCR on the image
    result = reader.readtext(image_path, detail=0)
    
    # Extract the base name of the image file without the extension
    base_name = os.path.splitext(image_file)[0]
    
    # Create a new file with the same base name and a .txt extension
    output_file = os.path.join(image_dir, f"{base_name}.txt")
    
    # Concatenate the detected text into a single passage
    passage = ' '.join(result)
    
    # Write the passage to the file
    with open(output_file, 'w') as file:
        file.write(passage)

# Print a message to indicate that the process is complete
print("OCR processing for file", base_name, "complete.")