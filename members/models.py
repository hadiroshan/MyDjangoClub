from django.db import models


class listmember(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=12)
    adr=models.TextField()
    def __str__(self) :
        return str(self.id)+"\t"+self.name+"\t"+str(self.mobile)+"\t"+self.adr

# Create your models here.
