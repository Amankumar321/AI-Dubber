import os
import shutil

try:
    os.remove("./output/a.wav")
except:
    pass
try:
    os.remove("./output/combine.wav")
except:
    pass
try:
    os.remove("./output/mixed.wav")
except:
    pass

def clean_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

clean_folder('./output/convert_audio')
clean_folder('./output/final')
clean_folder('./output/split_audio')
clean_folder('./output/srt')
clean_folder('./output/vocal_remover')

