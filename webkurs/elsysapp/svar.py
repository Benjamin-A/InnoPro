import csv
from operator import le
#from os import pardir
import requests
from random import randint
#fetch address of csv fil to corresponding guest
def fetch_guest_csv(guest):
  return "C:/Users/benja/Documents/Web-kurs/djangoprosjekt/webkurs/elsysapp/static/" + guest + '.csv'
def extract_q(list):
  q_list=[]
  for i in range(len(list)):
    q_list.append(list[i][0])
  return q_list
#csv writing function
def write_csv(file_path, list):
  with open(file_path, 'w', newline="") as f: 
    write = csv.writer(f) 
    write.writerows(list)
    f.close()
#csv reading function    
def read_csv(file_path):
  with open(file_path, 'r', newline="") as f: 
    res = list(csv.reader(f)) 
    f.close()
  return res 
#compares all questions from Google forms and old questions and adds the new q
def update_q():
  #fetching current questins & score list 
  guest1 = read_csv(fetch_guest_csv("guest1"))
  guest2 = read_csv(fetch_guest_csv("guest2"))
  guest3 = read_csv(fetch_guest_csv("guest3"))
  
  #make lists only containing old questions
  guest1_q = extract_q(guest1)
  guest2_q = extract_q(guest2)
  guest3_q = extract_q(guest3)
  
  #fetch new (and old) questions and write to temporary csv
  url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRSwEE8anKsk21yNNi6mVELFMkmVETZVEmtie6oWh9QVtUXcE3O7zuxZJxhAQd3414FIrvRgx_zVPvm/pub?output=csv'
  r = requests.get(url, allow_redirects=True)
  open(fetch_guest_csv("tester"), 'wb').write(r.content)
  
  #read temporary csv
  data=read_csv(fetch_guest_csv("tester"))
  
  #add new questions to old questions, whilst avoiding duplicates
  for i in data:
      if i[1] == "Gjest 1" and  (i[2] not in guest1_q):
        guest1.append([i[2],0,i[0],0,0])
      elif i[1] == "Gjest 2"  and  (i[2] not in guest2_q):
        guest2.append([i[2],0,i[0],0,0])
      elif i[1] == "Gjest 3" and  (i[2] not in guest3_q):
        guest3.append([i[2],0,i[0],0,0])
      else:
          continue
  #write to corresponding csv
  write_csv(fetch_guest_csv("guest1"), guest1)
  write_csv(fetch_guest_csv("guest2"), guest2)
  write_csv(fetch_guest_csv("guest3"), guest3)
#generate list of random numbers for each guest
def rand_int_list(length):
  res = []
  for i in range(5):
    rand_a=randint(0,length-1)
    rand_b=randint(0,length-1)
    
    while True:
      if length==1:
        break
      elif rand_a==rand_b:
        rand_a = randint(0,length-1)
        rand_b = randint(0,length-1)
      else:
        break
    res.append([rand_a,rand_b])
  
  return res
#returns list with 5 pairs of random questions
def spm(guest):
  #fetching current questions & score list 
  question_list = read_csv(fetch_guest_csv(guest))
  rand_list=rand_int_list(len(question_list))
  res=[]
  #generate questions 
  for i in range(5):
    res.append([[question_list[rand_list[i][0]][0]],[question_list[rand_list[i][1]][0]]])
  return res
  
def spm1():#spm(guest1)
  spm("guest1")
  return "abc"
def spm2():#spm(guest1)
  spm("guest1")
def spm3():#spm(guest1)
  spm("guest1")
#edits score of winner(+2) and looser(-1) question in guest's csv file
def edit_score(guest,winner,looser):
  question_list = read_csv(fetch_guest_csv(guest))
  win_i="err"
  loose_i="err"
  for i in range(len(question_list)):
    if question_list[i][0]==winner:
      win_i=i
      break
  for i in range(len(question_list)):
    if question_list[i][0]==looser:
      loose_i=i
      break
  if win_i!="err" and loose_i!="err":
    print("-"*20 + "\n" + "Winner and loooser found" + "\n" + "-"*20)
    #increase viewes counter
    question_list[win_i][1]= int(question_list[win_i][1])+ 1
    question_list[loose_i][1]=int(question_list[loose_i][1])+1
    #increase win counter
    question_list[win_i][3]= int(question_list[win_i][3])+ 1
    #Update score
    question_list[win_i][4]= int(question_list[win_i][3])/int(question_list[win_i][1])
    question_list[loose_i][4]=int(question_list[loose_i][3])/int(question_list[loose_i][1])
    #save changes
    write_csv(fetch_guest_csv(guest), question_list)
    print("-"*20 + "\n" + "Winner and loooser written" + "\n" + "-"*20)
  else:
    print("Winner or Looser question not found")
    print(winner)  
    print(looser)  


