import argparse
import os

from utils.prompt_making import make_prompt
from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--audio-prompt",
        type=str,
        default="",
    )
    parser.add_argument(
        "--text-prompt",
        type=str,
        default="",
    )
    parser.add_argument(
        "--target-text",
        type=str,
        default="",
    )
    parser.add_argument(
        "--out",
        type=str,
        default="",
    )

    return parser.parse_args()


def convert(audio_prompt, text_prompt, target_text, out):
    dirname = os.path.dirname(__file__) 
    text_english = make_prompt(name="temp", audio_prompt_path=audio_prompt, transcript=text_prompt)

    preload_models()

    print(target_text)

    audio_array = generate_audio(target_text if target_text != "" else text_english, prompt="temp")
    write_wav(out, SAMPLE_RATE, audio_array)

    filename = os.path.join(dirname, 'customs/temp.npz') 
    os.remove(filename)


if __name__ == "__main__":    
    args = get_args()
    convert(args.audio_prompt, args.text_prompt, args.target_text, args.out)
    