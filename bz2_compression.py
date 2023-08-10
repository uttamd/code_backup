import bz2
import os
import sys

os.chdir(r"C:\Users\deepak.uttam\Documents\backup\input_files")
print(os.getcwd())
filename_in = "202205-divvy-tripdata_data.csv"
filename_out = filename_in+"_compressed.bz2"


def compress_bz2(filename_in,filename_out):
    with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
        fout.write(fin.read())

   
def decompressed_bz2(filename_out):
    with bz2.open(filename_out, "rb") as fin:
        data = fin.read()
        print(f"Decompressed size: {sys.getsizeof(data)}")


def size_redunction(filename_in, filename_out):
    input_file_size = os.stat(filename_in).st_size
    output_file_size = os.stat(filename_out).st_size
    redunction_percentage = (1 - output_file_size/input_file_size )*100
    print(f"Uncompressed size: {os.stat(filename_in).st_size}")
    print(f"Compressed size: {os.stat(filename_out).st_size}")
    print(f"Compressed size: {redunction_percentage}" )


compress_bz2(filename_in,filename_out)