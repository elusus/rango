from django.http import HttpResponse

def index(request):
	return HttpResponse(
		"Rango says hello world!<br><br><a href='about/'>Here is a link to the about page</a>"
		)

def about_page(request):
	return HttpResponse(
		"Rango says: Here is the about page.<br><br><a href='/rango/'>Here is a link back to the about page</a>"
		)