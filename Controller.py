from Filework import *
from Listwork import *
from datetime import datetime

class Filework:
    def __init__(self, note):
        self.write_text = note

name_file = "Notebook.csv"

def write_control(name, text):
    if not check_file(name_file):
        create_file(name_file)
    elif check_none_file(name_file):
        create_file(name_file)
    id = int(get_last_id(name_file)) + 1
    data = datetime.now()
    write(id, data, name, text)

def read_control():
    if check_file(name_file) and int(get_last_id(name_file) != 0):
        note_list = read(name_file)
        read_list(note_list)
    else:
        print("Нет введенных записей")

def up_date_control(id, name, text):
    if check_file(name_file) and int(get_last_id(name_file) != 0):
        note_list = read(name_file)
        data = datetime.now()
        new_list = up_date_list(note_list, id, data, name, text)
        up_date_file(new_list)
    else:
        print("Нет введенных записей")

def delete_cotrol(id):
    if int(id) > int(get_last_id(name_file)):
        print("Такой заметки нет")
    elif check_file(name_file) and int(get_last_id(name_file) != 0):
        note_list = read(name_file)
        new_list = delete_list(note_list, id)
        up_date_file(new_list)
    else:
        print("Нет введенных записей")

def find_data_control(data_str_down, data_str_up):
    if check_file(name_file) and int(get_last_id(name_file) != 0):
        data_down = datetime.strptime(data_str_down, '%d.%m.%Y')
        data_up = datetime.strptime(data_str_up, '%d.%m.%Y')
        new_list = find_data(data_down, data_up)
        read_list(new_list)
    else:
        print("Нет введенных записей")
