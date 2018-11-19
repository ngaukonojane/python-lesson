from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    IntegerField,
                    OperationalError,
                    IntegrityError)
db = SqliteDatabase("contact.db")
contacts = [
    {'id': 1,'email': 'john@doe.com', 'name': 'felician','phone':'0712282129'},
    {'id': 2,'email': 'john@doe.com', 'name': 'felician','phone':'0712282129'}
    
    
    
]



class Contact(Model):
    
    
    name = CharField(max_length=200)
    amount= IntegerField(default=10)
    action=CharField(max_length=200)

    class Meta:
        database = db

def initialize():
    try:
        Contact.create_table()
    except OperationalError:
        pass
    for contact in contacts:
      try:
        Contact.create(
            name=contact.get('name'),
            amount=contact.get('amount'),
            action=contact.get('option'),
           
            )
      except IntegrityError:
        pass
    


