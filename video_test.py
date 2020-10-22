import os
import sys
from subprocess import Popen

_movie_default = "/home/pi/videos/##MOVIE_NAME.mp4"

playing = False

def main():
    while(True):
        if (not playing):
            omxc = Popen(['omxplayer', '-b', _movie_default])
            player = True

main()