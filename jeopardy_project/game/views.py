from django.shortcuts import get_object_or_404, render

from django.template import loader, RequestContext

from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
	air_date_list = Question.objects.all().values('air_date').order_by('air_date').distinct()
	context = RequestContext(request, {'air_date_list': air_date_list,})
	return render(request, 'game/index.html', context)


def date(request, air_date):
	categories_list = Question.objects.all().values('category').filter(air_date=air_date, current_round='Jeopardy!').distinct()
	current_round = 'Jeopardy'

	context = RequestContext(request, {'categories_list': categories_list, 
									   'current_round': current_round,
							})
	return render(request, 'game/air_date.html', context)
