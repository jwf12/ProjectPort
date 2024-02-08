from .models import Member
from django import forms
from django.contrib.auth.forms import UserCreationForm



#Creacion de usuario
class RegistroForm(UserCreationForm):
    profile_pic = forms.ImageField(label='pic')
    first_name = forms.CharField(label='Name', )
    last_name = forms.CharField(label='Last-name', )
    age = forms.DateField(label='age', widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField()
    SEX_OPTION = (
        ('1','Female'),
        ('2', 'Male')
    )
    sex = forms.TypedChoiceField(label='Sex', choices=SEX_OPTION, coerce=str)
    cv = forms.FileField(label='cv')
    about_me = forms.CharField(label='about', widget=forms.Textarea)
    searching = forms.BooleanField(label='searching', initial=True)
    language = forms.CharField(label='language', max_length=20)
    POSITION_OPTION = (
        ('1', 'Front-End'),
        ('2', 'Back-End')
    )
    position = forms.TypedChoiceField(label='position', choices=POSITION_OPTION, coerce=str)
    password1 = forms.CharField(label='password',widget = forms.PasswordInput, )
    password2 = forms.CharField(label='confirm-password',widget = forms.PasswordInput, )
    class Meta:
        model = Member
        fields = [
            'username',    
            'profile_pic',        
            'first_name',
            'last_name',
            'age',
            'email',
            'sex',
            'cv',
            'about_me',
            'searching',
            'language',
            'position',
            'password1',
            'password2',        
        ]