
from django.db import models
from multiselectfield import MultiSelectField

from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
	ROLE =(('Customer','Customer'),('Astrologer','Astrologer'),)
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	profile_pic =  models.ImageField(default="imansyah-muhamad-putera-KchIV_GDy6U-unsplash.jpg", null=True, blank=True)
	user_role = models.CharField(max_length=30,choices=ROLE)

	def __str__(self):
		return self.user.username

class Astro_Profile(models.Model):
	LANGUAGES = (('English','English'),('Hindi','Hindi'),('Gujarati','Guarati'),('Marathi','Marathi'),('Tamil','Tamil'))
	SKILLS = (    
	    ('Electional astrology','Electional astrology'),
        ('Horary astrology','Horary astrology'),
        ('Horoscopic astrology','Horoscopic astrology'),
        ('Indian astrology','Indian astrology'),
        ('Tibetan astrology','Tibetan astrology'),
        ('Western astrology','Western astrology'),
        ('Tropical astrology','Tropical astrology'),
        ('Agricultural astrology','Agricultural astrology'),
        ('Numerology','Numerology'),
        ('Tarot divination','Tarot divination'),
        ('Financial astrology','Financial astrology'),
        ('Locational astrology','Locational astrology'),
        ('Psychological astrology','Psychological astrology'),
        ('Sun sign astrology','Sun sign astrology'),
    )
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	skill = MultiSelectField(choices=SKILLS,max_choices=5)
	language = MultiSelectField(choices=LANGUAGES,max_choices=5)
	experience = models.IntegerField()
	location = models.CharField(max_length=200)
	about = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.profile.user.username


class Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	balance = models.IntegerField(default=100)
	def __str__(self):
		return self.user.username


class Review(models.Model):
	RATINGS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.CASCADE)
	reviewer = models.CharField(default="good",max_length=200) 
	post = models.CharField(max_length=200,null=True)
	star = models.CharField(max_length=10,choices=RATINGS)
	