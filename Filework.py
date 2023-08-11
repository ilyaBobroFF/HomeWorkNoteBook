import csv
from datetime import datetime
import os
class Filework:
    def __init__(self, note):
        self.write_text = note

def write(id, data, name, text):
    csv.register_dialect('my_dialect', delimiter=';', lineterminator="\r")
    with open("Notebook.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, 'my_dialect')
        file_writer.writerow([id, data, name, text])
    w_file.close()

def read(name_file):
    note_list = list()
    with open(name_file, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            note_list.append(row)
    r_file.close()
    return note_list

def get_last_id(name):
    with open(name, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        count = 0
        for row in file_reader:
            if(not "Идентификатор" in row[0]):
                count = row[0] 
    return count

def check_none_file(name):
    with open(name, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        count = 0
        for row in file_reader:
                count += 1
    r_file.close()
    if count == 0:
        return True
    else:
        return False

def up_date_file(note_list):
    csv.register_dialect('my_dialect', delimiter=';', lineterminator="\r")
    with open("Notebook.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, 'my_dialect')
        for item in note_list:
            file_writer.writerow(item)
    w_file.close()

def find_data(data_down, data_up):
    note_list = list()
    with open("Notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            if not "Идентификатор" in row[0]:
                cur_data = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
                if(cur_data > data_down and cur_data < data_up):
                    note_list.append(row)
    r_file.close()
    return note_list

def check_file(name):
    return os.path.exists(name)

def create_file(name):
    csv.register_dialect('my_dialect', delimiter=':', lineterminator="\r")
    with open(name, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, 'my_dialect')
        file_writer.writerow(["Идентификатор", "Дата записи", "Наименование", "Текст заметки"])
    w_file.close()