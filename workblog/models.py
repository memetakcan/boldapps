from django.db import models
import datetime

# Create your models here.



class Workchart(models.Model):
    user = models.ForeignKey('auth.User',default=1,verbose_name='Yazar',on_delete=models.SET_DEFAULT)
    project_list = ["003-EAP","004-SCP","030-EHP","036-IUA"]
    projectpartlist = ["MSTR","TW01","TW02","TW03","TW04","IFMS","IFA0","IFB0","IFC0","MFMS","MFA0","MFB0","MFC0","DBE0"]
    project = models.TextField(max_length=120, verbose_name="Proje",null="True")
    contentlist = ["Design Review","Publishing","4D Modeling","Modeling","Documentation","Meeting","Site Inspection","Clash Detection",
               "3D Control and Planning","Dimensioning","3D Coordination","Code Validation","Energy Analysis","Digital Asset Management","Programming"]
    content = models.CharField(max_length=120, verbose_name="Content")
    projectpart = models.CharField(max_length=120, verbose_name="datesection")
    publishingdate = models.DateTimeField(verbose_name="Tarih", auto_now_add=True)
    section = models.CharField(max_length=120, verbose_name="datesection")
    datetime = models.DateField(verbose_name="datetime", null="True")

    contentlist.sort()
    project_list.sort()
    projectpartlist.sort()
    #içeriği string haline getiriyor

    def __str__(self):
        return self.project

    class Meta:
        ordering=["-datetime"]

#get absolute url 17. veya 18. ders