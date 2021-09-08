from django.db import models
from django.core.urlresolvers import reverse

class Referral(models.Model):
    name = models.CharField(max_length=250)
    physician = models.CharField(max_length=250)
    serviceProvider = models.CharField(max_length=250)
    reason = models.CharField(max_length=250)
    date = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('refer:details', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.name + ' - ' + self.reason

class Patient(models.Model):
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE)
    history = models.CharField(max_length=1000)
    is_review = models.BooleanField(default=False)

    def __str__(self):
        return self.history
