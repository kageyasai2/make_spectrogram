import os
import sys
from pydub import AudioSegment

def exists_music_file_into_directory(music_file_name):
    if not os.path.isfile(music_file_name):
      print("file name don't exists directory")
      sys.exit()

def input_music_file():
    music_file_name = input('select music file name:')
    exists_music_file_into_directory(music_file_name)


def main():
    input_music_file()

if __name__ == '__main__':
    main()