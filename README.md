# Huggingface_Transformers_BERT
## 장점 
- Model Hub
- 전체(전처리, 학습, 벤치마크 테스트 등등)  pipeline 쉽게 통합됨

## Text Classification Process 
### - 입력: 문장 
### - 출력: Class에 대한 index , class별 확률 값  
![image](https://github.com/JinnyKo/Text-Classification-using-BERT/assets/93627969/249ed8a5-29c7-4790-9566-b6faac14c990)
![image](https://github.com/JinnyKo/Text-Classification-using-BERT/assets/93627969/d5eb44bc-345c-4b25-8d1f-ed67fa9d00f4)
### - 최종 test result 와 정답을 비교 후 Accuray 도출 

## Data Loading Procedure 
1. Read & Split
2. Preprocessing
   :*중요* BP(Backpropagation)수행은 꼭 training set (Validation set 이나 test set이 BP 과정에 들어가면 안됨)
   ==> BP 자체도 모델링 하는 과정으로 볼 수 있기 때문에 Validation set 이나 test set이 BP 과정에 들어가면 "Cheating" 한거라고 볼 수 있음
3. Iterator: DataLoader 활용 

