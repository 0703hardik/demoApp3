from PIL import Image

im1 = Image.open('input.jpeg')     # Input file
im1.save('output.png')             # Output file
print("Conversion done: output.png created")
