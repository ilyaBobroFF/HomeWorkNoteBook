from Controller import *

print("Выберите режим работы:")
print("1 - Записать заметку")
print("2 - Прочитать все заметки")
print("3 - Изменить заметку по id")
print("4 - Просмотр заметок по дате")
print("5 - Удалить заметку по id")
mode = int(input("Введите цифру режима работы: "))

if mode < 1 or mode > 5:
    print("Не верно введен режим работы")

if mode == 1:
    name = input("Введите название заметки: ")
    text = input("Тест заметки введите: ")
    write_control(name, text)

if mode == 2:
    read_control()

if mode == 3:
    id = int(input("Введите идентификатор для замены: "))
    if int(id) > int(get_last_id(name_file)):
        print("Такой заметки нет")
    else:
        name = input("Введите НОВОЕ название заметки: ")
        text = input("Новый тест заметки введите: ")
        up_date_control(id, name, text)

if mode == 4:
    data_down = input("Введите дату ОТ в формате дд.мм.гггг: ")
    data_up = input("Введите дату ДО в формате дд.мм.гггг: ")
    find_data_control(data_down, data_up)

if mode == 5:
    id = int(input("Введите идентификатор для УДАЛЕНИЯ: "))
    delete_cotrol(id)