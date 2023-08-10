import zlib
import sys
import os


os.chdir(r"C:\Users\deepak.uttam\Documents\backup\input_files")
print(os.getcwd())
filename_in = "202205-divvy-tripdata_data.csv"
filename_out = filename_in+"_compressed_data"

with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
    data = fin.read()
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    print(f"Original size: {sys.getsizeof(data)}")
    print(f"Compressed size: {sys.getsizeof(compressed_data)}")
    fout.write(compressed_data)

with open(filename_out, mode="rb") as fin:
    data = fin.read()
    compressed_data = zlib.decompress(data)



def size_redunction(filename_in, filename_out):
    input_file_size = os.path.getsize(filename_in)
    output_file_size = os.path.getsize(filename_out)
    redunction_percentage = (1 - output_file_size/input_file_size )*100
    print(f"Compressed size: {sys.getsizeof(data)}")
    print(f"Decompressed size: {sys.getsizeof(compressed_data)}")
    print(f"reduction percentage". redunction_percentage)

size_redunction(filename_in, filename_out)