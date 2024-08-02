import pandas as pd

def split_gender_age(line:str):
    """
    Обрабатывает значение Пол_Возраст и разделяет на 2 отдельные переменные(Пол и Возраст).
    
    Например:
    Ввод - Мужчина , 39 лет , родился 27 ноября 1979
    Вывод - 
        'Пол': 'М', 
        'Возраст': 39

    Args:
        line (str): данные из столбца Пол_Возраст
        
    Returns:
        pd.Series: columns=['Пол', 'Возраст']     
    """
    
    gender_age = line.split(' , ')
    # Берется первая буква из Пола
    gender = gender_age[0][0]
    # Берется первое "слово"(номер) из возраста
    age = gender_age[1].split()[0]    
    return pd.Series([gender, int(age)], index=['Пол', 'Возраст'])


if __name__ == '__main__':
    print(split_gender_age('Мужчина , 39 лет , родился 27 ноября 1979'))