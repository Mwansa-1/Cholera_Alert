from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Number of cases in the country needs to have a model the provinces . On the Home page the deaths and the cures will show as a total for the country. This part will be implemented in the views.
class Provinces(models.Model):
    province = models.TextField(max_length=50)
    positive_cases = models.CharField(max_length=10000)
    deaths = models.CharField(max_length=10000)
    cures = models.CharField(max_length=10000)

    def __str__(self):
        return self.province
    

# A blog model is needed for the blog section

class Blog(models.Model):
    image = models.ImageField(upload_to='images/blog')
    title = models.CharField(max_length=50)
    details = models.TextField(max_length=700)
    sources = models.CharField(max_length=50)
    authors = models.TextField(max_length=750)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    #Your Model Identity
    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")
  
    

# A report model is needed for the report section 

class Alert(models.Model):
    location = models.CharField(max_length=50)
    details = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

#For adding tests the user will choose whether to use the device or to submit the results. A model will be required for each of them.
#submit
class Submitted_Results(models.Model):
    result= models.BooleanField(blank=True, null=True)
    location = models.TextField(max_length=50)
    image = models.ImageField(upload_to='images/submitted_results')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

#test with device
class Device_Results(models.Model):
    image = models.ImageField(upload_to='images/device_results')
    result = models.BooleanField(blank=True, null=True)
    location = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

# A test model to show the previous tests
class Previous_Test(models.Model):
    test = models.TextField(max_length=50 , blank=True, null=True)
    submitted = models.ForeignKey('Submitted_Results',on_delete=models.CASCADE,blank=True, null=True)
    device_test = models.ForeignKey('Device_Results',on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
  
    
