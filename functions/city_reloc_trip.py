import pandas as pd

def city_reloc_trip(line:str) -> pd.Series:
    """
    Преобразует общие данные из 'Город, переезд, командировки' в отдельные колонки.
    
    Города разделяются на 3 категории:
        1 - Москва, Санкт-Петербург\n
        2 - города миллионники\n
        3 - другие\n
    
    Готовность к командировкам и переездам:
        * True - готов
        * False - нет
        
    Args:
        line (str): Данные из столбца 'Город, переезд, командировки'

    Returns:
        pd.Series: columns = ['Город', 'Готовность к переезду', 'Готовность к командировкам']
    """
    million_cities = ['Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань', 
                      'Челябинск', 'Омск', 'Самара', 'Ростов-на-Дону', 'Уфа', 'Красноярск', 
                      'Пермь', 'Воронеж', 'Волгоград']
    
    info_split = line.split(' , ')
    
    idx_city = 0
    # Проверка, указано ли метро
    if info_split[1].split()[0] != 'м.':
        # Метро не указано
        idx_reloc = 1
    else:
        idx_reloc = 2
    idx_trip = idx_reloc + 1
        
    # Определение города
    city = info_split[idx_city]
    if city in ['Москва', 'Санкт-Петербург']:
        pass
    elif city in million_cities:
        city = 'город-миллионник'
    else:
        city = 'Другое'
    
    # Готовность к переезду
    relocation = info_split[idx_reloc]
    # Проверка первого слова
    if relocation.split()[0] == 'не':
        ready4reloc = False        
    else:
        ready4reloc = True

    try:
    # Готовность к командировкам
        trip = info_split[idx_trip]
        # Проверка первого слова
        if trip.split()[0] == 'не':
            ready4trip = False
        else:
            ready4trip = True
    except IndexError:
        ready4trip = False

    return pd.Series([city, ready4reloc, ready4trip], index=['Город', 'Готовность к переезду', 'Готовность к командировкам'])

if __name__ == '__main__':
    print(city_reloc_trip('Москва , м. Беломорская , не готов к переезду , не готов к командировкам'))