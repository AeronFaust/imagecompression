import os
import shutil
import time
from downsample import downsample_images
from populate import populate_folder

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

if __name__ == '__main__':
    input="test"
    output="result"

    if os.path.exists(output):
        shutil.rmtree(output)

    populate_folder('./images', './test', 60, shuffle=True)

    start = time.time()

    # Running downsample
    downsample_images(
        input_dir = input,
        output_dir = output,
        max_size=(180, 180),
        quality=100,
        fmt="JPEG" 
    )

    duration = time.time() - start

    size_in = get_folder_size(input) / (1024 * 1024)
    size_out = get_folder_size(output) / (1024 * 1024)

    file_count = sum(1 for f in os.listdir(output) if os.path.isfile(os.path.join(output, f)))

    print("\n--- Summary ---")
    print(f"Input image count           : {file_count:.2f} frames")
    print(f"Input folder size           : {size_in:.2f} MB")
    print(f"Output folder size          : {size_out:.2f} MB")
    print(f"Time taken                  : {duration:.2f} seconds")
    print(f"Compressed Frames Per Second: {file_count/duration:.2f} frames per seconds")