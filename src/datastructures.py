
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"id":self._generateId(),
            "first_name": "Juan",
            "last_name":self.last_name,
            "age": 19,
            "lucky_numbers":[1,27,42]
            },


              {"id":self._generateId(),
            "first_name": "Juana",
            "last_name":self.last_name,
            "age": 42,
            "lucky_numbers":[65,77,1]
            }, 
            
             {"id":self._generateId(),
            "first_name": "Juanito",
            "last_name":self.last_name,
            "age": 12,
            "lucky_numbers":[8]
            },   ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
                aux_member={}
                aux_member['id']= int(member['id'])
                aux_member['first_name']=str(member['first_name'])
                aux_member['last_name']=self.last_name
                aux_member['age']=int(member['age'])
                aux_member['lucky_numbers']= member['lucky_numbers']
                self._members.append(aux_member)
                pass

    def delete_member(self, id):
        # fill this method and update the return
        for i in self._members:
            if i["id"] == id:
               return i
        pass

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
         if member['id'] == id :
             return member
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members