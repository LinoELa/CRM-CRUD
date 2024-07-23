from django.shortcuts import render

#importamos httpresponse para que lo devuelva en la visa 
# from django.http import HttpResponse

# Para redireccionar al a pantalla principal
from django.shortcuts import redirect

# Para la autentificacion 
from django.contrib.auth import authenticate, login , logout

#Mensaje al hacer un log in o un log out 
from django.contrib import messages


# imprtamos la clase que esa en el forms 
from .forms import SignUpForm


# Importamos el modelo primero
from .models import Record




# ------------------------- HOME ----------------------------------#

# Create your views here.

def home(request):

    # Para que el records se vea 
    records = Record.objects.all()

    # Chekear si esta logueado - 
    #usando excepciones

    # Cuando postean algo por eso el metodo POST
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar usuario para saber si es correcto o no 
        user = authenticate(request, username=username, password=password)

        #Para verificar que es valido usuario y que ha iniciado session
        if user is not None:
            login(request, user)
            messages.success(request, 'Enhorabuena, has Iniciar Session!')

            #Redirecionar a la pagina principal al iniciar session
            return redirect('home')
        else:
            messages.error(request, 'Hubo un error al intentar iniciar session, Porfavor Intentalo de nuevo ')

    """ 
    - Pero cuando no postean nada para que vean la pagina

    - Pasamos records para que puedan ve los records
    """
    return render(request, "home.html", {'records' : records})
    
# --------------------------- LOGIN --------------------------------#

# ya l cree pero en la pagian principal
# def login_user(request):
#     pass
# ---------------------------- LOGOUT -------------------------------#


def logout_user(request):
    logout(request)
    messages.success(request, 'Has cerrado session')

    return redirect('home')



# ---------------------------- REGISTER  O REGISTROS-------------------------------#

def register_user(request):

    #cuando estas o han rellenado el formulacio
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()

            # autenticar usuario
            username = form.cleaned_data['username'] # luego lo asigamos aser
            password = form.cleaned_data['password1'] #luego se asigna como password simple a user 

            user = authenticate(request, username=username, password= password)

            # Verificar si user es valido  y no un None
            if user is not None: 
                #si funciona bien pues iniciamos session
                login(request, user)

                #al iniciar sesion que aparezca un mensaje
                messages.success(request, 'Tu registro se ha realizado con exito')

                #luego le devolvemos a la pagina principal
                return redirect ('home')
            # Verificar si user es None o NO ES VALIDO
            else:
                messages.error(request, 'Hubo un problema al iniciar sesión. Por favor, inténtalo de nuevo.')
                return redirect('register')
            
        
        #Si el formulario no es valido
        else:
            # Depuración: imprimir errores en la consola
            print(form.errors)

            messages.error(request, 'Por favor corrige los errores en tu formulario')
            return render(request, 'register.html', {'form':form})
        
    # Si el método de la solicitud no es POST, renderizamos el formulario vacío
    # para evitar : The view appwebsite.views.register_user didn't return an HttpResponse object. It returned None instead.
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})


    


    

# ---------------------------- RECORDS : VISTA ----------------------#

def customer_record(request, pk):
    #si el usuario esta autenticado o ha hecho un log in
    if request.user.is_authenticated:
        # Buscar los Customer Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    #Si el usuario NO ESTA AUTENTICADO 
    else:
        messages.error(request, 'Tienes que iniciar session' )
        return redirect ('home')


# ---------------------------- BORRAR O DELETE RECORD -------------------------#


def delete_record(request, pk):
    #si el usuario esta autenticado o ha hecho un log in
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()  
        messages.error(request, 'Se ha borrado corectamente el record' )
        return redirect ('home')
        #Si el usuario NO ESTA AUTENTICADO 
    else:
        messages.error(request, 'Tienes que iniciar session' )
        return redirect ('home')






# ---------------------------- LOGOUT -------------------------------#

# ---------------------------- LOGOUT -------------------------------#
