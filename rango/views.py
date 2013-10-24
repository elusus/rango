from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am from the context"}
	return render_to_response('rango/index.html', context_dict, context)

def about_page(request):
	return HttpResponse(
		"Rango says: Here is the about page.<br><br><a href='/rango/'>Here is a link back to the about page</a>"
		)