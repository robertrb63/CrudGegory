
import pathlib
import json

# ESTA CLASE ES PARA LEER LA RUTA DEL ARCHIVO JSON
class ManageDb:
    __addres_file = "{0}/src/db/dbContacts.json".format(pathlib.Path().absolute())
    def read_contacts(self):
        with open(self.__addres_file, "r") as data:
            return json.loads(data.read())       
#md = ManageDb()       
#print(md.read_contacts())   
    def write_contacts(self, new_data):
        with open(self.__addres_file, "w") as data:
            data.write(json.dumps(new_data))