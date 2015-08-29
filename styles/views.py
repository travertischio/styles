from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from styles.models import BeerStyle
from styles.forms import BeerForm


def index(request):
  form = BeerForm()
  template = loader.get_template('styles/index.html')
  context = RequestContext(request, {
  	'form': form,
  })
  return HttpResponse(template.render(context))


def detail(request, name):
  this_beer = BeerStyle.objects.filter(name=name)[:1]
  template = loader.get_template('styles/detail.html')
  context = RequestContext(request, {
  	'this_beer': this_beer,
  })
  if this_beer:
  	return HttpResponse(template.render(context))
  else:
  	raise Http404


def results(request):
  if request.method == 'POST':
	  form = BeerForm(request.POST)
	  if form.is_valid():
	  	ibu = form.cleaned_data['ibu']
	  	srm = form.cleaned_data['srm']
	  	abv = form.cleaned_data['abv']
	  	country = form.cleaned_data['country']
	  	for beer in BeerStyle.objects.all():
	  		beer.comparison(ibu, srm, abv, country)

	  list_beers = BeerStyle.objects.order_by('similarity')[:10]
	  template = loader.get_template('styles/results.html')
	  context = RequestContext(request, {
	  	'list_beers': list_beers,
	  	'form': form,
	  })
	  if list_beers:
	  	return HttpResponse(template.render(context))
	  else:
	  	raise Http404

  else:
    HttpResponseRedirect('styles:index')


def list(request):
	beer_list = BeerStyle.objects.order_by('name')
	template = loader.get_template('styles/list.html')
	context = RequestContext(request, {
		'beer_list': beer_list
	})
	if beer_list:
		return HttpResponse(template.render(context))
	else:
		raise Http404


def countrys(request):
	beer_list = BeerStyle.objects.order_by('country')
	country = "Belgium"
	country_list = [country]
	for beer in beer_list:
		if beer.country != country:
			country = beer.country
			country_list.append(country)
	template = loader.get_template('styles/countrys.html')
	context = RequestContext(request, {
		'country_list': country_list
	})
	if beer_list:
		return HttpResponse(template.render(context))
	else:
		raise Http404


def bycountry(request, name):
	beer_list = BeerStyle.objects.filter(country=name)
	template = loader.get_template('styles/bycountry.html')
	context = RequestContext(request, {
		'beer_list': beer_list
	})
	if beer_list:
		return HttpResponse(template.render(context))
	else:
		raise Http404