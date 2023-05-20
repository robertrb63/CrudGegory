from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid
from pydantic import BaseModel
from src.lb.managedb import ManageDb

class ContactModel(BaseModel): #ESQUEMA QUE PERMITE INGRESAR NUEVOS USUARIOS
    id:str = str(uuid)
    name:str
    phone: str

app=FastAPI()

md = ManageDb()

@app.get("/")
def root():
    return {"message":"Hola FastaApi" }


@app.get("/api/contacts")
def get_all_contacts():
    return md.read_contacts()

@app.get("/api/contacts/{id_contact}")
def get_single_contact(id_contact:str):
    contacts = md.read_contacts()
    
    for contact in contacts:
        if contact["id"] == id_contact:
            return contact
    raise HTTPException(status_code=401, detail="Contact no found")

@app.post("/api/contacts/api/contacts/api/contacts")
def add_contact(new_contact:ContactModel): 
    contacts = md.read_contacts()
    new_contact = new_contact.dict()
    contacts.append(new_contact)
    
    md.write_contacts(contacts)
    print(contacts)
    return{
        "succes":"True",
        "message":"Added new Contact"
    }


@app.put("api/contacts/{id_contact}")
def update_contact(id_contact:str, new_contact:ContactModel):
    contacts = md.read_contacts()
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = new_contact.dict()
            md.write_contacts(contacts)
            
            return {
                "succes":"True",
                "message":"Updated Contactt"
                }
    raise HTTPException(status_code=404, detail="Contact no found")



@app.delete("/appi/contacts/{id_contact}")
def remove_contact(id_contact:str):
    contacts = md.read_contacts()
    
    for index, contact in enumerate(contacts):
        if contact ["id"] == id_contact:
            contacts.pop(index)
            md.write_contacts(contacts)
            
            return {
                "succes":"True",
                "message":"Deleted Contact"
                }
    raise HTTPException(status_code=404, detail="Contact no found")


  
