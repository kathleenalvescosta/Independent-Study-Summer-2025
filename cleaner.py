import os
import pandas as pd
import re
import unicodedata
import librosa
import soundfile as sf
from tqdm import tqdm

inputtxt = "/groups/rhenderson/kathleencosta/cv-corpus-21.0-2025-03-14/en/validated.tsv"              
inputwav = "/groups/rhenderson/kathleencosta/cv-corpus-21.0-2025-03-14/en/clips/"             
outputwav = "/groups/rhenderson/kathleencosta/wavs/"              
outputtxt = "metadata.csv"    
hz = 44100                    

os.makedirs(outputwav, exist_ok=True)

def normalize(text):
    text = text.lower()
    text = unicodedata.normalize("NFKC", text) #Normalizes the text to NFKC unicode standard
    text = re.sub(r"[^a-z0-9\s.,?!'-]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df = pd.read_csv(inputtxt, sep="\t")

with open(outputtxt, "w", encoding="utf-8") as fout:
    for _, row in tqdm(df.iterrows(), total=len(df)):
        try:
            wavfile = row["path"]
            text = row["sentence"]
            if not isinstance(text, str) or not isinstance(wavfile, str):
                continue
            if len(text.strip()) < 5:
                continue

            wavpath = os.path.join(inputwav, wavfile)
            if not os.path.exists(wavpath):
                continue

            y, sr = librosa.load(wavpath, sr=None)
            yt, _ = librosa.effects.trim(y, top_db=30) #Trims leading and trailing silence; detects anything us under 30 decibels as silence

            outputpath = os.path.join(outputwav, os.path.splitext(wavfile)[0] + ".wav")
            sf.write(outputpath, yt, sr)

            normalizedtext = normalize(text)
            fout.write(f"{outputpath}|{normalizedtext}\n")

        except Exception as e:
            print(f"Error with {wavfile}: {e}")