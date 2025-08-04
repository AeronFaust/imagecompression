import cv2
import matplotlib.pyplot as plt
import time

def upscale():
    # Read image
    orig = cv2.imread("./test/1_copy1.png")
    img = cv2.imread("./result/1_copy1.png")
    duration = [0] * 4

    # Test to see if it effects initialization
    # sr = cv2.dnn_superres.DnnSuperResImpl_create()
    # path = "EDSR_x4.pb"
    # sr.readModel(path)
    # sr.setModel("edsr",4)
    # throwaway = sr.upsample(img)

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = "EDSR_x4.pb"
    sr.readModel(path)
    sr.setModel("edsr",4)
    start = time.time()
    edsr_result = sr.upsample(img)
    duration[0] = time.time() - start

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = "ESPCN_x4.pb"
    sr.readModel(path)
    sr.setModel("espcn",4)
    start = time.time()
    espcn_result = sr.upsample(img)
    duration[1] = time.time() - start

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = "FSRCNN_x4.pb"
    sr.readModel(path)
    sr.setModel("fsrcnn",4)
    start = time.time()
    fsrcnn_result = sr.upsample(img)
    duration[2] = time.time() - start

    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = "LapSRN_x4.pb"
    sr.readModel(path)
    sr.setModel("lapsrn",4)
    start = time.time()
    lapsrn_result = sr.upsample(img)
    duration[3] = time.time() - start


    plt.figure(figsize=(16,12))
    # Original images
    plt.subplot(3,2,1)
    plt.imshow(orig[:,:,::-1])
    plt.title("Original Image")
    plt.subplot(3,2,2)
    plt.imshow(img[:,:,::-1])
    plt.title("Downsized Image")

    # SR upscaled
    plt.subplot(3,2,3)
    plt.imshow(edsr_result[:,:,::-1])
    plt.title("EDSR Upscaled Image")

    plt.subplot(3,2,4)
    plt.imshow(espcn_result[:,:,::-1])
    plt.title("ESPCN Upscaled Image")

    plt.subplot(3,2,5)
    plt.imshow(fsrcnn_result[:,:,::-1])
    plt.title("FSRCNN Upscaled Image")

    plt.subplot(3,2,6)
    plt.imshow(lapsrn_result[:,:,::-1])
    plt.title("LapSRN Upscaled Image")

    plt.show()


    print("\n--- Time Complexities ---")
    print(f"EDSR Upscaled Image  : {duration[0]:.5f} seconds")
    print(f"ESPCN Upscaled Image : {duration[1]:.5f} seconds")
    print(f"FSRCNN Upscaled Image: {duration[2]:.5f} seconds")
    print(f"LapSRN Upscaled Image: {duration[3]:.5f} seconds")