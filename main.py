from model import Model

import configparser
import category_encoders as ce
import pickle
import pandas as pd
import torch
import json
import numpy as np

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг

# читаем пути к файлам из конфига
MODEL_PATH = config['Path']['MODEL_PATH']
CBE_PATH = config['Path']['CBE_PATH']
INPUT_PATH = config['Path']['INPUT_PATH']
OUTPUT_PATH = config['Path']['OUTPUT_PATH']

# загружаем CatBoostEncoder
with open(CBE_PATH, 'rb') as f:
    encoder = pickle.load(f)


# Читаем данные из json и преобразуем через cbe
df = pd.read_json(INPUT_PATH, orient='index')
X = encoder.transform(df).values
X = torch.tensor(X, dtype=torch.float32)

# Инициализируем модель и загружаем обученные веса
model = Model(X.shape[1])
model.load_state_dict(torch.load(MODEL_PATH))

# Предиктим результат
model.eval()
with torch.no_grad():
  predict = model(X)
predict = (predict > 0.5).float()

# Сохраняем полученные результаты в json
df['label'] = predict.numpy()
df[['userid', 'title', 'label']].to_json(OUTPUT_PATH + 'output.json', orient='index')

print('Done')
