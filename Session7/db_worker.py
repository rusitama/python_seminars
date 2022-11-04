import csv
import os.path
import xml.etree.ElementTree as ET
from xml.dom import minidom

db_file = 'phonebook.csv'
db = []
row_id = 0  # id последней записи

def init_data_base():
    global row_id
    global db
    global db_file
    db.clear()
    if os.path.exists(db_file):
        with open(db_file, 'r', newline = '') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > row_id):
                        row_id = int(row[0])
    else:
        open(db_file, 'w', newline = '').close()

def create(name = '', surname = '', number = ''):
    global row_id
    global db
    global db_file
    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number):
            print("Такие данные уже существуе!")
            return
    row_id += 1
    new_row = [str(row_id), name.title(), surname.title(), number]
    db.append(new_row)
    print("Данные заведены.")
    with open(db_file, 'a', newline = '') as csv_file:
        writer = csv.writer(csv_file, delimiter = ',', quotechar = '\'', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(new_row)

def serch(id='', name='', surname='', number=''):
    global row_id
    global db
    global db_file
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        result.append(row)
    if len(result) == 0:
        return f'В базе нет контактов'
    else:
        return result

def update(id = '', new_name = '', new_surname = '', new_number = ''):
    global row_id
    global db
    global db_file
    if(id == ''):
        print('не ввели номер ID')
        return
    with open(db_file, 'w', newline = '') as csv_file:
        writer = csv.writer(csv_file, delimiter = ',', quotechar = '\'', quoting = csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()
                if(new_surname != ''):
                    row[2] = new_surname.title()
                if(new_number != ''):
                    row[3] = new_number
            writer.writerow(row)

def delete(id=''):
    global row_id
    global db
    global db_file
    if(id == ''):
        print('specify id for delete')
        return
    for row in db:
        if (row[0] == id):
            db.remove(row)
            break
    with open(db_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)

def export_data_to_xml():
    global db
    new = ET.Element('telephonebook')
    for row in db:
        title = ET.SubElement(new, 'title')
        n = 1
        for line in row:
            if n == 1:
                subtitle1 = ET.SubElement(title, 'id')
                subtitle1.text = line
            elif n == 2:
                subtitle2 = ET.SubElement(title, 'name')
                subtitle2.text = line
            elif n == 3:
                subtitle3 = ET.SubElement(title, 'surname')
                subtitle3.text = line
            elif n == 4:
                subtitle4 = ET.SubElement(title, 'number')
                subtitle4.text = line
                n = 1
            n += 1
    save_xml('telephonebook.xml', new)


def save_xml(filename, xml_code):
    xml_string = ET.tostring(xml_code).decode()
    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'w', encoding='UTF-8') as xml_file:
        xml_file.write(xml_prettyxml)

def parse_xml():
    global db
    global db_file
    db.clear()
    tree = ET.parse('telephonebook.xml')
    root = tree.getroot()
    id = ""
    name = ""
    surname = ""
    number = ""
    for elem in root:
        for subelem in elem:
            if subelem.tag == "id":
                id = subelem.text
            elif subelem.tag == "name":
                name = subelem.text
            elif subelem.tag == "surname":
                surname = subelem.text
            elif subelem.tag == "number":
                number = subelem.text
        new_row = [str(id), name.title(), surname.title(), number]
        db.append(new_row)
    with open(db_file, 'a', newline = '') as csv_file:
         writer = csv.writer(csv_file, delimiter = ',', quotechar = '\'', quoting = csv.QUOTE_MINIMAL)
         writer.writerow(new_row)

def export_data_to_txt():
    global db
    f = open('phone.txt', 'w')
    for row in db:
        n = 1
        for r in row:
            if n == 4:
                f.write(r + "\n")
                n = 1
            else:
                f.write(r + ", ")
                n += 1

            print(r)
    f.close()

def import_from_txt():
    global db
    global db_file
    db.clear()
    id = ""
    name = ""
    surname = ""
    number = ""
    f = open('phone.txt')
    for line in f:
        print(line + ",")
        rows = line.split()
        n = 1
        for l in rows:
            if n == 1:
                id = l
            elif n == 2:
                name = l
            elif n == 3:
                surname = l
            elif n == 4:
                number = l
            n += 1
        new_row = [str(id), name.title(), surname.title(), number]
        print(new_row)
        db.append(new_row)

    with open(db_file, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)