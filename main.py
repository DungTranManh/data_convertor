import xml.etree.ElementTree as ET
import pandas as pd
xml_file_name = 'JMnedict.xml'

tree = ET.parse(xml_file_name)
root = tree.getroot()

cols = ['ent_seq','keb','reb','name_type','trans_det']
rows = list()
res = tuple()
i = 0
for entry in root.findall("entry"):
    # storage components
    reb_storage = tuple()
    keb_storage = tuple()
    name_type_storage = tuple()
    trans_det_storage = tuple()
    # get ent_seq
    ent_seq = entry.find("ent_seq").text
    # get keb
    k_ele = entry.findall("k_ele")
    for i in range(len(k_ele)):
        keb = k_ele[i].find("keb").text
        keb_storage += (keb,)
    # get reb
    r_ele = entry.findall("r_ele")
    for i in range(len(r_ele)):
        reb = r_ele[i].find("reb").text
        reb_storage += (reb,)
    # get name_type and trans_det
    trans = entry.findall("trans")
    for i in range(len(trans)):
        name_type = trans[i].find("name_type")
        name_type_storage += (name_type,)
        trans_det = trans[i].findall("trans_det")
        for tmp in range(len(trans_det)):
            trans_det_com = trans_det[tmp].text
            trans_det_storage += (trans_det_com,)
    res += ((ent_seq,keb_storage,reb_storage,trans_det_storage),)
    i += 1
    if i == 4:
        break
for i in range (5):
    print(res[i])
