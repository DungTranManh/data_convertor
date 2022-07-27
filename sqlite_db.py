from json import load
import sqlite3
import pandas as pd
import csv

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("create table big_data (id INTEGER PRIMARY KEY AUTOINCREMENT, ent_seq INTERGER, keb text, reb text, name_type text, trans_det text)")

file = open("data.csv",encoding="utf-8")
contents = csv.reader(file)


cursor.executemany("INSERT INTO big_data (ent_seq,keb,reb,name_type,trans_det) VALUES (?,?,?,?,?)", contents)

conn.commit()
conn.close()