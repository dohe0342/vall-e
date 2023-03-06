import glob
import os

libritts = sorted(glob.glob('/home/work/workspace/LibriSpeech/tts/LibriTTS/train-*'))

for train_subset in libritts:
    subset = sorted(glob.glob(f'{train_subset}/*'))
    for spk in subset:
        books = sorted(glob.glob(f'{spk}/*'))
        for book in books:
            files = sorted(glob.glob(f'{book}/*'))
            for f in files:
                if 'wav' in f:
                    os.system(f'ln -s {f} ./')
                if 'norm' in f:
                    os.system(f'ln -s {f} ./')
                exit()
