import torch
from torch.utils.data import Dataset


class TextClassificationCollator():

    # tokenizer 받아오고, max 길이 하나 줌 
    def __init__(self, tokenizer, max_length, with_text=True):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.with_text = with_text

    def __call__(self, samples):
        # In samples :  __getitem__ return 값 (dictionary)의 list 들어있음
        texts = [s['text'] for s in samples]
        labels = [s['label'] for s in samples]

        # tokenizer 의 __call__ 호출 됨 => Huggingface tutorial
        encoding = self.tokenizer(
            texts,
            # padding 처리(알아서 해주는 격)
            padding=True,
            # truncation = true 면 max_length 기준으로 
            truncation=True,
            return_tensors="pt",
            max_length=self.max_length
        )

        return_value = {
            'input_ids': encoding['input_ids'],
            # attention_mask 왜? padding 들어간 부분에는 attention 들어가면 안됨.
            # 그 부분에 attention weight안 가도록 하기 위해 
            'attention_mask': encoding['attention_mask'],
            # list => torch long
            'labels': torch.tensor(labels, dtype=torch.long),
        }
        if self.with_text:
            return_value['text'] = texts

        return return_value

        # from torch.utils.data import Dataset 상속 받아서 필요한 함수만 override 
class TextClassificationDataset(Dataset):

    def __init__(self, texts, labels):
        # 전체 데이터
        self.texts = texts 
        self.labels = labels
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, item):
        text = str(self.texts[item])
        label = self.labels[item]

        return {
            'text': text,
            'label': label,
        }