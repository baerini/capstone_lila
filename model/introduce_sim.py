import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

path = "./data/train/"
train = pd.read_csv(path+'updated_train.csv')

def tokenize_ko(x):
    tokenizer = Okt()
    x = tokenizer.normalize(x) # 텍스트 Normalization
    x = tokenizer.morphs(x) # 형태소 분리
    return x


#모국어 외국어 매칭해서 데이터프레임 반환
def match_lang(user_id, train):
    user = train[train['User_ID'] == user_id]
    # 모국어와 희망하는 외국어가 모두 동일한 사용자 필터링
    filtered_users = train[(user['외국어'].iloc[0] == train['모국어']) & (user['모국어'].iloc[0] == train['외국어']) | (train['User_ID'] == user_id)]
    return filtered_users

def match_gender(user_id, train, gender):
    if not gender:
        return train
    filtered_df = train[(train['성별'] == gender) | (train['User_ID'] == user_id)]
    return filtered_df

def match_level(user_id, train, level):
    if not level:
        return train
    filtered_df = train[(train['외국어 수준'] == level) | (train['User_ID'] == user_id)]
    return filtered_df

def content_base(user_id, train, gender, level):
    temp1 = match_lang(user_id, train)
    temp2 = match_gender(user_id, temp1, gender)
    result = match_level(user_id,temp2, level)
    return result

def stopwords(path):
    tokenizer = Okt()
    # 불용어 파일에서 불용어 읽어오기
    with open(path+'stopwords-ko.txt', 'r', encoding='utf-8') as f:
        stopwords = f.readlines()
    stopwords = [tokenizer.morphs(word)[0] for word in stopwords]
    return stopwords

def cosine_sim(train, n, gender, level):
    #유저 아이디 n과 언어 매칭되는 유저들 추출
    sample = content_base(n, train, gender, level)
    introduce = list(sample['자기 소개'])
    #자기 소개 임베딩
    tf = TfidfVectorizer(stop_words=stopwords(path), tokenizer=tokenize_ko)
    tfidf_matrix =tf.fit_transform(introduce)
    # print(tfidf_matrix.shape) user수 * 임베딩수
    #코사인 유사도 게산
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

#자기소개 기반 추천
def intro_recommend(user_id, gender, level):
    sample = content_base(user_id, train, gender, level)
    rec_df = sample.set_index('User_ID')
    idx = rec_df.index.get_loc(user_id)
    sim_scores = list(enumerate(cosine_sim(train, user_id, gender, level)[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    user_indices = [i[0] for i in sim_scores]
    return sample.iloc[user_indices]

# print(train[train['User_ID'] == 30000])
# print(intro_recommend(30000, '남', '상'))
