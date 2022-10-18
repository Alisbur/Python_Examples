import xml.etree.ElementTree as ET
import class_person

def read_from_xml(db_path):
    result = []
    tree = ET.parse('Homework701 - Task_1\\db.xml')
    root = tree.getroot()
    for el in root:
        result.append(class_person.person_contact(el[0].text, el[1].text, el[2].text, el[3].text))
    return(result)


def append_to_xml(db_path, data_list):
    data = ET.Element('data')
    count = 1

    for el in data_list:
        person_list = ET.SubElement(data, f'Person{count}')
        var1 = ET.SubElement(person_list, 'LastName')
        var1.text = el.l_name
        var2 = ET.SubElement(person_list, 'Name')
        var2.text = el.f_name
        var3 = ET.SubElement(person_list, 'Phone')
        var3.text = el.phone_number
        var4 = ET.SubElement(person_list, 'Comment')
        var4.text = el.comment

        count+=1

    with open ("Homework701 - Task_1\\db.xml", "wb") as source:
        source.write(ET.tostring(data))  
