import csv
import requests

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRSwEE8anKsk21yNNi6mVELFMkmVETZVEmtie6oWh9QVtUXcE3O7zuxZJxhAQd3414FIrvRgx_zVPvm/pub?output=csv'
r = requests.get(url, allow_redirects=True)
open('tester.csv', 'wb').write(r.content)

gjest1 = []
gjest2 = []
gjest3 = []

with open(r'C:\Users\Freid\Documents\NTNU\Elsys\1. semester\tester.csv', mode='r', newline="") as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)
    csv_file.close()

print(data)
for i in data:
    if i[1] == "Gjest 1":
        gjest1.append(i[2])
    elif i[1] == "Gjest 2":
        gjest2.append(i[2])
    elif i[1] == "Gjest 3":
        gjest3.append(i[2])
    else:
        print("liste inneholder ikke 'Gjest #'.")

print(gjest1)
print(gjest2)
print(gjest3)

# dict_from_csv = pd.read_csv(r'C:\Users\Freid\Documents\NTNU\Elsys\1. semester\tester.csv', header=None, index_col=0, squeeze=True).to_dict()
# print(dict_from_csv)