# Huggingface_Transformers_BERT
## 장점 
- Model Hub
- 전체(전처리, 학습, 벤치마크 테스트 등등)  pipeline 쉽게 통합됨

## Text Classification Process 
### - 입력: 문장 
### - 출력: Class에 대한 index , class별 확률 값  
### - 최종 test result 와 정답을 비교 후 Accuray 도출 

## Data Loading Procedure 
### 1. Read & Split
### 2. Preprocessing
   :*중요* BP(Backpropagation)수행은 꼭 training set (Validation set 이나 test set이 BP 과정에 들어가면 안됨)
   ==> BP 자체도 모델링 하는 과정으로 볼 수 있기 때문에 Validation set 이나 test set이 BP 과정에 들어가면 "Cheating" 한거라고 볼 수 있음
### 3. Iterator: DataLoader 활용


> ## Probelm:  NLP에서는 미니배치 내의 각 element tensor 크기가 다름
>  => 문장의 길이를 코퍼스 전체에 대해 고정? 이거 안됨 
> Dataloader의 파라미터 collate_fn 으로 해결해야됨: 미니배치 element들을 list로 만들어 주기 때문, List를 받아 가장 긴 문장 기준으로 padding 채워 넣고, 
미니배치 텐서로 만들어서 반환

