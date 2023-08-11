
class Listwork:
    def __init__(self, note):
        self.write_text = note

def read_list(name_file):
        for row in name_file:
            print(f'{"; ".join(row)}')

def up_date_list(list_note, id, date, name, text):
    for item in list_note:
        if item[0] == str(id):
            item[1] = date
            item[2] = name
            item[3] = text
    return list_note

def delete_list(list_note, id):
    del_ok = False
    new_list = list() 
    for item in list_note:
        if item[0] == str(id):
            del_ok = True
        else:
            if(del_ok):
                item[0] = str(int(item[0]) - 1)
                new_list.append(item)
            else:
                new_list.append(item)
    return new_list