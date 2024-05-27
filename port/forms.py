from .models import Member
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
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


class UpdateMemberForm(forms.ModelForm):
    profile_pic = forms.ImageField(label='Profile Picture')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    age = forms.DateField(label='Age', widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label='Email')
    SEX_OPTION = (
        ('1', 'Female'),
        ('2', 'Male')
    )
    sex = forms.TypedChoiceField(label='Sex', choices=SEX_OPTION, coerce=str)
    cv = forms.FileField(label='CV')
    about_me = forms.CharField(label='About Me', widget=forms.Textarea)
    searching = forms.BooleanField(label='Searching', initial=True, required=False)
    language = forms.CharField(label='Language', max_length=20)
    POSITION_OPTION = (
        ('1', 'Front-End'),
        ('2', 'Back-End')
    )
    position = forms.TypedChoiceField(label='Position', choices=POSITION_OPTION, coerce=str)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput, required=False)

    class Meta:
        model = Member
        fields = ['profile_pic', 'first_name', 'last_name', 'age', 'email', 'sex', 'cv', 'about_me', 'searching', 'language', 'position']

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 != new_password2:
            self.add_error('new_password2', "Passwords don't match")

        # Eliminar los campos de contraseña si no se proporciona una nueva contraseña
        if not new_password1:
            self.cleaned_data.pop('new_password1', None)
            self.cleaned_data.pop('new_password2', None)
            

        return cleaned_data