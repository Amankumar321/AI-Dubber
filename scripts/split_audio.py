# Import everything needed to edit video clips
from moviepy.editor import *
from parsesrt import parse
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', type=str,
                    help='input')
parser.add_argument('-srt', type=str,
                    help='subtitles')
parser.add_argument('-o', type=str,
                    help='output')

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

clip = AudioFileClip(args.i, fps=24000)

lines, timestamps = parse(args.srt)

for i in range(len(timestamps)) :
    audioclip = clip.subclip(getTime(timestamps[i + 1], 0), min(getTime(timestamps[i + 1], 1), clip.duration))
    audioclip.write_audiofile(args.o + "/prompt{}.wav".format(i), fps=24000)