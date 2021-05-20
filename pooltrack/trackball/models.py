from django.db import models

# Create your models here.
class pool_table(models.Model):
    pool_name = models.CharField(max_length=200)
    pool_location = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pool_table


class action_table(models.Model):
	# 'id', 'status', 'date', 'time'
	pool_table = models.ForeignKey(pool_table, on_delete=models.CASCADE ,unique = False)
	date = models.DateField()
	time = models.TimeField()
	status = models.CharField(max_length=200)
   
	def __str__(self):
		return self.status
