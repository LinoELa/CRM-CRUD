from django.db import models

# Create your models here.


class Record(models.Model):
    # para saber la hora que que se a creado
    created_at = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)


    """
    Hacemos un return de lo que queremo mostrar en la pantalla cuando 
    accedamods a unos de estos record o informacion de los modelos 
    """
    def __str__(self):
        # Hacemos un return de lo queremos devolver y que se vea despues 
        """ 
        Si llamamos llamamos a algunos de estos records va a devolver en 
        el admin area va a devolver el first name y last name
        """
        return(f"{self.first_name} {self.last_name}")
    



    """ 
    HACER UNA MIGRACION  : 
    Despues de crear el modelo lo siguiente en hacer es una migracion a la base de datos 


    - python mange.py makemigrations
    
    - python manage.py migrate

    """