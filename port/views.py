from django.db.models.query import QuerySet
from django.views import generic
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, get_object_or_404, render
from .forms import RegistroForm, UpdateMemberForm
from .filters import SearchFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from .models import Member, Proyects, Friends, Proyect_Finder

#View creada para poder mostrar buscar los usuarios en el template base
class searchBar(generic.ListView):
    model = Member
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['users'] = Member.objects.all()
        context['user'] = user
        print(user)
        return context


class Home(LoginRequiredMixin, generic.ListView):
    model = Proyects
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Tomo el usuario logueado.
        user = self.request.user
        #Filtro los amigos relacionados con ese usuario.
        friends = Friends.objects.filter(user=user).values_list('friend', flat=True)
        friend_users = Member.objects.filter(id__in=friends)
        #Traigo los proyectos que esten relacionados con mis amigos.
        project_friends = Proyects.objects.filter(proyect_user__in=friends).order_by('-date')
        
        #Paso el contexto.
        context['projects'] = project_friends
        context['friends'] = friend_users
        context['users'] = Member.objects.all()

        return context


class UserDetail(generic.DetailView):
    model = Member
    template_name = 'member.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['friends'] = Friends.objects.filter(user=user).values_list('friend', flat=True)
        #variables usadas para el boton de eliminar amigo
        member = get_object_or_404(Member, pk=self.kwargs['pk'])
        context['fri'] = Friends.objects.filter(user=user, friend=member).first()
        context['users'] = Member.objects.all()

        context['projects'] = Proyects.objects.all()
        return context


class UpdateMember(generic.UpdateView):
    model = Member
    template_name = 'member.html'
    form_class = UpdateMemberForm
    success_url = reverse_lazy('port:home')

    def form_valid(self, form):
        # Verificar si se proporciona una nueva contraseña
        new_password1 = form.cleaned_data.get('new_password1')
        if new_password1:
            # Si se proporciona una nueva contraseña, actualizarla
            self.object.set_password(new_password1)
            self.object.save()
            messages.success(self.request, 'Password updated successfully')

        # Actualizar el perfil del usuario
        response = super().form_valid(form)
        messages.success(self.request, 'Profile updated successfully')
        return response
    
    def form_invalid(self,form):
        print(form.errors)
        return super().form_invalid(form)

# class DeleteFriend(generic.DeleteView):
#     model = Friends
#     template_name = 'member.html'
#     success_url = reverse_lazy('port:home')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         member = get_object_or_404(Member, pk=self.kwargs['pk'])
#         context['fri'] = get_object_or_404(Friends, user=user, friend=member)
#         return context


class CreateProject(generic.CreateView):
    model = Proyects
    template_name = 'member.html'
    fields = [
        'proyect_user',
        'title',
        'img',
        'description',
        'coworker',
        'url_proyect',
        'url_repo'
    ]
    success_url = reverse_lazy('port:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Project created')
        return response
    
    def form_invalid(self,form):
        print(form.errors)
        return super().form_invalid(form)
    
    
class DeleteProject(generic.DeleteView):
    model = Proyects
    template_engine = 'member.html'
    success_url = reverse_lazy('port:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Project deleted')
        return response
    
    def form_invalid(self,form):
        print(form.errors)
        return super().form_invalid(form)




#BOTONES
    

#Boton en member para eliminar a seguidos.
def DeleteFriend(request, pk):
    user = request.user
    friends = Friends.objects.get(pk=pk)
    if friends: 
        friends.delete()
        messages.error(request, 'Friend deleted')
        return redirect(reverse_lazy('port:home'))


#Boton en member para agregar a seguidos.
def create_friend(request, pk):
    user = request.user
    member = get_object_or_404(Member, pk=pk)
    
    if user != member: 
        Friends.objects.create(user=user, friend=member)
        messages.success(request, 'Friend added')
        return redirect(reverse_lazy('port:home'))


#filtro para buscar usuarios.
# def searchView(request):
#     filter = SearchFilter(request.GET, queryset=Member.objects.all())
#     user = filter.qs
#     return render(request, 'home.html', context={'users': user})




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
        messages.success(self.request, '¡Account created! Please sign in.')
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