from django.http import HttpResponse
from django.shortcuts import render

#from .models import PhotoEntry

class PhotoEntry:
	def __init__(self, photo, thumbnail, title, position):
		self.photo = photo
		self.thumbnail = thumbnail
		self.title = title
		self.position = position

	def __str__(self):
		return f"{self.position} - {self.title}"

tmp_entries = []

for i in range(1, 34):
	tmp_entries.append(PhotoEntry(f"photo ({i}).jpg", f"thumbnail ({i}).jpg", f"Photo {i}", i))

# Create your views here.
def index(request):
	context = {
		"photo_entries": tmp_entries # PhotoEntry.objects.all()
	}
	return render(request, "main/index.html", context)

def about(request):
	return render(request, "main/about.html")

def tools(request):
	return render(request, "main/tools.html")

def learning(request):
	return render(request, "main/learning.html")