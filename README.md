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
   :*중요* BP 수행은 꼭 training set (Validation set 이나 test set이 BP 과정에 들어가면 안됨)
   ==> BP 자체도 모델링 하는 과정으로 볼 수 있기 때문에 Validation set 이나 test set이 BP 과정에 들어가면 "Cheating" 한거라고 볼 수 있음=> overfitting
### 3. Iterator: DataLoader 활용


> ## Probelm:  NLP에서는 미니배치 내의 각 element tensor 크기가 다름
>  => 문장의 길이를 코퍼스 전체에 대해 고정? 이거 안됨 

> Dataloader의 파라미터 collate_fn 으로 해결해야됨: 미니배치 element들을 list로 만들어 주기 때문, List를 받아 가장 긴 문장 기준으로 padding 채워 넣고, 
미니배치 텐서로 만들어서 반환

## Huggungface Tokenizer 
### Subword Segmentation:
- 많은 언어들에서 단어는 더 작은 의미 단위들이 모여서 구성됨, Data-driven (통계 방식, 사전을 만드는게 아닌)으로 해결 하는 방법.
  한자나 라틴어등 (단어의 뜻의 기원을 더 쪼개는 단위)
- Oov(Out-Of-Vocabulary)를 없앨 수 있기 때문에 성능상 매우 큰 이점
- But, 모델 파일이 하나 더 생기는 것이기 때문에, 학습을 할 때 활용한 Tokenizer를 Test를 할 때도 "똑같이" 적용 해 줘야함.
- 그래서 영어같은 경우는 그냥 BPE 쓰면 되는데 한국어는 형태소 분석기를 먼저 쓴 후에 BPE 를 쓰는경우가 있음. (그냥 BPE만 써도 되는데 미미하게 성능차이 있기는 함)
- (해 당 프로젝트에서는 단독으로 BPE 쓰겠음)

  >Huggingface 내부적에서 Tokenizer 학습 하는 방법 
![image](https://github.com/JinnyKo/Text-Classification-using-BERT/assets/93627969/73754860-6dba-4b0d-9a87-197b481660e3)

  

