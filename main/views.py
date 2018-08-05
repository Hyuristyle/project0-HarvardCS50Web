from django.http import HttpResponse
from django.shortcuts import render

from .models import PhotoEntry

# Create your views here.
def index(request):
	context = {
		"photo_entries": PhotoEntry.objects.all()
	}
	return render(request, "main/index.html", context)