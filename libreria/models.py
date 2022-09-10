from django.db import models

# Create your models here.
class book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description", null=True)
    image = models.ImageField(upload_to="images/", verbose_name="Image", null=True)

    def __str__(self):
        fila = "Title: " + self.title + "-" + "Description: " + self.description
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()