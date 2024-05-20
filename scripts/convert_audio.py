from parsesrt import parse
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-converter', type=str,
                    help='input')
parser.add_argument('-split', type=str,
                    help='input')
parser.add_argument('-srt', type=str,
                    help='subtitles')
parser.add_argument('-srt-converted', type=str,
                    help='subtitles')
parser.add_argument('-out', type=str,
                    help='output')

args = parser.parse_args()

files = [f for f in os.listdir(args.split)]
files.sort()
lines, timestamps = parse(args.srt)
lines_converted, timestamps_converted = parse(args.srt_converted)

for i, file in enumerate(files):
    out_file = os.path.join(args.out, f"{i}.wav")
    os.system(f'python {args.converter} --audio-prompt {os.path.join(args.split, file)} --target-text "{lines_converted[i+1]}" --out {out_file}')