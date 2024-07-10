from django.db import models

# Create your models here.

class Navbar(models.Model):
    id_nav = models.AutoField(db_column="idNav", primary_key=True)
    nom_nav = models.CharField(max_length=20, blank=False, null=False)
    url_nav = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
	    return str(self.nom_nav)
