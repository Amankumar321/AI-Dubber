from moviepy.editor import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', type=str,
                    help='input')

parser.add_argument('-o', type=str,
                    help='output')

args = parser.parse_args()

clip = VideoFileClip(args.i)

audioclip = clip.audio
audioclip.write_audiofile(args.o, fps=24000)