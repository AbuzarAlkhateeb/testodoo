
import json

class Info(object):
	def __init__(self, name,email , phone):
		self.name = name 
		self.email = email
		self.phone = phone

	@staticmethod
	def convertToObj(str):
		objInfo =  str.split(" / ")
		newObj =  Info(objInfo[0],objInfo[1],objInfo[2]);
		return newObj


class Contacts(Info):
	pass
	



class Leads(Info):
	pass

contacts = """Alice Brown / None / 1231112223
Bob Crown / bob@crowns.com / None
Carlos Drew / carl@drewess.com / 3453334445
Doug Emerty / None / 4564445556
Egan Fair / eg@fairness.com / 32112d34567"""


leads = """None / kevin@keith.com / None
Lucy / lucy@liu.com / 3210001112
Mary Middle / mary@middle.com / 3211234567
None / None / 4442223334
None / ole@olson.com / None"""

def matchPhone(listarg , phone):
	return phone in [x.phone for x in listarg]
def matchEmail(listarg , email):
	return email in [x.email for x in listarg]
def indexPhone(listarg , phone):
	return [x.phone for x in listarg].index(phone)
def indexEmail(listarg , email):
	return [x.email for x in listarg].index(email)
contactsList =  [Contacts.convertToObj(x) for x in contacts.split("\n") ]
leadsList =  [Leads.convertToObj(x) for x in leads.split("\n") ]
# print(matchPhone(leadsList,"4442223334"))
with open('registrant.json') as f:
	data = json.load(f)
print(contactsList)
match_phone = matchPhone(contactsList,data['registrant']['phone']) 
match_email = matchEmail(contactsList,data['registrant']['email'])
if(not match_email):
	if(not match_phone):
		match_phone = matchPhone(leadsList,data['registrant']['phone']) 
		match_email = matchEmail(leadsList,data['registrant']['email'])
		if(match_phone):
			index_phone = indexPhone(leadsList,data['registrant']['phone'])
			contactsList.append(leadsList.pop(index_phone))
		if(match_email):
			index_email = indexEmail(leadsList,data['registrant']['email'])
			contactsList(leadsList.pop(index_email))
		else:
			contact =  Contacts(data['registrant']['name'],data['registrant']['email'],data['registrant']['phone'])
			contactsList.append(contact)



print(contactsList)
