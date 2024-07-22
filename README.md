# CRM-CRUD


#### Iniciar Secion en la base de datos 



#### <!-- -----------------INFORMACION GENERAL ---------------  -->
- Podemos usar el nombre para puntar a una direccion o Url 
- NO ASI 
    > href="{% url 'home'%}"
        - home.html
- MEJOR Y SI QUE FUNCIONA : Usamos el nombre
    >  href="{% url 'home'%}"
        - home
        
    - En vez de 





#### <!-- ----------------- AUTENTIFICACION ---------------  -->

- Importar la autentificacion
    > from django.contrib.auth import authenticate, login , logout
- Importar para los mensajes al hacer un login o un logout 
    > from django.contrib import messages