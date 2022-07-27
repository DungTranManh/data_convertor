from sys import api_version
from unicodedata import name
import xml.etree.ElementTree as ET

xml_file_name = 'JMnedict.xml'

tree = ET.parse(xml_file_name)
root = tree.getroot()
i = 0
res = list()
for entry in root.findall("entry"):
    ent_seq = entry.find("ent_seq").text
    # k_ele = entry.findall("k_ele")
    # if len(k_ele) != 1:
    #     for i in range(len(k_ele)):
    #         keb = k_ele[i].findall("keb")
    #         res.append(len(keb))
    # r_ele = entry.findall("r_ele")
    # # if len(r_ele) != 1:
        # for i in range(len(r_ele)):
        #     reb = r_ele[i].findall("reb")
        #     res.append(len(reb))
    trans = entry.findall("trans")
    # if len(trans) != 1:
    for i in range(len(trans)):
        name_type = trans[i].findall("name_type")
        if len(name_type) != 1:
            print(ent_seq)
            # res.append(len(name_type))
            # trans_det = trans[i].findall("trans_det")
            # res.append(len(trans_det))
# print(max(res))

