# CRM-CRUD


#### <!-- ----------------- Iniciar Secion en la base de datos  ---------------  -->


```
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'dbELA',
        'USER' : 'root',
        'PASSWORD' : 'mysql@123',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}
```
#### <!-- -----------------SUPERUSER  ---------------  -->

- ela
- 123456789


#### <!-- ----------------- URLs ---------------  -->

urlpatterns = [
    path('' , views.home, name='home'),
    # si quiero crear una pagina separada de log in solo quitar el comentario
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]


#### <!-- ----------------- AUTENTIFICACION ---------------  -->

Para hacer los login y logout

- Importar la autentificacion
    > from django.contrib.auth import authenticate, login , logout

- Importar para los mensajes al hacer un login o un logout 
    > from django.contrib import messages



#### <!-- -----------------INFORMACION GENERAL ---------------  -->
- Podemos usar el nombre para puntar a una direccion o Url 
- NO ASI 
    > href="{% url 'home'%}"
        - home.html
- MEJOR Y SI QUE FUNCIONA : Usamos el nombre
    >  href="{% url 'home'%}"
        - home
        
    - En vez de 

- Siempre hay 3 pasos en DJANGO que siempre vas a necesitar 
    - view o vista 
    - Plantilla (ej : home.html)
    - URL

#### <!-- ----------------- REGISTRO DE USUARIOS ---------------  -->

- Primero creamos la url - views - template 

- Creamos el forms.py 

- Completamos la logica de forms.py

 - Si el método de la solicitud no es POST, renderizamos el formulario vacío
    - -  para evitar : "The view appwebsite.views.register_user didn't return an HttpResponse object. It returned None instead."

    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})




    - Revisar bien los nombres de las variables que sean los mismo, porque si no lleva a un error faltal

#### <!-- -------- MODELOS  PARA LA ADMIN &  BASE DE DATOS ------------  -->
- No hace falta que escribamos codigo para la base de datos , Django ya lo escribe 

def __str__(self):
    Hacemos un return de lo que queremo mostrar en la pantalla cuando accedamods a unos de estos record o informacion de los modelos 


- Despues de crear el modelo lo traemos a admin.py para asi poder verlo en la seccion de admin

    > from django.contrib import admin
    from .models import Record
    #para registrar el record en admin
    > admin.site.register(Record)

- Luego de crearlo el modelo  y vincularlo al admin,  ya se puede ir a la ala web de /admin y desde alli añadir los modelos  



#### <!-- -------- VER DE LOS MODELOS EN LA PAGINA WEB ------------  -->

- Como queremos que aparezca cuando el usuario este logueado






