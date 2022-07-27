import string
import xml.etree.ElementTree as ET
import csv
xml_file_name = 'JMnedict.xml'

tree = ET.parse(xml_file_name)
root = tree.getroot()

cols = ['ent_seq','keb','reb','name_type','trans_det']
rows = list()
res = tuple()
for entry in root.findall("entry"):
    # storage components
    reb_storage = ""
    keb_storage = ""
    name_type_storage = ""
    trans_det_storage = ""
    # get ent_seq
    ent_seq = entry.find("ent_seq").text
    # get keb
    k_ele = entry.findall("k_ele")
    for i in range(len(k_ele)):
        keb = k_ele[i].find("keb").text
        keb_storage += keb
        if i != len(k_ele) - 1:
            keb_storage += ','
    # get reb
    r_ele = entry.findall("r_ele")
    for i in range(len(r_ele)):
        reb = r_ele[i].find("reb").text
        reb_storage += reb
        if i != len(r_ele) - 1:
            reb_storage += ","
    # get name_type and trans_det
    trans = entry.findall("trans")
    for i in range(len(trans)):
        name_type = trans[i].findall("name_type")
        if name_type is not None:
            for tmp2 in range(len(name_type)):
                name_type_storage += name_type[tmp2].text
                if tmp2 != len(name_type) - 1:
                    name_type_storage += ','
        trans_det = trans[i].findall("trans_det")
        for tmp in range(len(trans_det)):
            trans_det_com = trans_det[tmp].text
            trans_det_storage += trans_det_com
            if tmp != len(trans_det) - 1:
                trans_det_storage += ','
    rows.append([ent_seq,keb_storage,reb_storage,name_type_storage,trans_det_storage])

with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(cols)

    # write multiple rows
    writer.writerows(rows)


