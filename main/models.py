from django.db import models

# Create your models here.
class PhotoEntry(models.Model):
	photo = models.ImageField(upload_to="images/photos/")
	#thumbnail = 
	title = models.CharField(max_length=32)
	position = models.IntegerField()

	def __str__(self):
		return f"{position} - {title}"