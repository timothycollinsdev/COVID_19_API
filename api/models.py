from django.db import models

# Create your models here.
class CoronaCounrty(models.Model):
	country = models.CharField(max_length=250, null=True, blank=True)
	total_cases = models.IntegerField(null=True, blank=True)
	new_cases = models.IntegerField(null=True, blank=True)
	total_deaths = models.IntegerField(null=True, blank=True)
	new_deaths = models.IntegerField(null=True, blank=True)
	total_recovered = models.IntegerField(null=True, blank=True)
	active_cases = models.IntegerField( null=True, blank=True)
	serious_cases = models.IntegerField(null=True, blank=True)
	tot_cases = models.CharField(max_length=250, null=True, blank=True)
	track_it = models.BooleanField(default=False)
	
	def __str__(self):
		return "%s - %s"%(self.pk, self.country)
	

class TrackCountry(models.Model):
	country = models.CharField(max_length=250, null=True, blank=True)
	total_cases = models.IntegerField(null=True, blank=True)
	new_cases = models.IntegerField(null=True, blank=True)
	total_deaths = models.IntegerField(null=True, blank=True)
	new_deaths = models.IntegerField(null=True, blank=True)
	total_recovered = models.IntegerField(null=True, blank=True)
	active_cases = models.IntegerField(null=True, blank=True)
	serious_cases = models.IntegerField(null=True, blank=True)
	tot_cases = models.CharField(max_length=250, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return "%s - %s"%(self.pk, self.country)
