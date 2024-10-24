import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.divan.ru/ekaterinburg/category/svet"   \
      # "https://tomsk.hh.ru/vacancies/programmist"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(5)

vacancies = driver.find_elements(By.CLASS_NAME, 'LlPhw')
# my                                 'vacancy-card--hhzAtjuXrYFMBMspDjrF')
# vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')

# Выводим вакансии на экран
print(vacancies)

# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for vacancy in vacancies:
    try:
        # Находим элементы внутри вакансий по значению
        # Находим названия вакансии
    #    title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-info--umZA61PpMY07JVJtomBA').text
    # my    vacancy-name--SYbxrgpHgHedVTkgI_cA                                            # 'vacancy-name-wrapper--tzZ1sS33pe6ELop6_Cte').text
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.WdR1o').text
                                     # "span.vacancy-name--SYbxrgpHgHedVTkgI_cA").text
        # Находим названия компаний
    #    company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_4-3-6').text    # company-info-text--O32pGCRW0YDmp3BHuNOP").text

        # Находим зарплаты
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.pY3d2').text
        # Находим ссылку с помощью атрибута 'href'
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute("href")
    # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
    except:
        print("произошла ошибка при парсинге")
        continue

    # Вносим найденную информацию в список
    parsed_data.append([title, salary, link])
# , company, salary, link
# Закрываем подключение браузера
driver.quit()


# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд  'название компании',
    writer.writerow(['Название вакансии',  'зарплата', 'ссылка на вакансию'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)
