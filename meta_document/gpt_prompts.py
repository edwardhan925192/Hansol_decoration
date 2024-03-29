# -*- coding: utf-8 -*-
"""gpt_prompts.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HvaMeYai3P2J7ccgiwQQZx9ZztZJZtG-
"""

from tqdm import tqdm

def summarize_chat(text):
  completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
      {"role": "system", "content": "You are a helpful assistant who summarizes long texts into concise but overarching topic, one-sentence overviews, focusing on the main point."},
      {"role": "user", "content": f"핵심적인 내용을 한문장으로 간결하게 요약해줘. 문장: '{text}'"}
    ]
  )
  return completion.choices[0]

summary_lists = []

for text in tqdm(hansol_docs['내용'], desc='Summarizing documents'):
  summary = summarize_chat(text)
  summary_lists.append(summary.message.content)