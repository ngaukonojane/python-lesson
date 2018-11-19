from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    DateTimeField,
                    IntegrityError,
                    IntegerField,
                    OperationalError
                    )

db = SqliteDatabase("farmers.db")

farmers = [
    {'id':1,'username':'janelodipo', 
     'email':'janelodipo@gmail.com',
    'phone':'0720355780', },
    {'id':2, 'username':'fredomondi', 
   'email':'fredomondi@gmail.com',
    'phone':'0725867534', },
     {'id':3, 'username':'marianjeri', 
   'email':'marianjeri@gmail.com',
    'phone':'0792756428', }, 
     {'id':4, 'username':'ericotieno', 
   'email':'ericotieno@gmail.com',
    'phone':'0725867534', },
    
]


class Farmer(Model):

  username = CharField(max_length=200)
  
  email = CharField(max_length=50,unique=True)
  phone = IntegerField(default=10)
 
 


  class Meta:
        database = db


def initialize():
    try:
        Farmer.create_table()
    except OperationalError:
        pass
    for farmer in farmers:
      try:
        Farmer.create(
            username=farmer.get('username'),             
            email=farmer.get('email'),
            phone=farmer.get('phone'),
            
           
            
            )
      except IntegrityError:
        pass
    
