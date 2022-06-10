from django.db import models

class HelpRequest(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=40)
    text = models.TextField()
    date_default = models.DateField('date default')
    pub_date = models.DateTimeField('date published', auto_now=True, auto_now_add=False)
    update = models.DateTimeField('date updated', auto_now=False, auto_now_add=True)
    contacts = models.TextField()

    def __str__(self):
        return self.title
