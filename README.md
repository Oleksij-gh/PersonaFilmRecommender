# PersonaFilmRecommender
Система рекомендаций фильмов на основе психологического портрета пользователя

[.ipynb](https://github.com/Oleksij-gh/PersonaFilmRecommender/blob/main/rnd/RecSysBinary.ipynb) с процессом анализа

Датасет взят с [Kaggle](https://www.kaggle.com/datasets/arslanali4343/top-personality-dataset/data)

## Инициализация
```Python 3.11.9```

Все необходимые библиотеки указаны в ```requirements.txt```

После установки всех необходимых библиотек запуск производится инициализацией ```main.py```

При изменении пути к файлам необходимо внести изменения в ```config.ini```

Результатом работы является ```json``` содержащий:
- id пользователя
- Название фильма
- Результат предикта модели (0 - фильм не понравится, 1 - фильм понравится)
  
Более подробное описание файла конфигурации и структура json указаны ниже.

## ```config.ini```
```
[Path]
MODEL_PATH = '' - путь к весам модели
CBE_PATH = '' - путь к сохранённому CatBoostEncoder
INPUT_PATH = '' - пусть к json, в котором хранятся данные на вход модели
OUTPUT_PATH = '' - пусть куда будет сохранён json с результатами
```

## ```.json```

### Структура json, подаваемого в ```INPUT_PATH```
```json
{
    "index":{
    "userid": "str",
    "openness": "float",
    "agreeableness": "float",
    "emotional_stability": "float",
    "conscientiousness": "float",
    "extraversion": "float",
    "title": "str",
    "tag1": "str",
    "tag2": "str",
    "tag3": "str"}
}
```

Пример

```json
    {
    "0": {
    "userid": "8e7cebf9a234c064b75016249f2ac65e",
    "openness": 5.0,
    "agreeableness": 2.0,
    "emotional_stability": 3.0,
    "conscientiousness": 2.5,
    "extraversion": 6.5,
    "title": "Toy Story (1995)",
    "tag1": "animation",
    "tag2": "pixar",
    "tag3": "comedy"},
    "1": {
    "userid": "8e7cebf9a234c064b75016249f2ac65e",
    "openness": 5.0,
    "agreeableness": 2.0,
    "emotional_stability": 3.0,
    "conscientiousness": 2.5,
    "extraversion": 6.5,
    "title": "Heat (1995)",
    "tag1": "action",
    "tag2": "crime",
    "tag3": "dialogue"}
}
```

### ```output.json```

```json
{
"0":{
"userid":"8e7cebf9a234c064b75016249f2ac65e",
"title":"Toy Story (1995)",
"label":1.0},
"1":{
"userid":"8e7cebf9a234c064b75016249f2ac65e",
"title":"Heat (1995)",
"label":1.0}
}
```
