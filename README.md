# Prettify JSON

Этот код позволяет отобразить JSON-структуру данных в человекочитаемом виде

# Quickstart
1 код может быть использован как самостоятельная программа, при этом потребуется указать файл, содержащий raw-JSON
2 код может быть импортирован в состеве двух функций, load_data - для подгрузки raw-JSON из файла 
	и pretty_print_json - для вывода в интерактивное меню в человекочитаемом виде

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
{
    "красивый JSON,уровень 1":{
        "красивый  JSON,уровнь 2":{
	    "красивый  JSON,уровнь 3":"пейлоуд, красивого JSON-а"
	}
    }
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
