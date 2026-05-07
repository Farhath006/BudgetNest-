from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class FamilyData(models.Model):
    family_lead=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    income=models.FloatField()

    class Meta:
        db_table='family_data'

    def __str__(self):
        return self.name




class ExpensesData(models.Model):
    family_lead=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.ForeignKey(FamilyData,on_delete=models.CASCADE)
    purpose=models.CharField(max_length=100)
    expense=models.FloatField()
    date=models.DateField(null=True,blank=True)


    def __str__(self):
        return self.name