def experience_by_month(line):
    """
    Преобразует значение Опыт работы количество месяцев.\n
    
    Принцип преобразования: \n
    1 - Пропуск -> return Nan \n
    2 - 'Не указано' -> return Nan \n
    3 - Указан опыт: \n
        * Опыт работы 3 года 2 месяца -> return 38
        * Опыт работы 7 лет 7 месяцев -> return 91
        * Опыт работы 4 года -> return 48
        * Опыт работы 11 месяцев -> return 11

    Args:
        line (str or np.nan): данные из столбца 'Опыт работы'
    """
    # Проверка на пропуск или некорректный тип данных
    if pd.isna(line) or not isinstance(line, str):
        return np.nan
    
    split_experience = line.split()
    # Проверка на наличие строки 'Опыт'
    if len(split_experience) < 3  or split_experience[0] != 'Опыт':
        return np.nan
    
    experience = 0
    # Указано количество лет (год, лет)
    if split_experience[3][0] in ['г', 'л']:
        experience = int(split_experience[2]) * 12
        # Проверка на количество месяцев
        if len(split_experience) > 5 and split_experience[5][:3] == 'мес':
            experience += int(split_experience[4])
        return experience
    
    # Опыт меньше одного года
    return int(split_experience[2])

if __name__ == '__main__':
    print(experience_by_month('Опыт работы 7 лет  Интернет-маркетолог,'))
