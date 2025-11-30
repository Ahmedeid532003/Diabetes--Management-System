from django.db import models




# Create your models here.
class client(models.Model):
    UserName = models.CharField(max_length=20,unique=True)
    Name=models.CharField(max_length=30)
    Password = models.CharField(max_length=10,unique=True) 
    Email= models.EmailField(max_length=50)
    BirthDate = models.DateField(null=True)
    Stage1= models.CharField(max_length=50, null=True, blank=True)
    Stage2= models.CharField(max_length=50, null=True, blank=True)
    Stage3= models.CharField(max_length=50, null=True, blank=True)
    Stage4= models.CharField(max_length=50, null=True, blank=True)
    Stage5= models.CharField(max_length=50, null=True, blank=True)
    Stage6= models.CharField(max_length=50, null=True, blank=True)
    Stage7= models.CharField(max_length=50, null=True, blank=True)
    
    
    
    
    
class DiabetesPatient(models.Model):
    full_name = models.CharField(max_length=100)
    Dtype = models.CharField(max_length=50)
    age = models.IntegerField()
    hba1c = models.FloatField()
    weight = models.FloatField()
    height = models.FloatField()
    blood_pressure = models.FloatField(null=True, blank=True)
    cholesterol = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    pregnant = models.BooleanField(default=False)
    
  
    

    
    def __str__(self) :
        return self.UserName
    

