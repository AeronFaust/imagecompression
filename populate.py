import os
import shutil
import math

def populate_folder(source_folder, destination_folder, x):
    # Delete the destination folder and all its contents if it exists
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)

    # Recreate the empty destination folder
    os.makedirs(destination_folder, exist_ok=True)

    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}

    # Calculate padding width based on copies count
    padding = max(1, math.ceil(math.log10(x+1)))

    for filename in os.listdir(source_folder):
        name, ext = os.path.splitext(filename)
        if ext.lower() in image_extensions:
            source_path = os.path.join(source_folder, filename)

            for i in range(1, x + 1):
                new_filename = f"{name}_copy{i:0{padding}d}{ext}"
                destination_path = os.path.join(destination_folder, new_filename)
                shutil.copy2(source_path, destination_path)
                print(f"Copied {filename} → {new_filename}")