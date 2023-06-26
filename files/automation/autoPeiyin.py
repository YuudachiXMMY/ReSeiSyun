import os
import pandas as pd

# 图片存放的路径
tar = r'W://renpy//projects//ReSeiSyun//game//output'
input = r'W://renpy//projects//ReSeiSyun//game//input'

pd_reader = pd.read_csv('W://renpy//projects//ReSeiSyun//game//TODO.csv')

df = pd_reader[pd_reader["file"].notnull()]
file = '1100.mp3'
def f():
    for file in os.listdir(input):
        todo = int(file[:-4])
        if todo in df["file"].tolist() :
            tar_name = df.loc[df['file'] == todo]["Identifier"].item()
            print(tar_name)
            os.rename(os.path.join(input,file), os.path.join(tar,str(tar_name+".mp3")))
f()