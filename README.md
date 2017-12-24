## 1.Что это такое ?

Этот код позволяет отобразить JSON-структуру данных хранимую в файле в RAW формате  
в человекочитаемом виде

## 2.Системные требования
Для работы с программой понадобится Python3.5(который скорее всего у вас уже установлен,  
если Вы используете Linux)

## 3.Где можно скачать  
Можно скачать здесь - [pretify_json](https://github.com/aligang/4_json.git)

## 4.Как этим пользоваться...   
*a.Данный код может быть исползован как самостоятельная программа, при этом программа*
*попросит Вас указать файл с JSON*

```bash
$ python3.5 pprint_json.py <path to file>
{
    "красивый JSON,уровень 1":{
        "красивый  JSON,уровнь 2":{
	        "красивый  JSON,уровнь 3":{
                "пейлоуд, уровня 3"
            }
    }
}

```
*b. Функции могут быть импортированы в Ваш код (пример в разделе 5)*


## 5.Какие функции могут быть переиспользованы в вашем коде
Функция `load_data` читает структуру raw-JSON из файла и преобразует её в python-обект.  
Функция `pretty_print_json` преобразует python-объект в сроку JSON-а, при этом отображая  
её легкочитаемом виде
Импортировать и использовать функцию коди можно  следующим образом:  
```python
from pprint_json import load_data
from pprint_json import pretty_print_json

data_dict = load_data(filepath)
pretty_print_json(data_dict)
```

## 6. Цели
Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
