import glob
import os
from tqdm import tqdm

libritts = sorted(glob.glob('/home/work/workspace/LibriSpeech/tts/LibriTTS/train-clean-360'))

for train_subset in tqdm(libritts):
    print(train_subset)
    subset = sorted(glob.glob(f'{train_subset}/*'))
    for spk in tqdm(subset, leave=False):
        books = sorted(glob.glob(f'{spk}/*'))
        for book in tqdm(books, leave=False):
            files = sorted(glob.glob(f'{book}/*'))
            for f in tqdm(files, leave=False):
                if 'wav' in f:
                    os.system(f'ln -s {f} ./')
                if 'norm' in f:
                    os.system(f'ln -s {f} ./')
