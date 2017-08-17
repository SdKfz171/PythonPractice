
from pip._vendor import requests
import json

url = "http://localhost:4872/api/MemberTables"

while True:

	print("ID :",end=' ')
	id = input()

	print("PW :",end=' ')
	pw = input()

	print("Name :",end=' ')
	name = input()

	header = {'ID':id,'PW':pw,'Name':name}

	r = requests.post(url,header)

	print(r.text)
	print();