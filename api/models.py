from django.db import models

# Create your models here.
class ListBook(models.Model):
    identifier = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100 ,  null=True, blank=True)
    url= models.URLField( null=True, blank=True)
    direct_url = models.URLField( null=True, blank=True)
    def __str__(self):
        return {self.id} - {self.name} - {self.url}
    
