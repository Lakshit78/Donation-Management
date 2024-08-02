from django.db import models




class record2(models.Model):
	username=models.CharField(max_length=100,unique=True)
	role=models.CharField(max_length=100)


	def __str__(self):
		return self.username



class record5(models.Model):
	
	username=models.CharField(max_length=100)
	child=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	amount=models.CharField(max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username

class price(models.Model):
	
	name=models.CharField(max_length=100)
	amount=models.CharField(max_length=100)

	def __str__(self):
		return self.name

class relation(models.Model):
	
	student=models.CharField(max_length=100)
	donator=models.CharField(max_length=100)

	def __str__(self):
		return self.student