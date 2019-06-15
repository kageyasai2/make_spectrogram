import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

def exists_music_file_into_directory(music_file_name):
    if not os.path.isfile(music_file_name):
      print("file name don't exists directory")
      sys.exit()

def input_music_file():
    music_file_name = input('select music file name:')
    exists_music_file_into_directory(music_file_name)

    return music_file_name

def make_graph_music_data(music_file_name):
    tmp_music_data = AudioSegment.from_mp3(music_file_name)
    music_frame_rate = tmp_music_data.frame_rate
    music_datas = np.array(tmp_music_data.get_array_of_samples())

    return music_datas,music_frame_rate

def make_spectrum_graph(music_datas,music_frame_rate):
    pxx, freq, bins, t = plt.specgram(music_datas,Fs=music_frame_rate)
    plt.show()

def main():
    music_file_name = input_music_file()
    music_datas ,music_frame_rate= make_graph_music_data(music_file_name)
    make_spectrum_graph(music_datas,music_frame_rate)

if __name__ == '__main__':
    main()