# -*- coding: utf-8 -*-
"""08_OpenAIEmbeddingSimilarity.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hz9NtRkCO32OidmRUOjUZ91KDQxs94gw
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 다국어 지원 모델 불러오기
model = SentenceTransformer('distiluse-base-multilingual-cased')

# 문장 임베딩
sentences = [
    "안녕하세요? 반갑습니다.",
    "안녕하세요? 반갑습니다!",
    "안녕하세요? 만나서 반가워요.",
    "Hi, nice to meet you.",
    "I like to eat apples."
]
embedded_sentences = model.encode(sentences)

# 유사도 계산 함수
def similarity(a, b):
    return cosine_similarity([a], [b])[0][0]

# 유사도 출력
for i, sentence in enumerate(embedded_sentences):
    for j, other_sentence in enumerate(embedded_sentences):
        if i < j:
            print(
                f"[유사도 {similarity(sentence, other_sentence):.4f}] {sentences[i]} \t <=====> \t {sentences[j]}"
            )

