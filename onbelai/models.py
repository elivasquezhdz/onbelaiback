from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
['AutoField', 'BigAutoField', 'BigIntegerField', 'BinaryField', 'BooleanField',
'CharField', 'CommaSeparatedIntegerField', 'DateField', 'DateTimeField', 'DecimalField',
'DurationField', 'EmailField', 'Field', 'FileField', 'FilePathField', 'FloatField', 
'GenericIPAddressField', 'IPAddressField', 'ImageField', 'IntegerField', 'JSONField',
'ManyToManyField', 'NullBooleanField', 'OneToOneField', 'PositiveBigIntegerField', 
'PositiveIntegerField', 'PositiveSmallIntegerField', 'SlugField', 'SmallAutoField', 
'SmallIntegerField', 'TextField', 'TimeField', 'URLField', 'UUIDField', 'fields', 'fields_all']
'''

class Project(models.Model):
  name = models.CharField(max_length=255)
  class_to_detect =  models.CharField(max_length=255)
  prompt_image = models.TextField()
  #start_image = models.ImageField(upload_to="/images")
  prompt_change = models.TextField()
  #image_change = models.ImageField(upload_to="/images")
  author = models.ForeignKey(User, on_delete=models.CASCADE)