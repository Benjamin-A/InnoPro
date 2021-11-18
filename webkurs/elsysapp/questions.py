import csv
from operator import le
#from os import pardir
import requests
from random import randint
#fetch address of csv fil to corresponding guest
def fetch_guest_csv(guest):
  return "C:/Users/benja/Documents/Web-kurs/djangoprosjekt/webkurs/elsysapp/static/" + guest + '.csv'
#extract questions from a list
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
  open(fetch_guest_csv("raw_questions_from_Google"), 'wb').write(r.content)
  
  #read temporary csv
  data=read_csv(fetch_guest_csv("raw_questions_from_Google"))
  
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
#Calculate a new score for the list: wins divided by tries, rounded
def calc_score(question):
  #wins divided by tries, rounded
  return round( int(question[3])/int(question[1]),3)
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
    #print("-"*20 + "\n" + "Winner and loooser found" + "\n" + "-"*20)
    #increase viewes counter
    question_list[win_i][1]= int(question_list[win_i][1])+ 1
    question_list[loose_i][1]=int(question_list[loose_i][1])+1
    #increase win counter
    question_list[win_i][3]= int(question_list[win_i][3])+ 1
    #Update score
    question_list[win_i][4]= calc_score(question_list[win_i])
    question_list[loose_i][4]=calc_score(question_list[loose_i])
    #save changes
    write_csv(fetch_guest_csv(guest), question_list)
    #print("-"*20 + "\n" + "Winner and loooser written" + "\n" + "-"*20)
  else:
    print("Winner or Looser question not found")
    print(winner)  
    print(looser)  
#turns a boring list to a beautifull dictionary filled list
def dictionaryfy(list):
  myList = []
  for i in range(len(list)):
    myList.append({"question":list[i][0],"views":list[i][1],"time":list[i][2],"wins":list[i][3],"score":list[i][4]})
  return myList
#returns scoring used to sort results
def get_score(question):
    return question.get('score')
#returns ALL data, nicely sorted
def show_results():
  #fetch data
  guest1_raw_data = read_csv(fetch_guest_csv("guest1"))
  guest2_raw_data = read_csv(fetch_guest_csv("guest2"))
  guest3_raw_data = read_csv(fetch_guest_csv("guest3"))
  #make array of dictionary
  guest1_data = dictionaryfy(guest1_raw_data)
  guest2_data = dictionaryfy(guest2_raw_data)
  guest3_data = dictionaryfy(guest3_raw_data)
  #sort array by score, ascending
  guest1_data.sort(key=get_score, reverse=True)
  guest2_data.sort(key=get_score, reverse=True)
  guest3_data.sort(key=get_score, reverse=True)
  #combine lists
  list_o_guests=[[guest1_data,"Sigrid"],[guest2_data,"Hans Majestet Kong Harald V"],[guest3_data, "Henrik Ingebrigtsen"]]
  
  return list_o_guests
#reset score of chosen list
def reset_score(guest):
  question_list= read_csv(fetch_guest_csv(guest))
  for i in range(len(question_list)):
    #Reset counter,wins and score
    question_list[i][1]=0
    question_list[i][3]=0
    question_list[i][4]=0
  write_csv(fetch_guest_csv(guest), question_list)
#resets score of all lists
def reset_all_scores():
  reset_score("guest1")
  reset_score("guest2")
  reset_score("guest3")


