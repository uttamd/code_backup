import lzma
import os
import time

os.chdir(r"C:\Users\deepak.uttam\Documents\backup\lzma")
print(os.getcwd())

start_time = time.perf_counter()

def compression_bz2(filename_in,output_file):
    # Initialize the lzma.LZMACompressor
    compressor = lzma.LZMACompressor()
    # Open the input and output files
    with open(filename_in, "rb") as infile, open(output_file, "wb") as outfile:
        while True:
            chunk = infile.read(8192)  # Read a chunk of data (adjustable)
            if not chunk:
                break
            compressed_chunk = compressor.compress(chunk)
            if compressed_chunk:
                outfile.write(compressed_chunk)

    # Flush any remaining compressed data
        outfile.write(compressor.flush())
    print("File compression complete.")


def size_redunction_compression(filename_in, output_file):
    input_file_size = os.stat(filename_in).st_size
    output_file_size = os.stat(output_file).st_size
    redunction_percentage = (1 - output_file_size/input_file_size )*100
    print(f"Uncompressed size: {os.stat(filename_in).st_size}")
    print(f"Compressed size: {os.stat(output_file).st_size}")
    print(f"Size reduction : {redunction_percentage}" )





def decompression_bz2(filename_in,output_file):
    decompressor = lzma.LZMADecompressor()
    with open(filename_in, "rb") as infile, open(output_file, "wb") as outfile:
        while True:
            chunk = infile.read(8192)  # Read a chunk of compressed data (adjustable)
            if not chunk:
                break
            decompressed_chunk = decompressor.decompress(chunk)
            if decompressed_chunk:
                outfile.write(decompressed_chunk)
    print("File decompression complete.")




# Input CSV file path
filename_in = "recipes_data_data.csv"
# Output compressed file path
output_file = "recipes_data_data_compress_testing.xz"
## Compressing file and calculating the size
compression_bz2(filename_in,output_file)
size_redunction_compression(filename_in,output_file)

# Input bz2 path
filename_in = "recipes_data_data_compress_testing.xz"
# Output csv file
output_file = "recipes_data_data_decompress_testing.csv"
# decompressing the files
decompression_bz2(filename_in,output_file)

## total time taken
end_time = time.perf_counter()
print("total time taken in execution in secs", round((end_time-start_time) , 2))
