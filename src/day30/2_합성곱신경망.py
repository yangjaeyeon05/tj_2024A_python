import tensorflow as tf
# 데이터셋 # 10가지 종류의 이미지 데이터셋 [비행기0,자동차1,새2,고양이3,사슴4,개5,개구리6,말7,배8,트럭9]
cifar10 = tf.keras.datasets.cifar10
(x_train , y_train),(x_valid , y_valid) = cifar10.load_data()

import matplotlib.pyplot as plt
# plt.imshow(x_train[0])
# plt.show()

# 확인용
print(x_train.shape , x_valid.shape) # (50000, 32, 32, 3) (10000, 32, 32, 3)

# for i in range(10):
#     plt.imshow(x_train[i])
#     print(y_train[i])
#     plt.show()

# 칼라 이미지의 합성곱 모델 만들기
# 데이터 전처리
x_train = x_train/255.0
x_valid = x_valid/255.0

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    tf.keras.layers.BatchNormalization(),  # 배치 정규화 추가
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.BatchNormalization(),  # 또 다른 배치 정규화 추가
    tf.keras.layers.Dense(10, activation='softmax'),
])

model.compile(optimizer='adam' , loss='sparse_categorical_crossentropy' , metrics=['accuracy'])
# 5. 모델 훈련
history = model.fit(x_train , y_train, # 학습에 사용되는 데이터
                    validation_data=(x_valid , y_valid), # 학습하면서 컴파일이 테스트를 할 테스트 데이터
                    epochs=10)  # 훈련 반복 횟수

# 1. 파이썬 OpenCV : 이미지 파일을 파이썬으로 호출하는 모듈 제공한다.
import cv2
# 2. 외부 이미지 가져오기
img = cv2.imread('poly.jpg')
print(img)
print(img.shape) # (336, 575, 3) # 원본 이미지는 가로 336 픽셀 세로 575 픽셀 컬러 (3채널)
# 3. 이미지의 사이즈 변경
img = cv2.resize(img , dsize=(32 , 32)) # 모델이 학습한 사이즈와 동일하게 변경

# * 정규화
img = img/255.0

# 4. 변경된 이미지 cv 시각화
# cv2.imshow('img' , img)
# cv2.waitKey()

# 5. 모델을 이용한 새로운 이미지 예측하기
result = model.predict(img[tf.newaxis , ...]) # (32 , 32 , 3) ---> (1 , 32 , 32 , 3)
print(tf.argmax(result[0]).numpy()) # 가장 높은 확률을 가진 종속 변수