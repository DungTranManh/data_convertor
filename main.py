from sys import api_version
from unicodedata import name
import xml.etree.ElementTree as ET

xml_file_name = 'JMnedict.xml'

tree = ET.parse(xml_file_name)
root = tree.getroot()
i = 0
res = list()
for entry in root.findall("entry"):
    # ent_seq = entry.findall("ent_seq")
    # k_ele = entry.findall("k_ele")
    # if len(k_ele) != 1:
    #     for i in range(len(k_ele)):
    #         keb = k_ele[i].findall("keb")
    #         res.append(len(keb))
    r_ele = entry.findall("r_ele")
    if len(r_ele) != 1:
        for i in range(len(r_ele)):
            reb = r_ele[i].findall("reb")
            res.append(len(reb))
    # name_type = entry.find("trans").find("name_type").text
    # trans_det = entry.find("trans").findall("trans_det")
    # # print(f"{ent_seq},{keb},{reb},{name_type},{len(trans_det)}")
    # i += 1
    # if i == 4:
    #     break
    # res.append(len(r_ele))

print(max(res))

