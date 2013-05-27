from django.db import models

class UserInput(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length = 200)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
