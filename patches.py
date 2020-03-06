# Inspired by https://stackoverflow.com/questions/53501331/crop-entire-image-with-the-same-cropping-size-with-pil-in-python and https://stackoverflow.com/questions/5953373/how-to-split-image-into-multiple-pieces-in-python

# Import needed libraries
import os
import glob
from PIL import Image
Image.MAX_IMAGE_PIXELS = None # to avoid image size warning

# Set image locations
imgdir = "E:\Panobatches\Mapillarytest"

# if you want file of a specific extension (.jpg):
filelist = [f for f in glob.glob(imgdir + "**/*.jpg", recursive=True)]
# Save directory
savedir = "E:\Panobatches\Mapillarytest\mapillaryoutput"

# Of which point should the patching start
start_pos = start_x, start_y = (0, 0)
# Image size
cropped_image_size = w, h = (832, 832)

# For each image on image list, open, set size
for file in filelist:
    img = Image.open(file)
    width, height = img.size

    frame_num = 1
    for col_i in range(0, width, w):
        for row_i in range(0, height, h):
            crop = img.crop((col_i, row_i, col_i + w, row_i + h))
            name = os.path.basename(file)
            name = os.path.splitext(name)[0]
            save_to= os.path.join(savedir, name+"_{:03}.jpg")
            crop.save(save_to.format(frame_num))
            frame_num += 1
