from django.shortcuts import render
from recipe.models import Recipe, Step
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
	recipes = Recipe.objects.all()

	context = RequestContext(request, {
		'recipes': recipes,
	})
	return render_to_response('recipe/index.html', context_instance = context)

def search(request):
	context = {'recipes' : []}
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		recipes = Recipe.objects.filter(name__icontains=q)
		context = {
			'recipes': recipes
		}
	return render(request, 'recipe/search.html', context)

def recipe(request, number):
	recipe = Recipe.objects.get(id=number)
	steps = recipe.step_set.all()

	context = {
		'recipe': recipe,
		'steps': steps,
	}
	return render(request, 'recipe/recipe.html', context)
