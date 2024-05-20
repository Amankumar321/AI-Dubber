from pydub import AudioSegment
from moviepy.editor import *
import os
import math
from parsesrt import parse
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', type=str,
                    help='input')
parser.add_argument('-srt', type=str,
                    help='subtitles')
parser.add_argument('-o', type=str,
                    help='output')
parser.add_argument('-original', type=str,
                    help='original')

args = parser.parse_args()
  
# loading video dsa gfg intro video
#clip = VideoFileClip("v.mp4")
def getTime(st:str,idx:int)->int:
    a=st.split(" --> ")[idx]
    hh=int(a.split(":")[0])
    mm=int(a.split(":")[1])
    ss=int(a.split(":")[2].replace(",",""))
    # print(hh,mm,ss)
    totalmillisecs=hh*60*60*1000+mm*60*1000+ss
    return totalmillisecs/1000

lines, timestamps = parse(args.srt)

original = AudioSegment.from_wav(args.original)
combined_sounds = AudioSegment.silent(duration=0, frame_rate=2400)

currTime = 0

files = [os.path.join(args.i, f) for f in os.listdir(os.path.join(args.i))]
files.sort()

if (len(files) > 0):
    start = 0
    end = getTime(timestamps[1], 0)
    silent = AudioSegment.silent(duration=(end - start) * 1000, frame_rate=24000)
    combined_sounds += silent
    currTime = end * 1000

for i, (key, time) in enumerate(timestamps.items()):
    segment = AudioSegment.from_wav(files[i])
    start = getTime(time, 0)
    end = getTime(time, 1)
    length = min((end - start) * 1000, segment.duration_seconds * 1000)
    segment = segment[: length]
    combined_sounds += segment
    currTime += length

    if (i != len(files) - 1):
        start = currTime / 1000
        end = getTime(timestamps[key + 1], 0)
        silent = AudioSegment.silent(duration=(end - start) * 1000, frame_rate=24000)
        combined_sounds += silent
        currTime = end * 1000

combined_sounds.export(args.o, format="wav")





        
