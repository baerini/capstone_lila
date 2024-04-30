import os
import json
import pandas as pd

path = "./skku/2024/캡스톤/data/"
files = [f for f in os.listdir(path+"02.라벨링데이터") if f.endswith('.json')]


df = pd.DataFrame(columns=['성별', '연령대', '자기 소개'])

persona_val = []


for i, file in enumerate(files):
    with open(os.path.join(path, file), 'r') as f:
        data = json.load(f)
        if 'info' in data:
            info = data['info']
            if 'personas' in info:
                personas = info['personas']
                for personas_dict in personas:
                    if 'persona' in personas_dict:
                        row = {}
                        for persona_dict in personas_dict['persona']:
                            if persona_dict['profile_major'] == "성별":
                                row['성별'] = persona_dict['profile_minor']
                            elif persona_dict['profile_major'] == "연령대":
                                row['연령대'] = persona_dict['profile_minor']
                            elif persona_dict['profile_major'] != "연령대" and persona_dict['profile_major'] != "성별":
                                persona_val.append(persona_dict['profile'])
                        profile = " ".join(persona_val)
                        row['자기 소개'] = profile
                        df = df.append(row, ignore_index=True)
                        persona_val = []

df.to_csv('./skku/2024/캡스톤/data/train/profile.csv', index=False)