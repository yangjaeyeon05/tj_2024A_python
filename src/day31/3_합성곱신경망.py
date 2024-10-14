import numpy as np
import tensorflow as tf

# 1. 데이터셋 로드 , 10가지 종류의 의류 이미지 데이터셋
# Label Description
# 0 T-shirt/top
# 1 Trouser
# 2 Pullover
# 3 Dress
# 4 Coat
# 5 Sandel
# 6 Shirt
# 7 Sneaker
# 8 Bag
# 9 Ankle boot

fashion_mnist = tf.keras.datasets.fashion_mnist
(x_train , y_train),(x_valid , y_valid) = fashion_mnist.load_data()
# 과제 : Functional API 이용한 모델 생성 (다중입력)과 예측 테스트
print(x_train.shape , y_train.shape)
print(x_valid.shape , y_valid.shape)

# 2. 정규화
x_train = x_train/255.0
x_valid = x_valid/255.0

# 3. 채널 추가
x_train_in = tf.expand_dims(x_train , -1)
x_valid_in = tf.expand_dims(x_valid , -1)

print(x_train_in.shape , x_valid_in.shape)

# 4. 모델 생성
# 입력레이어 1
inputs = tf.keras.layers.Input(shape=(28 , 28 , 1))
conv = tf.keras.layers.Conv2D(64 , (3,3) , activation='relu')(inputs)
pool = tf.keras.layers.MaxPooling2D((2,2))(conv)
flat = tf.keras.layers.Flatten()(pool)
# 입력레이어2
flat_inputs = tf.keras.layers.Flatten()(inputs)

# 입력레이어 합치기
concat = tf.keras.layers.Concatenate()([flat , flat_inputs])

# 추가 레이어
dense1 = tf.keras.layers.Dense(128, activation='relu')(concat)
dropout1 = tf.keras.layers.Dropout(0.5)(dense1)  # 50% 드롭아웃
dense2 = tf.keras.layers.Dense(64, activation='relu')(dropout1)

# 출력 레이어
outputs = tf.keras.layers.Dense(10, activation="softmax")(dense2)

model = tf.keras.models.Model(inputs=inputs , outputs=outputs)
print(model.summary())

# 5. 모델 컴파일
model.compile(optimizer='adam' , loss='sparse_categorical_crossentropy' , metrics=['accuracy'])

# 6. 모델 훈련
history = model.fit(x_train_in , y_train ,
                    validation_data=(x_valid_in , y_valid) , epochs=10)

# 7. 모델 성능
val_loss , val_acc = model.evaluate(x_valid_in , y_valid)
print(val_loss , val_acc)

# 8. 모델 예측
print(y_valid[0])
preds = model.predict(x_valid_in)
print(preds[0])

preds_labels = np.argmax(preds , axis=-1)
print(preds_labels)

import cv2

# 이미지 읽기
img = cv2.imread('shirt.jpg')

# 이미지 흑백으로 바꾸기
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('img' , img)
# cv2.waitKey()

img = cv2.resize(img , dsize=(28 , 28))
print(img.shape)

# 정규화
img = img/255.0

# 채널축 추가
img = tf.expand_dims(img , -1) # 마지막 인덱스
img = tf.expand_dims(img , 0) # 첫번째 인덱스
print(img.shape)

# 모델을 이용한 새로운 이미지 예측하기
result = model.predict(img)
print(tf.argmax(result[0]).numpy())



