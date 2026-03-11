from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import *
from .models import *
# Create your views here.

def login(request):
  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      auth_login(request, user)
      print('Login successful!')
      return redirect('/index')
    else:
      print("Login failed!")
  else:
    form = LoginForm()
  
  context = {'form': form}
  return render(request, 'pages/sign-in.html', context)

def index(request):
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'pages/index.html', context)

def dynamic_api(request):
    context = {
        'segment': 'dynamic_api'
    }
    return render(request, 'dyn_api/index.html', context)

def clientes(request):
    clientes = Cliente.objects.all()
    tipo = tipo_documnento.objects.all()
    context = {
        'segment': 'clientes',
        'clientes': clientes,
        'tipos_documento': tipo
    }
    return render(request, 'Clientes/index.html', context)

def registrar_clientes(request):
    if request.method == 'POST':
        id_tipo_doc = request.POST.get('tipo_documento')
        numero_documento = request.POST.get('numero_documento')
        nombre = request.POST.get('nombre_apellido')
        
        email = request.POST.get('email')
        telefono = request.POST.get('telefono') 
        direccion = request.POST.get('direccion')
        fecha_registro = request.POST.get('fecha_registro')
        esta_activo = True if request.POST.get('activo') == '1' else False
        
        
        try:
           new_client = Cliente.objects.create(
                tipo_documento_id=id_tipo_doc,
                numero_documento=numero_documento,
                nombre=nombre,
                apellidos="",
                email=email,
                telefono=telefono,
                direccion=direccion,
                fecha_registro=fecha_registro,
                activo=esta_activo
            )
           new_client.save()
           print('Client created successfully!')
           return redirect('/clientes')
        except Exception as e:
            print(f"Error creating client: {e}")
            return redirect('/index')
    else:
        print("Invalid request method!")
        return redirect('/index')

def charts(request):
    context = {
        'segment': 'charts'
    }
    return render(request, 'charts/index.html', context)

def tables(request):
    usuarios = User.objects.all()
    context = {
        'segment': 'tables',
        'usuarios': usuarios
    }
    return render(request, 'pages/tables.html', context)

def registrar_usuario(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not email or not password or not first_name or not last_name:
            print("All fields are required!")
            return redirect('/index')
        try:
            new_user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            new_user.save()
            print('User created successfully!')
            return redirect('/tables')
        except Exception as e:
            print(f"Error creating user: {e}")
            return redirect('/index')
    else:
        print("Invalid request method!")
        return redirect('/index')
        
    


def billing(request):
    context = {
        'segment': 'billing'
    }
    return render(request, 'pages/billing.html', context)

def virtual_reality(request):
    context = {
        'segment': 'virtual_reality'
    }
    return render(request, 'pages/virtual-reality.html', context)

def rtl(request):
    context = {
        'segment': 'rtl'
    }
    return render(request, 'pages/rtl.html', context)

def notifications(request):
    context = {
        'segment': 'notifications'
    }
    return render(request, 'pages/notifications.html', context)

def profile(request):
    context = {
        'segment': 'profile'
    }
    return render(request, 'pages/profile.html', context)


def map(request):
    context = {
        'segment': 'map'
    }
    return render(request, 'pages/map.html', context)

def typography(request):
    context = {
        'segment': 'typography'
    }
    return render(request, 'pages/typography.html', context)

def icons(request):
    context = {
        'segment': 'icons'
    }
    return render(request, 'pages/icons.html', context)

def template(request):
    context = {
        'segment': 'template'
    }
    return render(request, 'pages/template.html', context)




# def register(request):
#   if request.method == 'POST':
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#       form.save()
#       print('Account created successfully!')
#       return redirect('/accounts/login/')
#     else:
#       print("Registration failed!")
#   else:
#     form = RegistrationForm()
  
#   context = {'form': form}
#   return render(request, 'pages/sign-up.html', context)


# class UserPasswordResetView(auth_views.PasswordResetView):
#   template_name = 'accounts/forgot-password.html'
#   form_class = UserPasswordResetForm


# class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
#   template_name = 'accounts/recover-password.html'
#   form_class = UserSetPasswordForm


# class UserPasswordChangeView(auth_views.PasswordChangeView):
#   template_name = 'accounts/password_change.html'
#   form_class = UserPasswordChangeForm


def user_logout_view(request):
  logout(request)
  return redirect('login')