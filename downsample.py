import os
from PIL import Image

def downsample_images(input_dir, output_dir, max_size=(800, 800), quality=85, fmt="JPEG"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                with Image.open(input_path) as img:
                    img.thumbnail(max_size, Image.LANCZOS)

                    save_kwargs = {"optimize": True}

                    if fmt.upper() == "JPEG":
                        img = img.convert("RGB")
                        save_kwargs["quality"] = quality

                    elif fmt.upper() == "PNG":
                        img = img.convert("RGB").quantize(colors=256)

                    img.save(output_path, fmt, **save_kwargs)
                    print(f"Resized and saved: {output_path}")
            except Exception as e:
                print(f"Error with {filename}: {e}")
