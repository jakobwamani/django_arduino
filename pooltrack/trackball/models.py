from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class pool_table(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pool_name = models.CharField(max_length=200)
	pool_location = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.pool_name


class action_table(models.Model):
	# 'id', 'status', 'date', 'time'
	pool_table = models.ForeignKey(pool_table, on_delete=models.CASCADE ,unique = False)
	date = models.DateField()
	time = models.TimeField()
	status = models.CharField(max_length=200)
   
	def __str__(self):
		return self.pool_table,self.status,self.date,self.time
