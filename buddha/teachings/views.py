from django.http import HttpResponse

def index(request):
	return HttpResponse("Hi, There! This is my first django view!")

