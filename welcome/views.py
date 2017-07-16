from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render_to_response
from welcome.models import Question
# Create your views here.
def index(request):
	#context_instance=RequestContext(request)
    return render_to_response('index.html')

'''def play(request):
    content={
        'title' : "django",
        'author' : "dikshnat",
    }

    return render_to_response('play.html',content)
'''
def play(request):
	#context_instance=RequestContext(request)
    game = Question.objects.all()
    return render_to_response('play.html',{'game':game})
	
	
def verify(request):
	#context_instance=RequestContext(request)
	#return render_to_response("<html><head><body>YOU submitted the answer</body></head></html>")
	return render_to_response("<html><head><body>dikshant u submitted</body></head></html>")
	#return HttResponse("<html><head><body>dikshant u submitted</body></head></html>")

	'''def contact(request):
    form_class = ContactForm
    
    return render(request, 'contact.html', {
        'form': form_class,
    })'''