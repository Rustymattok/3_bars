# Ближайшие бары

Описаны функции для поиска бара с максимальным количеством мест и минимальным.
Также проводит поиск ближайщий от введенных координат

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
Также в корне проекта должен лежать файл bars.json ( выгрузка data.mos.ru)
```
Достаточно обновить bars.json на более свежий, чтобы получить актуальную информацию
```

Запуск на Linux:

```
$ python bars.py 
```

# пример ответа скрипта вывод всех данных найденного бара.

```
{'geometry': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'},
'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2,
'RowId': 'fbe6c340-4707-4d74-b7ca-2b84a23bf3a8', 'Attributes': {'global_id': 169375059,
'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'OperatingCompany': None,
'AdmArea': 'Южный административный округ', 'District': 'Даниловский район',
'Address': 'Автозаводская улица, дом 23, строение 1',
'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}],
'SeatsCount': 450, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
