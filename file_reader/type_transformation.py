# -*- coding: utf-8 -*-
"""type_transformation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19btg8oDkGW37emLZrYv7Yae8dDgTyvAz
"""

import os
from langchain.document_loaders import PyPDFLoader
from langchain.docstore.document import Document
import pandas as pd
from tqdm import tqdm
import json
from langchain_community.document_loaders.text import TextLoader


def txt_files_to_dict(folder_path):
    files_dict = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            title = os.path.splitext(filename)[0]
            files_dict[title] = title + " " + content

    return files_dict

def pdfs_to_docs(folder_path):
    docs = []

    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    for filename in tqdm(pdf_files, desc='Processing PDFs'):
        file_path = os.path.join(folder_path, filename)
        loader = PyPDFLoader(file_path)
        docs.extend(loader.load_and_split())

    return docs



def load_and_modify_json(file_path):
    try:
        with open(file_path, 'r') as f:
            loaded_dict = json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return {}

    modified_dict = {}
    for key, value in loaded_dict.items():
        # Ensure value is a string for concatenation
        value_str = str(value) if not isinstance(value, str) else value
        modified_value = f"{key} {value_str}"
        modified_dict[key] = modified_value

    return modified_dict



def train_csv_loader(df):
  def store_columns_to_list_by_row(df, columns):
      combined_answers_list = []
      for index, row in df.iterrows():
          for column in columns:
            combined_answers_list.append(row[column])
      return combined_answers_list

  # -- answers
  columns_to_extract = ['답변_1', '답변_2','답변_3','답변_4', '답변_5']
  answers = store_columns_to_list_by_row(df, columns_to_extract)

  # ------------------- csv to docs -------------------------- #
  csv_docs = []
  for i in range(len(answers)):
    doc =  Document(page_content= answers[i], metadata={"source": "local"})
    csv_docs.append(doc)

  return csv_docs