from PIL import Image
import numpy as np

# # Load the image
# img = Image.open("test.png")  # Replace "your_image.jpg" with your image file

# # Convert the PIL Image to a NumPy array
# img_array = np.array(img)

# # with open("output.txt", "w") as f:
# #     print(img_array, file=f)

# print(img_array.dtype)

def png_to_bits(input_path, output=None):
    with open(input_path, "rb") as f:
        image_bytes = f.read()

        with open(output, "wb") as f:
            f.write(image_bytes)

        print(f"Bits saved to {output}")

if __name__ == "__main__":
    png_to_bits("./result/1_copy1.png", output="./image_bits.bin")