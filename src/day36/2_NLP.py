# 텐서플로 토크나이저
from tensorflow.keras.preprocessing.text import Tokenizer
sentences = [
    '영실이는 나를 정말 정말 좋아해' ,
    '영실이는 영화를 좋아해'
] # 문장들
tokenizer = Tokenizer() # 토크나이저 객체 생성
tokenizer.fit_on_texts(sentences) # fit_on_texts(문장목록)
print(tokenizer.word_index) # 문장에서 문자들을 인덱스와 매칭한다.
# 단어 사전 {단어 : 인덱스} # 빈도수 순 , 중복 단어 제외
# {'영실이는': 1, '정말': 2, '좋아해': 3, '나를': 4, '영화를': 5}

# 벡터로 변환
word_encoding = tokenizer.texts_to_sequences(sentences)
print(word_encoding) # [[1, 4, 2, 2, 3], [1, 5, 3]]

# 새로운 단어
new_sentence = ['영실이는 경록이와 나를 좋아해'] # '경록이와' 앞전에 없던 단어이다.
print(tokenizer.texts_to_sequences(new_sentence))
# [[1, 4, 3]] # 1:영실이는 4:나를 3:좋아해 # 경록이는 사전에 없으므로 인코딩에서 빠졌다.

# 새로운 단어 처리 방법 # 앞전 사전에 등록되지 않는 단어들은 <OOV> 표현한다.
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences) # .fit_on_texts(문장목록) 첫번째 문장 목록을 사전화(문자와 숫자매칭) 하기
print(tokenizer.word_index) # word_index 사전 목록 출력
# {'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}
print(tokenizer.texts_to_sequences(sentences)) # 인코딩1 # [[2, 5, 3, 3, 4], [2, 6, 4]]
print(tokenizer.texts_to_sequences(new_sentence)) # 인코딩2 # [[2, 1, 5, 4]]

# 단어 사전의 최대 개수 설정 # 최대 개수와 단어들은 <OOV> 표현된다. # num_words=(N-1)개
tokenizer = Tokenizer(num_words=3 , oov_token="<OOV>") # 사전 목록의 단어수는 최대 2 , (N-1)개이며, 나머지는 <OOV> 표현
tokenizer.fit_on_texts(sentences)
print(tokenizer.word_index) # {'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}
print(tokenizer.texts_to_sequences(sentences)) # [[2, 1, 1, 1, 1], [2, 1, 1]] # '정말' , '좋아해' 빈도수가 같아서 중복이 들어가서 다 1로 나옴 # 시퀀스에 포함이 안됨
print(tokenizer.texts_to_sequences(new_sentence)) # [[2, 1, 1, 1]] # 2:영실이는 1:경록이와 1:나를 1:좋아해

# 문장의 길이 맞추기 # 패딩 # pad_sequences(인코딩단어들) : 문장의 길이를 맞춘다. 앞쪽에 0으로 채운다.
from tensorflow.keras.preprocessing.sequence import pad_sequences
word_encoding = tokenizer.texts_to_sequences(sentences) # 인코딩된 결과
print(word_encoding) # [[2, 1, 1, 1, 1], [2, 1, 1]]
print(pad_sequences(word_encoding)) # [[2 1 1 1 1] [0 0 2 1 1]] # 두번째 문장에서 첫번째 문장과 길이 맞추기
    # padding='post' : 뒤쪽에 0으로 채운다, 생략시 앞쪽에 0으로 채운다.
print(pad_sequences(word_encoding , padding='post')) # [[2 1 1 1 1] [2 1 1 0 0]]
    # 문장 길이 최대값 설정 # 앞쪽에서 잘린다.
print(pad_sequences(word_encoding , padding='post' , maxlen=4)) # [[1 1 1 1] [2 1 1 0]]
    # 문장 길이 최대값 설정 # truncating='post' 뒤쪽에서 잘린다. 생략 시 앞쪽에서 잘린다.
print(pad_sequences(word_encoding , padding='post' , maxlen=4 , truncating='post')) # [[2 1 1 1] [2 1 1 0]]