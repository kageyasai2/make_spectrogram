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
    music_datas = np.array(tmp_music_data.get_array_of_samples())
    print(len(music_datas))
    music_data = music_datas[:20000]
    plt.plot(music_data)
    plt.show()

    return music_data

def make_fourier_transform_graph(music_data):
    print(music_data)
    fft = np.fft.fft(music_data)
    print(type(fft))
    plt.plot(fft)
    plt.show()

def main():
    music_file_name = input_music_file()
    music_data = make_graph_music_data(music_file_name)
    make_fourier_transform_graph(music_data)

if __name__ == '__main__':
    main()