from moviepy.editor import *

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', type=str,
                    help='input')
parser.add_argument('-audio', type=str,
                    help='audio')
parser.add_argument('-o', type=str,
                    help='output')

args = parser.parse_args()


clip = VideoFileClip(args.i)

# loading audio file
audioclip = AudioFileClip(args.audio, fps=24000)

# adding audio to the video clip
videoclip = clip.set_audio(audioclip)
  
videoclip.write_videofile(args.o)