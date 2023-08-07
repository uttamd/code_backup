from PIL import Image
import os
import sys
import time

# """
# Document -
# WebP
# Pillow reads and writes WebP files. The specifics of Pillow’s capabilities with this format are currently undocumented.
# Options - 
# Saving
# The save() method supports the following options:
# lossless
# If present and true, instructs the WebP writer to use lossless compression.
# quality
# Integer, 0-100, Defaults to 80. For lossy, 0 gives the smallest size and 100 the largest. For lossless, this parameter is the amount of effort put into the compression: 0 is the fastest, but gives larger files compared to the slowest, but best, 100.
# method
# Quality/speed trade-off (0=fast, 6=slower-better). Defaults to 4.
# exact
# If true, preserve the transparent RGB values. Otherwise, discard invisible RGB values for better compression. Defaults to false. Requires libwebp 0.5.0 or later.
# icc_profile
# The ICC Profile to include in the saved file. Only supported if the system WebP library was built with webpmux support.
# exif
# The exif data to include in the saved file. Only supported if the system WebP library was built with webpmux support.
# xmp
# The XMP data to include in the saved file. Only supported if the system WebP library was built with webpmux support.
# """
img_path = r"C:\Users\deepak.uttam\Documents\image"
os.chdir(img_path)
print(f"existing directory -> {os.getcwd()}")

start_time = time.perf_counter()

def webp_conversion(filename,path="images/"):
    try:
        extension = filename.split('.')[-1]
        fname = filename.split('.')[0]
        output_fname = 'converted_'+ fname
        img = Image.open(path + filename)

        if extension == "png":
            img.save((path+output_fname+".webp"), "webp", lossless=True,quality=50)
        elif extension == "jpg" or extension == "jpeg":
            img.save((path+output_fname+".webp"), "webp",  quality=80)
    except Exception:
        print("exception generated")

def convert_all(path=img_path+"\\"):
    try:
        for root, dirs, files in os.walk(path):
            for imagefile in files:
                if imagefile.endswith(".png") or imagefile.endswith(".jpg") or imagefile.endswith(".jpeg"):
                    webp_conversion(imagefile, os.path.join(root, ""))
        size_reduction(path)
    except Exception:
        print("Exception occured at convert_all function")

def size_reduction(path=img_path+"\\"):
    try:
        input_size =0
        input_files =[]
        output_size=0
        output_files =[]
        for root, dirs, files in os.walk(path):
            for imagefile in files:
                if imagefile.endswith(".png") or imagefile.endswith(".jpg") or imagefile.endswith(".jpeg"):
                    input_size += os.stat(imagefile).st_size
                    input_files.append(imagefile)
                elif imagefile.endswith('.webp'):
                    output_size += os.stat(imagefile).st_size
                    output_files.append(imagefile)
  
        size_reduction_per = (1- output_size/input_size)*100
        print(f"input file_name -> {input_files} and size->{input_size}")
        print(f"output file_name-> {output_files} and size->{output_size}")
        print(f"reduction percentage -> {size_reduction_per}")
    except Exception as e:
        print("exception occured at size reduction function",e)

if __name__ == "__main__":
    convert_all()
    end_time = time.perf_counter()
    print("time taken in secs->", round((end_time-start_time),2))



"""
Observation - 
lossless=True increases file_size for jpeg file 
quality controls the size of image , lesser the quality less the size 
"""
