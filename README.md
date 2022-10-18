# Sound Classification 

> ## 학습 & 검증 데이터
[Environment Sound Classification 50](https://www.kaggle.com/datasets/mmoreaux/environmental-sound-classification-50)을 이용

---

> ## 목차
- [목표](#목표)
- [데이터 전처리](#데이터-전처리)
- [CNN 학습](#cnn-학습)
- [결론](#결론)

---

> ## 목표

* CQT(Constant-Q)와 MFCC(Mel-Frequency Cepstral Coefficient)등 각각 두 Feature를 사용해 학습비율을 8:2로 모델링을 진행하고, 두 CNN모델의 Accuracy 비교하여 최적의 Feature를 찾고, 차후 진행할 실시간 분류에 적합한 모델을 목표로 한다.

---

> ## 데이터 전처리

* Constant-Q(Constant-Q Transform)
    ![extract cqt](https://user-images.githubusercontent.com/108206338/196156891-307ea1c0-8a86-4a15-b605-68300ddcb81f.png)
    * 시간데이터를 주파수 영역 신호로 변환하는 방법
    

* MFCC(Mel-Frequency Cepstral Coefficient)
    ![extract mfcc](https://user-images.githubusercontent.com/108206338/196156895-faea650a-2898-477c-99dd-c2dd56b46e9d.png)
    * 오디오 신호에서 고유한 특징을 추출하는 방법

---

> ## CNN 학습

|Feature|Accuracy|Val Accuracy|Code|
|---|---|---|---|
|CQT|###|###|lnk|
|MFCC|###|###|lnk|


---

> ## 결론

