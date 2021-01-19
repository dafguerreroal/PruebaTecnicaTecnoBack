from django.db import models

class Card(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    texto = models.TextField()
    
