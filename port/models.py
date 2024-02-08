from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



# Create your models here.
class Member(AbstractUser):
    profile_pic = models.ImageField(upload_to="media/images", blank=True, null=True)
    first_name = models.CharField(max_length=100, verbose_name='Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    age = models.DateField( blank=True, null=True)
    email = models.EmailField(max_length=254)
    SEX_OPTION = (
        ('1', 'Female'),
        ('2', 'Male')
    )
    sex = models.CharField(max_length=1, choices=SEX_OPTION, verbose_name='Sex')
    cv = models.FileField(upload_to="media/cv", blank=True, null=True)
    about_me = models.TextField(verbose_name='About', blank=True, null=True)
    searching = models.BooleanField(default=True, verbose_name='Searching')
    language = models.CharField(max_length=20, verbose_name='Language')
    POSITION_OPTION = (
        ('1', 'Front-End'),
        ('2', 'Back-End')
    )
    position = models.CharField(max_length=10, choices=POSITION_OPTION, verbose_name='Position')
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    

class Friends(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(Member,  on_delete=models.CASCADE, related_name='friend_friends')

    def __str__(self):
        return f"{self.friend.username}"

class Proyects(models.Model):
    proyect_user = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to="media/images/proyects")
    description = models.TextField()
    coworker = models.ForeignKey(Friends, on_delete=models.CASCADE, blank=True, null=True)
    url_proyect = models.URLField(blank=True)
    url_repo = models.URLField(blank=True)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title


class Proyect_Finder(models.Model):
    user_finder = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField()
    POSITION_OPTION = (
        ('1', 'Front-End'),
        ('2', 'Back-End')
    )
    position = models.CharField(max_length=10, choices=POSITION_OPTION)
    LANGUAGE_OPTION = (
        ('1', 'Python'),
        ('2', 'Java'),
        ('3', 'JavaScript'),
        ('4', '.Net'),
        ('5', 'Rust'),
        ('6', 'PHP'),
    )
    language = models.CharField(max_length=20, choices=LANGUAGE_OPTION)

    def __str__(self):
        return self.title