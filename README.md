# Ближайшие бары

Описаны функции для поиска бара с максимальным количеством мест и минимальным.
Также проводит поиск ближайщий от введенных координат

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
Сам список баров Москвы можете взять по ссылке (выгрузка [data.mos.ru](data.mos.ru)).
В начале работы вы указываете путь к файлу баров и ваши координаты.

Запуск на Linux:

```bash
$ python bars.py -f<path to file> X Y
```

# пример ответа скрипта вывод всех данных найденного бара.

```bash
the biggest bar: 
{
    "geometry": {
        "type": "Point", 
        "coordinates": [
            37.638228501070095, 
            55.70111462948684
        ]
    }, 
    "type": "Feature", 
    "properties": {
        "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8", 
        "Attributes": {
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ], 
            "Name": "Спорт бар «Красная машина»", 
            "District": "Даниловский район", 
            "OperatingCompany": null, 
            "global_id": 169375059, 
            "IsNetObject": "нет", 
            "Address": "Автозаводская улица, дом 23, строение 1", 
            "SocialPrivileges": "нет", 
            "AdmArea": "Южный административный округ", 
            "SeatsCount": 450
        }, 
        "VersionNumber": 2, 
        "ReleaseNumber": 2, 
        "DatasetId": 1796
    }
}
the smallest bar: 
{
    "geometry": {
        "type": "Point", 
        "coordinates": [
            37.35805920566864, 
            55.84614475898795
        ]
    }, 
    "type": "Feature", 
    "properties": {
        "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53", 
        "Attributes": {
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 258-94-19"
                }
            ], 
            "Name": "БАР. СОКИ", 
            "District": "район Митино", 
            "OperatingCompany": null, 
            "global_id": 20675518, 
            "IsNetObject": "нет", 
            "Address": "Дубравная улица, дом 34/29", 
            "SocialPrivileges": "нет", 
            "AdmArea": "Северо-Западный административный округ", 
            "SeatsCount": 0
        }, 
        "VersionNumber": 2, 
        "ReleaseNumber": 2, 
        "DatasetId": 1796
    }
}
the closest bar: 
{
    "geometry": {
        "type": "Point", 
        "coordinates": [
            36.900000000253, 
            55.303299999814
        ]
    }, 
    "type": "Feature", 
    "properties": {
        "RowId": "bb9eb30d-d16b-4821-8d9c-894b581ac762", 
        "Attributes": {
            "PublicPhone": [
                {
                    "PublicPhone": "(985) 069-34-47"
                }
            ], 
            "Name": "Staropramen", 
            "District": "Красносельский район", 
            "OperatingCompany": null, 
            "global_id": 281494712, 
            "IsNetObject": "нет", 
            "Address": "Садовая-Спасская улица, дом 19, корпус 1", 
            "SocialPrivileges": "нет", 
            "AdmArea": "Центральный административный округ", 
            "SeatsCount": 50
        }, 
        "VersionNumber": 2, 
        "ReleaseNumber": 2, 
        "DatasetId": 1796
    }
}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
