import pandas as pd
import numpy as np
from tqdm import tqdm

data = pd.read_csv('./skku/2024/캡스톤/data/train/profile.csv')
name = pd.read_csv('./skku/2024/캡스톤/data/yob2010.txt', sep=',')
#print(data['성별'].value_counts())

#print(data['연령대'].value_counts())

#이름
name.columns = ['Name', 'Gender', 'temp']
name.drop('temp', axis=1, inplace=True)
len = len(data)
name = name.iloc[:len]
df = pd.concat([data,name], axis=1)
df.drop('Gender', axis=1, inplace=True)
df = df.rename(columns={'Name':'이름'})
df = df[['이름','성별','연령대','자기 소개']]

unique_values = {
    col: df[col].dropna().unique() for col in df.columns
}

#null 값 fill
for col in df.columns:
    null_indices = df[col].isnull()
    if null_indices.any():
        num_nulls = null_indices.sum()
        replacement_values = np.random.choice(unique_values[col], size=num_nulls)
        df.loc[null_indices, col] = replacement_values
        
languages = ['한국어', '영어', '아랍어', '불어', '일어', '중국어', '스페인어']
levels = ['상', '중', '하']

df_temp = pd.DataFrame(columns = ['모국어', '외국어', '외국어 수준'])

for i in tqdm(range(df.shape[0])):
    native_lang = np.random.choice(languages)
    foreign_lang = [lang for lang in languages if lang != native_lang]
    foreign_lang = np.random.choice(foreign_lang)
    level = np.random.choice(levels)
    df_temp.loc[i] = [native_lang, foreign_lang, level]

df = pd.concat([df,df_temp], axis=1)
df.insert(0, 'User_ID', range(1, df.shape[0] + 1))

df.to_csv('./skku/2024/캡스톤/data/train/train.csv', index=False)
