from pydub import AudioSegment
import os
import time


"""
**export paramters***
format | example: "aif" | default: "mp3" Format of the output file. Supports "wav" and "raw" natively, requires ffmpeg for all other formats.
codec | example: "libvorbis" For formats that may contain content encoded with different codecs, you can specify the codec you'd like the encoder to use. For example, the "ogg" format is often used with the "libvorbis" codec. (requires ffmpeg)
bitrate | example: "128k" For compressed formats, you can pass the bitrate you'd like the encoder to use (requires ffmpeg). Each codec accepts different bitrate arguments so take a look at the ffmpeg documentation for details (bitrate usually shown as -b, -ba or -a:b).
tags | example: {"album": "1989", "artist": "Taylor Swift"} Allows you to supply media info tags for the encoder (requires ffmpeg). Not all formats can receive tags (mp3 can).
parameters | example: ["-ac", "2"] Pass additional command line parameters to the ffmpeg call. These are added to the end of the call (in the output file section).
id3v2_version | example: "3" | default: "4" Set the ID3v2 version used by ffmpeg to add tags to the output file. If you want Windows Exlorer to display tags, use "3" here (source).
cover | example: "/path/to/imgfile.png" Allows you to supply a cover image (path to the image file). Currently, only MP3 files allow this keyword argument. Cover image must be a jpeg, png, bmp, or tiff file.

"""
os.chdir(r"C:\Users\deepak.uttam\Documents\audio")

print(f"current working directoty -> {os.getcwd()}")

start_time = time.perf_counter()

def size_reduction(input_file, outputfile):
    input_size = os.stat(input_file).st_size
    output_size = os.stat(outputfile).st_size
    size_reduction_per = (1- output_size/input_size)*100
    print(f"input file_name and size ->{input_file} , {input_size}")
    print(f"output file_name and size ->{outputfile} , {output_size}")
    print(f"reduction percentage -> {size_reduction_per}")


def change_to_flac(file_name):
    audio = False
    fname = file_name.split('.')[0]
    f_format = file_name.split('.')[-1]
    output_file_name = 'converted_'+fname+'.flac'
    if f_format == 'mp3' :
        audio = AudioSegment.from_mp3(file_name)
    elif f_format =='wav':
        audio = AudioSegment.from_wav(file_name)
    elif f_format == 'ogg':
        audio = AudioSegment.from_ogg(file_name)
    if audio:
        audio.export(output_file_name,format='flac', bitrate= '128k')
    print(f"conversion completed for {file_name}!")
    size_reduction(file_name, output_file_name)



change_to_flac('file_example_OOG_5MG.ogg')
change_to_flac('euphoric-electric-groove-160306.mp3')
change_to_flac('file_example_WAV_10MG.wav')
change_to_flac('summer-walk-152722.mp3')

end_time = time.perf_counter()
print(f"Total time taken in secs", round((end_time-start_time),2))
