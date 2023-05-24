from django.db import models
# Create your models here.

class catalog(models.Model):
    groupName=models.CharField(max_length=64)
    groupPic = models.ImageField(
             height_field=None,
              width_field=None,
              max_length=100,
              default=None)
    
class detail(models.Model): 
    catalog=models.ForeignKey(catalog,on_delete=models.CASCADE)
    detailName=models.CharField(max_length=64)
    detailPic = models.ImageField(
        upload_to='detail/',
        height_field=None,
        width_field=None,
        max_length=100,
        default=None)

    