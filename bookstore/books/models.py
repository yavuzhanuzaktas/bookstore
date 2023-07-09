from django.db import models

# Create your models here.
class Author(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')
    



class Book(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')
    author = models.ForeignKey(Author,on_delete=models.CASCADE)       
    price = models.DecimalField(decimal_places=2,max_digits=4,null=True)
    #models.CASCADE -> ilişkisel veritabanında eğer bir yazar silinirse veri tabanından ; o yazara ait kitaplarında silinmesini sağlar.
    #1-N ilişkisi söz konusu yani bir yazarın birden çok kitabı olabilir.
    #1-N ilişkisi söz konusu yani bir türün birden fazla kitabı olabilir.
