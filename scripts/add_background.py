from pydub import AudioSegment
from parsesrt import parse
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-convert', type=str,
                    help='input')
parser.add_argument('-srt', type=str,
                    help='subtitles')
parser.add_argument('-original', type=str,
                    help='original')
parser.add_argument('-combine', type=str,
                    help='combined')
parser.add_argument('-background', type=str,
                    help='background sound')
parser.add_argument('-o', type=str,
                    help='output')

args = parser.parse_args()

def getTime(st:str,idx:int)->int:
    a=st.split(" --> ")[idx]
    hh=int(a.split(":")[0])
    mm=int(a.split(":")[1])
    ss=int(a.split(":")[2].replace(",",""))
    # print(hh,mm,ss)
    totalmillisecs=hh*60*60*1000+mm*60*1000+ss
    return totalmillisecs/1000

parts = []

original = AudioSegment.from_file(args.original)

lines, timestamps = parse(args.srt)

audio1 = AudioSegment.from_file(args.combine) #your first audio file
audio2 = AudioSegment.from_file(args.background) #your second audio file

# currTime = 0
# i = 0

# while 1:
#     diff = currTime - original.duration_seconds
#     if diff < 0.0001 and diff > -0.0001:
#         break

#     if i >= len(timestamps):
#         break

#     #print(currTime, getTime(timestamps[i + 1], 0))
#     if len(timestamps) > i  and currTime >= getTime(timestamps[i + 1], 0):
#         path = args.convert + '/' + str(i) + '.wav'
#         length = AudioSegment.from_wav(path).duration_seconds
#         end = max(getTime(timestamps[i + 1], 0)*1000 + length*1000, getTime(timestamps[i + 1], 1)*1000)
#         part = audio1[getTime(timestamps[i + 1], 0)*1000 : end]
#         part_bg = audio2[getTime(timestamps[i + 1], 0)*1000 : end]
#         mixed = part.overlay(part_bg)  

#         parts.append(mixed)
#         currTime = currTime + part.duration_seconds

#     else :
#         if len(timestamps) > i :
#             end = getTime(timestamps[i + 1], 0)
#         else :
#             end = original.duration_seconds
#         part = original[currTime*1000 : end*1000]
#         parts.append(part)
#         currTime = currTime + part.duration_seconds
#         i = i - 1

#     i = i + 1
        

# mixed_combined = AudioSegment.silent(0)

# for part in parts :
#     mixed_combined += part


audio1 = audio1 + AudioSegment.silent((audio2.duration_seconds - audio1.duration_seconds)*1000, frame_rate=24000)
mixed_combined = audio1.overlay(audio2)

mixed_combined.export(args.o, format='wav') #export mixed  audio file 


