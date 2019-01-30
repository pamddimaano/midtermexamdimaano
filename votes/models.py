from django.db import models

# Create your models here.
class Candidate(models.Model):
	firstname = models.CharField(max_length=100) 
	lastname = models.CharField(max_length=100) 										
	position = models.CharField(max_length=100) 									
	birthdate = models.DateTimeField('date of birth')
	platform = models.TextField(max_length=200)

	def __str__(self):
		return 'Candidate: {}'.format(self.firstname, ' ', self.lastname)


class Position(models.Model):
	name = models.CharField(max_length=100) 
	description = models.TextField(max_length=200)


class Vote(models.Model):
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name = 'candidate', null=True, blank=True) 										
	vote_datetime = models.DateTimeField('vote date')