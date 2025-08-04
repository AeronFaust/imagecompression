def bits_to_png(input=None, output_path=None):
    if input:
        with open(input, "rb") as f:
            image_bytes = f.read()

    else:
        raise ValueError("Invalid input.")

    with open(output_path, "wb") as f:
        f.write(image_bytes)

    print(f"PNG image restored to {output_path}")

if __name__ == "__main__":
    bits_to_png(input="image_bits.bin",output_path="./result/restored.png") 