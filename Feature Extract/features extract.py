import os
import librosa
import numpy as np
import pandas as pd
from tqdm import tqdm

metadata = pd.read_csv("C:\\Users\\ILXYENILXY\\Desktop\\Sound-Classification\\esc50.csv")
audio_path = "C:\\Users\\ILXYENILXY\\Desktop\\Sound-Classification\\audio\\audio\\16000"

def extract_cqt(file):
    audio,sr=librosa.load(file_name, res_type='kaiser_fast')
    cqt = librosa.cqt(y=audio, sr=sr, hop_length=1024, n_bins=24*7, bins_per_octave=24)
    return cqt

def extract_mfcc(file):
    audio,sr=librosa.load(file_name, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return mfccs

cqt_data = []
mfcc_data = []

for index_num,row in tqdm(metadata.iterrows(),colour='green'):
    file_name = os.path.join(os.path.abspath(audio_path) + '/' + str(row["filename"]))
    class_label = row['target']
    cqt_val = extract_cqt(file_name)
    mfcc_val = extract_mfcc(file_name)
    cqt_data.append([cqt_val, class_label])
    mfcc_data.append([mfcc_val, class_label])

cqt_df = pd.DataFrame(cqt_val, columns=('features','label')).to_pickle("cqt.pkl")
mfcc_df = pd.DataFrame(mfcc_val, columns=('features','label')).to_pickle("mfcc_pkl")