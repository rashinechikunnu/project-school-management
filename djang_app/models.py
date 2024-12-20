from django.db import models

# Create your models here.
class school(models.Model):
    study_name =  models.CharField(max_length=200)
    study_Description = models.CharField(max_length=200)
    study_category =(
                    (1,"phase I"),
                    (2,"phase II"),
                    (3,"phase III"),
                    (4,"phase IV")
                                 
    )
    study_phase = models.IntegerField(choices=study_category,null=True,blank=True)
    Sponsor_Name  = models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.name
    
