from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistroForm
from .models import Member, Proyects, Friends, Proyect_Finder

class Home(generic.ListView):
    model = Proyects
    template_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Tomo el usuario logueado.
        user = self.request.user
        #Filtro los amigos relacionados con ese usuario.
        friends = Friends.objects.filter(user=user).values_list('friend', flat=True)
        #Traigo los proyectos que esten relacionados con mis amigos.
        project_friends = Proyects.objects.filter(proyect_user__in=friends).order_by('date')
        
        #Paso el contexto.
        context['projects'] = project_friends

        return context



# Login 
class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales no validas.')        
        return super().form_invalid(form)


# register.
class SingUpView(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('port:login')
    template_name = 'register.html'

    def form_valid(self, form):        
        response = super().form_valid(form)
        messages.success(self.request, '¡Tu cuenta ha sido creada! Por favor inicia sesión.')
        return response
            
    def form_invalid(self, form):
       
        response = super().form_invalid(form)
        
        # Obtén los errores del formulario
        errors = form.errors.get_json_data()

        # Recorre los errores y muestra los mensajes de error
        for field, field_errors in errors.items():
            for error in field_errors:
                messages.error(self.request, f'{field.capitalize()}: {error["message"]}')

        return response