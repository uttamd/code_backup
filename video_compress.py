import ffmpeg
import os
import time 

# start time
start_time = time.perf_counter()

os.chdir(r"C:\Users\deepak.uttam\Documents\video")
print(os.getcwd())

input_file = 'V360_Awards_2023_Winner_Highlights.mp4'
output_file_h264 = 'output_compressed_h264.mp4'
output_file_h265 = 'output_compressed_h265.mp4'

def compress_video(input_file,output_file_h264):
    try:
        # Compress using H.264 codec
        ffmpeg.input(input_file).output(output_file_h264, vcodec='libx264', crf=23).run()

        # Compress using H.265 (HEVC) codec
        # ffmpeg.input(input_file).output(output_file_h265, vcodec='libx265', crf=28).run()
    except Exception as e:
        print("exception occured ! ",e)

def size_reduction(input_file, outputfile):
    try:
        input_size = os.stat(input_file).st_size
        output_size = os.stat(outputfile).st_size
        size_reduction_per = (1- output_size/input_size)*100
        print(f"input file_name and size ->{input_file} , {input_size}")
        print(f"output file_name and size ->{outputfile} , {output_size}")
        print(f"reduction percentage -> {size_reduction_per} %")
    except Exception as e :
        print("exception occured ",e)


if __name__ == "__main__":
    compress_video(input_file,output_file_h264)
    size_reduction(input_file,output_file_h264)

# end time
end_time = time.perf_counter()
print("time taken in conversion in secs", round((end_time-start_time),2))
