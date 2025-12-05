from django.db import models
from django.conf import settings

# Create your models here.
class Orszag(models.Model):
    Nev = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.Nev

class Telepules(models.Model):
    Nev = models.CharField(max_length= 255, null=False)
    OId = models.ForeignKey(Orszag,on_delete=models.CASCADE)

    def __str__(self):
        return self.Nev

class Latvanyossag(models.Model):
    Nev = models.CharField(max_length= 255, null=False)
    RLeiras = models.TextField(null = False)
    VId = models.ForeignKey(Telepules,on_delete=models.CASCADE)
    AtlagErtekeles = models.DecimalField(default=0.5,max_digits=5, decimal_places=2, null = False)
    Nyitvatartas = models.CharField(max_length=255, null=False,  default="H-P: 07-19, SZ: 10-14, V: zárva")
    URL = models.URLField()

    def __str__(self):
        return self.Nev

class Hozzaszolasok(models.Model):
    Iro = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Megjegyzes = models.TextField(null = False)
    LId = models.ForeignKey(Latvanyossag,on_delete=models.CASCADE)

    def __str__(self):
        return self.LId+":"+self.Iro+"("+str(self.Megjegyzes)+")"