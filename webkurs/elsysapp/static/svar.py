import csv
from operator import le
import requests
from random import randint

#temporary list emulating database
guest1 = [['Hva heter du?',6],['Hvor er du fra?', 8]]
guest2 = [['Hvor er du fra?', 2]]
guest3 = [['Hvor er du fra?', 2]]

def extract_q(list):
  q_list=[]
  for i in range(len(list)):
    q_list.append(list[i][0])
  return q_list
#make lists only containing old questions
guest1_q = extract_q(guest1)
guest2_q = extract_q(guest2)
guest3_q = extract_q(guest3)

#fetch new (and old) questions and write to temporary csv
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRSwEE8anKsk21yNNi6mVELFMkmVETZVEmtie6oWh9QVtUXcE3O7zuxZJxhAQd3414FIrvRgx_zVPvm/pub?output=csv'
r = requests.get(url, allow_redirects=True)
open('webkurs/elsysapp/static/tester.csv', 'wb').write(r.content)

#read temporary csv
with open(r'webkurs/elsysapp/static/tester.csv', mode='r', newline="") as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)
    csv_file.close()

#add new questions to old questions, whilst avoiding duplicates
for i in data:
    if i[1] == "Gjest 1" and  (i[2] not in guest1_q):
      guest1.append([i[2],2,i[0]])
    elif i[1] == "Gjest 2"  and  (i[2] not in guest2_q):
      guest2.append([i[2],2,i[0]])
    elif i[1] == "Gjest 3" and  (i[2] not in guest2_q):
      guest3.append([i[2],2,i[0]])
    else:
        continue

#csv writing function
def write_csv(file_path, list):
  with open(file_path, 'w', newline="") as f: 
    write = csv.writer(f) 
    write.writerows(list) 

#write to corresponding csv
write_csv('webkurs/elsysapp/static/guest1.csv', guest1)
write_csv('webkurs/elsysapp/static/guest2.csv', guest2)
write_csv('webkurs/elsysapp/static/guest3.csv', guest3)

#generate list of random numbers for each guest
def rand_int_list(length):
  res = []
  for i in range(5):
    rand_a=randint(0,length-1)
    rand_b=randint(0,length-1)
    while True:
      if rand_a==rand_b:
        rand_a = randint(0,length-1)
        rand_b = randint(0,length-1)
      else:
        break
    res.append([rand_a,rand_b])
  return res
  
rand_list1=rand_int_list(len(guest1))
rand_list2=rand_int_list(len(guest2))
rand_list3=rand_int_list(len(guest3))


for i in range(5):
  print(f"{guest1[rand_list1[i][0]][0]} VS {guest1[rand_list1[i][1]][0]}")
print("-"*30)
for i in range(5):
  print(f"{guest2[rand_list2[i][0]][0]} VS {guest2[rand_list2[i][1]][0]}")
print("-"*30)
for i in range(5):
  print(f"{guest3[rand_list3[i][0]][0]} VS {guest3[rand_list3[i][1]][0]}")


  #print(f"{guest1[rand_list1[i][0]]} VS {guest1[rand_list1[i][0]]}")